# -*- coding: gbk -*-

import os
import sys
import os.path
import json

dirroot = "/home/gaochuan/fetch/twitter/tmp/"
#line_num = 0
total_di = {}

for parent,dirnames,filenames in os.walk(dirroot):
    #print ("enter:" + dirroot)
    for key in dirnames:
        #print dirroot + key
        for parent, dirnames, filenames in os.walk(dirroot + key + "/"):
            print ("enter:" + dirroot + key + "/")
            #print filenames
            #print dirnames
            for filename in filenames:
                file = dirroot + key + "/" + filename
                print ("read: " + file)
		#total_di = {}
                fin = open(file,'r')
                json_list = fin.readline()
                fin.close()
                #print type(json_list)
                #if isinstance(json_list, list) == False:
                    #continue
                fout = open("tmp2/%s.json" % key.decode('utf-8'), "a+")
                try:
                    li = json.loads(json_list)
                    #print type(li)
                    #print li
                    for di in li['posts']:
                        #print type(di['id'])
                        print di['id']
                        #print di
                        total_di[di['id']] = di
                    for di in total_di:
                        #print total_di[di]
                        total_di_per = json.dumps(total_di[di])
                        print total_di_per
                        #print total_di_per
                        fout.write(total_di_per)
                        fout.write('\n')
                    fout.close()
                    total_di.clear()
                    #print ("______file end________")
                except Exception, e:
                    pass
            print ("_______key end________")
