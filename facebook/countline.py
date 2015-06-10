# -*- coding: gbk -*-

import os

Key_num = {}

dirroot = "/home/gaochuan/fetch/facebook/quchong_Key/"

for parent, dirnames, filenames in os.walk(dirroot):
    #print filenames
    fout = open("Key_Nums_facebook.txt", "a")
    for key in filenames:
        filepath = dirroot + key
        #print filepath
        #fin = open(file, "r")
        count = len(open(filepath,'rU').readlines())
        Key_num[key] = count
        result = key + '\t\t\t' + str(count)
        fout.write(result)
        fout.write('\n')
    fout.close()
#print Key_num
