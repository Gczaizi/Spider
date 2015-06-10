# -*- coding: utf-8 -*-

import os
import sys
import os.path
import json

dirroot = "/home/gaochuan/fetch/twitter/result_Name/"
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
                print type(json_list)
                #if isinstance(json_list, list) == False:
                    #continue
                #fout = open("quchong_Key2/%s.json" % key.decode('utf-8'), "a+")
                try:
                    li = json.loads(json_list)
                    #print type(li)
                    #print li
                    for di in li['posts']:	#遍历li，每个di是一个完整的json数据
                        #print type(di['id'])
                        #print di['id']		#di['id']是每个json数据中的id对应的value。
                        #print di
                        total_di[di['id']] = di	#根据di中的id字段值去重，total_di是以id的值为key，json数据为value的字典
                    #for id in total_di:	#total_di[id]是每个id对应的json数据
                        #print id
                        #print type(total_di[id])
                        #total_di_per = json.dumps(total_di[id])
                    #total_di_store = json.dumps(total_di)
                    #print total_di_store
                        #fout.write(total_di_per)
                        #fout.write('\n')
                    #fout.close()
                    #total_di.clear()
                    #print ("______file end________")
                except Exception, e:
                    pass

            fout = open("quchong_Name2/%s.json" % key.decode('utf-8'), "a+")
            for id in total_di: #total_di[id]是每个id对应的json数据
                print id
                print type(total_di[id])
                total_di_per = json.dumps(total_di[id])
                #total_di_store = json.dumps(total_di)
                #print total_di_store
                fout.write(total_di_per)
                fout.write('\n')
            fout.close()
        total_di.clear()
        print ("_______key end________")
            
