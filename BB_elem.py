import requests
from requests import Request
import json
import time


url="https://www.ele.me/restapi/shopping/restaurant/150971585"

def getTime():
	return(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
	

isOpen=0;
while isOpen==0:
	rr=requests.get(url)
	print (rr.text)
	if rr==200:
		continue
	jsonp=json.loads(rr.text)
	status=jsonp["status"]
	print (status)
	if status==1 :
		isOpen =1
		break
	print (getTime(),"---",isOpen)
	time.sleep(60)
	
import os
os.system("mshta vbscript:msgbox(\"要吃饭啦   (•̀ᴗ•́)و ̑̑ \",64,\"eleme\")(window.close)")
import winsound
winsound.Beep(4000,2200)


