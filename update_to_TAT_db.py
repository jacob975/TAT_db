#!/usr/bin/python
from sys import argv
import MySQLdb
import pyfits
import os
import sys

def insert_data_file(filename):

    name="{0}".format(filename)
    header=pyfits.getheader(filename)
    key=header.keys()
    datakey=[]
    name="'{0}'".format(filename)

    db = MySQLdb.connect("localhost", "TAT" ,"1234","TAT")
    cursor = db.cursor()

    sql= "desc data_file;"    
    
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        
        for row in results:
            datakey.append(row[0])

        sql="insert into data_file (FILENAME) values ({0});".format(name)
        print("{0},ok".format(sql)) 
        try:
            cursor.execute(sql)
            db.commit()
            print("{0},ok".format(sql)) 
        except:
            db.rollback()

        for header_element in key:
            for data_element in datakey:
                if header_element==data_element:
                    if (type(header[data_element]) == bool) or (type(header[data_element]) == int) or (type(header[data_element]) == float):
                        sql="UPDATE data_file SET `{0}` = {1} WHERE `FILENAME` = {2} ;".format(data_element,header[header_element],name)
                    else:
                        sql="UPDATE data_file SET `{0}` = '{1}' WHERE `FILENAME` = {2} ;".format(data_element,header[header_element],name)

            if 'OBSERVAT'==header_element:
                sql="UPDATE data_file set `SITENAME`  = '{0}' WHERE `FILENAME`= {1};".format(header['OBSERVAT'],name)
                if header['OBSERVAT']=='TF':
                    sql_ob="insert into observersite (SITENAME)  values ('TF');"
                    #print(sql_ob)
                    TFkey=['SITELAT','SITELONG','SITEALT']
                    TFline=['28.3003','-16.5122','0000']
                    for i in range(len(TFkey)):  
                        sql1="UPDATE observersite SET `{0}` = '{1}' WHERE `SITENAME`= 'TF';".format(TFkey[i],TFline[i])
                        #print(sql1)
                        try:
                            cursor.execute(sql1)
                            db.commit()
                        except:
                            db.rollback()
                   
                elif header['OBSERVAT']=='LI-JIANG':
                    sql_ob="insert into observersite (SITENAME)  values ('LI-JIANG');"  
                    KUkey=['SITELAT','SITELONG','SITEALT']
                    KUline=['26:41:24','100:01:48','3330']
                    for i in range(len(KUkey)):  
                        sql1="UPDATE observersite SET `{0}` = '{1}' WHERE `SITENAME`= 'LI-JIANG';".format(KUkey[i],KUkey[i])
                        try:
                            cursor.execute(sql1)
                            db.commit()
                        except:
                            db.rollback()
                try:
                    cursor.execute(sql_ob)
                    db.commit()
                except:
                    db.rollback()

            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
    except:
        print "Error: unable to fecth data"
 
    db.close()

    return
if __name__ =="__main__":
    if len(argv)==2:
        path=argv[1]
    else:
        print("ERROR:use update_to_TAT_db.py path")
        sys.exit() 
    os.chdir(path)
    os.system("ls *.fit > list.txt")
    f=open('list.txt','r')
    for line in f.readlines():
        line=line.strip()
        insert_data_file(line)
    f.close()
    os.remove("list.txt")

