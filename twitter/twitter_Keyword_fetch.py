#coding=gbk 

import tornado.httpclient
import sys
import time
import json
import os

def fetchbody(url):
    http_header = {}
    http_request = tornado.httpclient.HTTPRequest(url=url, method='GET', headers=http_header, connect_timeout=20, request_timeout=600)

    http_client = tornado.httpclient.HTTPClient()
    print "__________ START __________"
    http_response = http_client.fetch(http_request)
    print "__________ FINISHI__________"

    print http_response.code

    all_fields = http_response.headers.get_all()
    for field in all_fields:
        print field
    #file_ob = open("facebook.json", 'w')
    #file_ob.write(http_response.body)
    #file_ob.close()
    #print http_response.body
    return http_response.body

def geturl(Keywords):
    url = []
    for i in Keywords:
        tmp = "http://54.248.44.79:8888/post/twitter?kw=%s&num=50" % i
        url.append(tmp)
    return url

def getKey(fop):
    lst = []
    while True:
        r = fop.readline().strip('\r\n')
        r = r.replace(" ", "+")
	if len(r) == 0:
            break
        lst.append(r)#[0:len(r)-1])
    #print lst
    return lst

def getNowTime():
    return time.strftime("%Y_%m_%d %H-%M-%S", time.localtime(time.time()))


if __name__ == "__main__":
    fop = open("Keywords.txt", "r")
    Key = getKey(fop)
    Url = geturl(Key)
    #print Url
    fop.close()
    for i in range(len(Url)):
        now = getNowTime()
        time.sleep(3)
	response = fetchbody(Url[i])
        #print type(response)
	#print json.reads(response)
	#print Key
        name = Key[i] + ' ' + now
        print name + ' ' + Url[i]
        path = "/home/gaochuan/fetch/twitter/result_Key/%s" % Key[i]
	print path
	if os.path.exists(path) != 1:
		os.mkdir(r"result_Key/%s" % Key[i].decode('utf-8'))
	fw = open("result_Key/%s/%s.json" % (Key[i].decode('utf-8'), now), "a+")
        fw.write(response)
        fw.close()
