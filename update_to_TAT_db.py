#!/usr/bin/python
from sys import argv
import MySQLdb
from astropy.io import fits as pyfits
import os
import sys

def insert_data_file(filename,path):

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
        try:
            cursor.execute(sql)
            db.commit()
            print("{0},ok".format(sql))
        except:
            db.rollback()
        sql="UPDATE data_file SET `FILEPATH` = '{0}' WHERE `FILENAME` = {1} ;".format(path,name)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        for header_element in key:
            for data_element in datakey:
                if header_element==data_element:
                    if (type(header[data_element]) == bool) or (type(header[data_element]) == int) or (type(header[data_element]) == float):
                        sql="UPDATE data_file SET `{0}` = {1} WHERE `FILENAME` = {2} ;".format(data_element,header[header_element],name)
                    else:
                        sql="UPDATE data_file SET `{0}` = '{1}' WHERE `FILENAME` = {2} ;".format(data_element,header[header_element],name)
            if 'OBSERVAT'== header_element:
                sql="UPDATE data_file set `SITENAME`  = '{0}' WHERE `FILENAME`= {1};".format(header['OBSERVAT'],name)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        for data_element in datakey: 
            if ('subbed'== data_element):
                try:
                    header['subbed'] is True
                except:
                    sql="UPDATE data_file set `subbed`  = False WHERE `FILENAME`= {0};".format(name)
                    print(sql)
            if ('divfitted'== data_element):
                try:
                    header['divfitted'] is True
                except:
                    sql="UPDATE data_file set `divfitted`  = False WHERE `FILENAME`= {0};".format(name)
                    print(sql)
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
    fo=open("back_up_path","r")
    line=fo.readlines()
    lineread=line[0][:-1].split("=")
    if lineread[0]=="path":
        backuppath=lineread[1]
    else:
        print("ERROR: not a path")
    fo.close()
    for root, dirs, files in os.walk(backuppath):
        for name in dirs:
            path=os.path.join(root, name)
            print(path)
            os.chdir(path)
            os.system("ls *.fit* > list.txt")
            f=open('list.txt','r')
            for line in f.readlines():
                line=line.strip()
                insert_data_file(line,path)
            f.close()
            os.remove("list.txt")

