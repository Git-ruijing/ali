#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#edit from Filename:urllib2-header.py
'''
{
    "success": true,
    "result": {
        "paging": {
            "n": 1452,
            "page": 1,
            "pages": 146
        },
        "items": [
            {
                "shopUserId": "1762474504",
                "title": "韩国时尚带锁拉杆箱行李箱",
                "status": 1,
                "totalNum": 10,
                "requestNum": 23235,
                "acceptNum": 0,
                "reportNum": 0,
                "isApplied": false,
                "shopName": "surelaptop旗舰店",
                "showId": "1972834",
                "startTime": 1479916800000,
                "endTime": 1480518000000,
                "id": "28854045",
                "type": 1,
                "pic": "//img.alicdn.com/bao/uploaded/TB1QK8UOXXXXXbMaXXXXXXXXXXX.jpg",
                "shopItemId": "536989289866",
                "price": 799
            }
        ]
    },
    "~hsf~": {
        "success": true,
        "msgCode": null,
        "httpStatusCode": 200,
        "msgInfo": null,
        "model": {
            "sysTime": 1479991505375,
            "returnCode": 0,
            "errCode": 0,
            "resultMsg": "",
            "module": [
                {
                    "moduleIndex": null,
                    "moduleLazyCode": null,
                    "moduleName": "showList",
                    "moduleLoadType": 1,
                    "isSuccess": true,
                    "errorMsg": null,
                    "errorCode": null,
                    "totalNum": 1452,
                    "totalPage": 145,
                    "server": "try011183080095.eu13",
                    "moduleData": [
                        {
                            "tryId": 28854045,
                            "shopUserId": 1762474504,
                            "itemId": 536989289866,
                            "itemUrl": "//detail.tmall.com/item.htm?id=536989289866",
                            "title": "韩国时尚带锁拉杆箱行李箱",
                            "picUrl": "//img.alicdn.com/bao/uploaded/TB1QK8UOXXXXXbMaXXXXXXXXXXX.jpg",
                            "status": 1,
                            "catId": 105,
                            "catname": "箱包",
                            "parentId": 100,
                            "parentCatname": null,
                            "currentPrice": 799,
                            "totalNum": 10,
                            "requestNum": 23235,
                            "acceptNum": 0,
                            "reportNum": 0,
                            "leftTimeToStart": -74594113,
                            "leftTimeToEnd": 526605887,
                            "markSum": null,
                            "mark": null,
                            "starSize": null,
                            "lifeCycle": null,
                            "isExamItem": null,
                            "isApplied": false,
                            "isAnswered": false,
                            "wapScm": null,
                            "wapPvid": null,
                            "qiStar": null,
                            "qiNote": "",
                            "shopName": "surelaptop旗舰店",
                            "itemShowType": 1,
                            "showId": 1972834,
                            "discountPrice": 0,
                            "typeDesc": null,
                            "isBy0": false,
                            "auditType": 0,
                            "msg": null,
                            "features": null,
                            "tryActivityId": 0,
                            "activity": 0,
                            "itemNewDetailUrl": "//shop105490584.taobao.com/tryshop.htm?id=28854045",
                            "startTime": "2016-11-23T16:00:00.000Z",
                            "endTime": "2016-11-30T15:00:00.000Z",
                            "showBeginTime": "2016-11-23T16:00:00.000Z",
                            "showEndTime": "2016-11-30T15:00:00.000Z",
                            "createTime": null,
                            "votes": null,
                            "avgVotes": null
                        }
                    ]
                }
            ]
        },
        "headers": {},
        "bizExtMap": null
    }
}
'''
import urllib2,urllib,json,time
import sys

from StringIO import StringIO
import gzip
 
 
#抓取网页内容-发送报头-1
def APIget(page):
	url= "https://shishi.taobao.com/api3/call?what=show&page="+str(page)+"&pageSize&api=x%2Fsearch"
	send_headers = {

	#POST /api3/call?what=show&page=2&pageSize&api=x%2Fsearch HTTP/1.1
	'Host':'shishi.taobao.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/50.0',
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate, br',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'X-Requested-With':'XMLHttpRequest',
	'x-csrf-token':'EgszEGve3BkGHHdEc07Y',
	'Referer':'https://shishi.taobao.com/item/list.htm?spm=a1z0i.1000799.1996938005.2.RsUveB',
	'Content-Length':'8',
	'Cookie':'thw=cn; t=a0d83d6320e546f735f6df51d0100522; uc1=cookie14=UoWwLQnqbJfqpQ%3D%3D; v=0; cookie2=1c77a96b73e75e3b57a09953cb5fa919; _tb_token_=EgszEGve3BkGHHdEc07Y',
	'Connection':'keep-alive'
	}

	# postdata={'status':'1'}
	postdata=dict(status='1')
	postdata=urllib.urlencode(postdata)
	req = urllib2.Request(url,data=postdata,headers=send_headers)
	r = urllib2.urlopen(req)

	receive_header = r.info()     #返回的报头信息
	if receive_header.get('Content-Encoding') == 'gzip':
		buf = StringIO( r.read())
		f = gzip.GzipFile(fileobj=buf)
		data = f.read()
	#print data

	# sys.getfilesystemencoding() 
	html1 = data.decode('utf-8','replace').encode(sys.getfilesystemencoding()) #转码:避免输出出现乱码
	print html1 
	print '####################################'
	#html=json.encode(data)
	#tt=json.loads(data)
	print receive_header
	print '####################################'
	return data
	
#  抓取开始     需要设置后一次抓寻得itemid   以控制抓取结束
pointer ="17624745041111"  #结束指针

seed=json.loads(APIget(page=1));
pageall=seed["result"]["paging"]["pages"]
print pageall

page=2
list=[APIget(page=1)]
while (page<=pageall):
	print  "*****************************this page:"+str(page)+"***********************************"
	cache=APIget(page)
	list.append(cache)
	if cache.find(pointer)!=-1:
		break
	page=page+1

print  "*****************************spider  end***********************************"

def time2date(time1):
	x = time.localtime(float(time1))
	return str(time.strftime('%Y-%m-%d %H:%M:%S',x))

#数据保存
print  "*****************************the count of pages:"+str(len(list))+"***********************************"
f = file ("D:/item.txt","a")
#f.writelines(["shopUserId","title","status","totalNum","requestNum","isApplied","shopName","showId","startTime","endTime","id","pic","shopItemId","price"])
f.writelines("shopUserId,title,status,totalNum,requestNum,isApplied,shopName,showId,startTime,endTime,id,pic,shopItemId,price"+"\n")
for jsonstr in list:
	#print str(jsonstr).decode('utf-8','replace').encode("gbk")
	shishijson=json.loads(jsonstr)
	itemjosn=shishijson["result"]["items"]
	for item in itemjosn:		   #f.writelines(item["shopUserId"]+item["title"]+item["status"]+item["totalNum"]+item["requestNum"]+item["isApplied"]+item["shopName"]+item["showId"]+time2date(item["startTime"])+time2date(item["endTime"])+item["id"]+item["pic"]+item["shopItemId"]+item["price"]+"\n")
		if(item["shopUserId"]==pointer):
			break
		f.writelines((str(item["shopUserId"])+","+item["title"]+","+str(item["status"])+","+str(item["totalNum"])+","+str(item["requestNum"])+","+str(item["isApplied"])+","+item["shopName"]+","+str(item["showId"])+","+time2date(item["startTime"]/1000)+","+time2date(item["endTime"]/1000)+","+str(item["id"])+","+item["pic"]+","+str(item["shopItemId"])+","+str(item["price"])+"\n").encode('utf-8'))

f.close