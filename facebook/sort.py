# -*- coding: gbk -*-

import json
import os

dirroot = "/home/gaochuan/fetch/facebook/quchong_Key2/"
#total_json = {}
for parent, dirnames, filenames in os.walk(dirroot):
    #print parent, dirnames, filenames
    for filename in filenames:
        filepath = dirroot + filename
        fin = open(filepath, "r")
        json_key_total_list = fin.readlines()
        fin.close()
        json_key_total = []
        #total = dict(json_key_total_list)
        #print json_key_total_list
        #print type(json_key_total_list)
        #json_key_total = json.loads(json_key_total_list)
        #print type(json_key_total)
        for json_key_per in json_key_total_list:
            #json = json.loads(json_key_per)
            #print type(json_key_per)
            json_per =  json_key_per.strip('\n')
            #print json_per
            json_dict = json.loads(json_per)
            print json_dict.get('created_time')
            json_key_total.append(json_dict)
            #print json_key_total
            #total_json[json_per['created_time']] = json_per
            #print json_per
        json_key_total.sort(key=lambda obj:obj.get('created_time'))
        fout = open('sort_Key2/%s' % filename, 'a')
        for json_dict in json_key_total:
            fout.write(json.dumps(json_dict))
            fout.write('\n')
        fout.close()
        print ('__________KEY END___________')
