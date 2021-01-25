import requests
import re
import time
import sys


CourseId = "00853204"                                                          #课程号
TeacherId="1351"                                                               #教师号
cookies="ASP.NET_SessionId=un0240dcdkbiw35hux4jiox"                            #cookie
timeDelay = 0




formdata = {"PageIndex": "1",
"PageSize": "10",
"FunctionString": "LoadData",
"CID": CourseId,
"CourseName": "",
"IsNotFull": "false",
"CourseType": "B",
"TeachNo": TeacherId,
"TeachName": "",
"Enrolls": "",
"Capacity1":"" ,
"Capacity2":"" ,
"CampusId":"" ,
"CollegeId":"" ,
"Credit": "",
"TimeText":"", }
RequestUrl="http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/QueryCourseCheck"
RequestHeader={
"Accept": "text/html, */*; q=0.01",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "219",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie": cookies,
"Host": "xk.autoisp.shu.edu.cn",
"Origin": "http://xk.autoisp.shu.edu.cn",
"Referer": "http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/FuzzyQuery",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
i=0


def get_course():
    RequestUrl="http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/VerifyDiffCampus"
    formdata={"cids": CourseId,
    "tnos":TeacherId}
    response = requests.post(url=RequestUrl,headers=RequestHeader,data=formdata)
    RequestUrl="http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/CourseSelectionSave"
    response = requests.post(url=RequestUrl,headers=RequestHeader,data=formdata)
    print (response.text)
while(True):
    i=i+1
    try:
        response = requests.post(url=RequestUrl,headers=RequestHeader,data=formdata,timeout=1)
        peopleNum=re.findall("<td style=\"text-align: center;\">(.*?)</td>",response.text)
        print (peopleNum[1],peopleNum[2],"第%d次"%i)
        if (int(peopleNum[2])<int(peopleNum[1])):
            get_course()
            break
    
    except:
        print("timeout")
    time.sleep(timeDelay)

