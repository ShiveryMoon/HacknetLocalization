#!/usr/bin/env python3
# coding=utf-8

import os
import zipfile
import random
import time
import sys
import re

def change(path,name):
    if not ('txt' in name or 'xml' in name):
        return 
    curName = os.path.join(path,name)
    tmpName = os.path.join(path,name+".backup2")
    os.rename(curName,tmpName)
    with open(tmpName,'r') as ifile:
        with open(curName,'w') as ofile:
            ss = ifile.read()
            ss = re.sub("\r?\n","\r\n",ss)
            ofile.write(ss)
    os.remove(tmpName)

def insertSecret(path,name,secret,z):
    curName = os.path.join(path,name)
    tmpName = os.path.join(path,name+".backup")
    os.rename(curName,tmpName)
    with open(tmpName,'r') as ifile:
        with open(curName,'w') as ofile:
            ss = ifile.read()+"\r\n\r\n"+secret
            ofile.write(ss)
    change(path,name);
    z.write(curName)
    os.remove(curName)
    os.rename(tmpName,curName)

def main():
    locked = True
    while locked:
        try:
            with open("lock",'r') as f:
                print('locked')
                locked = True
                pass
        except:
            print("released")
            locked = False

    with open('lock', 'w') as f:
        pass
        
    basedir = os.getcwd();
    rootdir = "Hacknet/HacknetLocalizationBase"
    random.seed(time.time());
    flag = False;
    randomstr = sys.argv[1];
    while flag == False:
        with zipfile.ZipFile("downloads/"+sys.argv[2]+'.zip',"w") as z:
            for path,dirs,files in os.walk(rootdir):
            
                for file in files:
                    filepath = os.path.join(path,file);
                    #print(filepath);
                    change(path,file)
                    if flag == False and random.randint(0,100)==1 and ('xml' in file or 'txt' in file):
                        #print(filepath)
                        flag=True
                        insertSecret(path,file,randomstr,z)
                    else:
                        #change(path,file);
                        z.write(filepath);
    os.remove('lock')        
    return ;



if __name__ == "__main__":
    main();
else:
    print("Hello Ruby");
