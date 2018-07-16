#!/usr/bin/python                           
import MySQLdb                              #Let python use mysql
from astropy.io import fits as pyfits       #To get the header key, use pyfits
import os                                   #To use command in terminal
import sys                                  #Used in some error, we can exodus


#set useful variable fpr path. We save the path in the file back_up_path.txt.
global BACKUP_PATH_FILENAME                                                       
BACKUP_PATH_FILENAME = "/home2/TAT/programs/TAT_database/back_up_path.txt" 

global LOG
LOG="/home2/TAT/programs/TAT_database/log.txt"

# The function to deal with the data to insert Table data_file
def insert_data_file(filename,path):

    name="{0}".format(filename)           # Just set name is like string to the pyfits.header use.
    header=pyfits.getheader(filename)     # Get the header from the fit file. 
    key=header.keys()                     # Set the variable key is the key in header   
    datakey=[]                            # define the datakey is a list
    name="'{0}'".format(filename)         # Just set name be easily used in Mysql


    # Connect the Mysql and use the user "TAT" .The form is (your localhost , username, password, name of database)
    db = MySQLdb.connect("localhost", "TAT" ,"1234","TAT")    
    cursor = db.cursor()                     # Create a Cursor object to execute queries. 


    # Describe the data_file 
    sql= "desc data_file;"                      
    try:
        cursor.execute(sql)
        results=cursor.fetchall()      # The result of the Mysql command "desc data_file"
        
        # We just need the first column of "desc data_file"( its meaning is the all key in table data_file)
        for row in results:
            datakey.append(row[0])     

        # Insert the filename
        sql="insert into data_file (FILENAME) values ({0});".format(name)
        try:
            cursor.execute(sql)         #excute the "isnert into data_file...."
            db.commit()                 #do nothing
        except:
            db.rollback()               #skip if error

        # Update the path
        sql="UPDATE data_file SET `FILEPATH` = '{0}' WHERE `FILENAME` = {1} ;".format(path,name)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        # Check the "subbed" and "divfitted" in the header is True. Otherwise set them be False.  
        for data_element in datakey: 
            if ('subbed'== data_element):
                try:
                    header['subbed'] is True
                except:
                    sql="UPDATE data_file set `subbed`  = False WHERE `FILENAME`= {0};".format(name)
            if ('divfitted'== data_element):
                try:
                    header['divfitted'] is True
                except:
                    sql="UPDATE data_file set `divfitted`  = False WHERE `FILENAME`= {0};".format(name)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

        #Match all key in header and data_file.
        for header_element in key:
            for data_element in datakey:
                if header_element==data_element:
                    if (type(header[data_element]) == bool) or (type(header[data_element]) == int) or (type(header[data_element]) == float):
                        sql="UPDATE data_file SET `{0}` = {1} WHERE `FILENAME` = {2} ;".format(data_element,header[header_element],name)
                    else:
                        sql="UPDATE data_file SET `{0}` = '{1}' WHERE `FILENAME` = {2} ;".format(data_element,header[header_element],name)
            if 'OBSERVAT'== header_element:
                sql="UPDATE data_file set `SITENAME`  = '{0}' WHERE `FILENAME`= {1};".format(header['OBSERVAT'],name)
            if 'LOCATION'== header_element:
                sql="UPDATE data_file set `SITENAME`  = '{0}' WHERE `FILENAME`= {1};".format(header['LOCATION'],name)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
    # if command "desc data_file" were wrong, it would output error
    except:
        print "Error: unable to fecth data"
 
    # Unconnect the Nysql
    db.close()

    return

# Main process 
if __name__ =="__main__":
    #read the path file
    fo=open(BACKUP_PATH_FILENAME,"r")
    line=fo.readlines()
    lineread=line[0][:-1].split("=")         # I set the format in back_up_path path=.... ,thus we check where line is path
    if lineread[0]=="path":
        backuppath=lineread[1]
    else:
        print("ERROR: not a path")          # If reading the path were not a path.
        sys.exit()                          # Exodus this program
    fo.close()

    #create the file log.txt if it doesn't exist.
    fo=open(LOG,"a")
    fo.close()

    #read all file and directory under the path "/home2/TAT/data" (root --> the current directory, directory -->sll directory in the root  , files --> all the file in the root)
    # When read all file in the current directory, root will become the one of dirs
    for root, dirs, files in os.walk(backuppath):
        for name in dirs:
            path=os.path.join(root, name)    # the current directory plus the one of sub directory.

            #read the log and elimate "\n"
            fo=open(LOG,"r")
            line=fo.readlines()
            for i in range(len(line)):
                line[i]=line[i][:-1]
            fo.close()

            # Check whether it has been done. If it has been done ,it will output has already been deal. Otherwise, it will insert it.
            if path in line:
                print("{0} has already been deal ").format(path)
            else:
                os.chdir(path)
                # Let all filename contain the fit be a file, and let the filename line by line.
                os.system("ls *.fit* > list.txt")
                f=open('list.txt','r')
                # read line one by one in the list.txt
                for line in f.readlines():
                    line=line.strip()
                    insert_data_file(line,path)   # Use the function insert_data_file one by one.
                f.close()
                os.remove("list.txt")  # After inserting the database TAT, delete this file.     
                print(path,"ok")

                # Write the path dealed to log.txt
                fo=open(LOG,"a")
                fo.write(path+'\n')
                fo.close()
