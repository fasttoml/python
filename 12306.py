import requests
import mod_config
import time
import random
class Get12306():
    #定义函数获取地区码
    def getdqm(self, m):
         f=open("hcdqm.txt","r")
         for i in f:
             list_a=i.split("|")
             if m==list_a[1]:
                 return list_a[2]
             else:
                pass
         f.close()
    #定义属性出发日期
    @property
    def date(self):
        return(self.date_s)
    @date.setter
    def date(self,date_s):
        self.date_s=date_s
    #定义属性出发地点
    @property
    def source(self):
        return(self.road_s)
    @source.setter
    def source(self,road_s):
        self.road_s=road_s
    #定义属性目的地地点
    @property
    def destination(self):
        return self.road_d
    @destination.setter
    def destination(self, road_d):
        self.road_d=road_d
    #定义函数返回12306的数据地址
    def getUrl(self,date,s,d):
        url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (date,self.getdqm(s),self.getdqm(d))
        return url
    #定义函数获取json数据
    def get12306Json(self,url):
        json_12306=requests.get(url).json()
        list_json=json_12306["data"]["result"]
        return(list_json)
    # 定义函数返回列车信息表格
    def get12306Table(self,list_json):
        # 索引3返回车次信息
        # 索引8返回出发时间
        # 索引9返回到站时间
        # 索引10返回全程所用时间
        # 索引23返回软卧信息
        # 索引29返回硬座信息

        str_msg="找到%s个车辆匹配" % len(list_json)
        print("========%s=========" % str_msg)
        #封装车次信息
        for i in list_json:
            a=i.split("|")
            print("车次:%s,出发时间:%s，到站时间:%s,全程%s小时  软卧有%s张票    硬座有%s张票" % (a[3],a[8],a[9],a[10],a[23],a[29]))
        pass
    #函数返回一个介于30-60的整数，用来模仿人类的查询活动
    def return_randomTime(self):
        return(int(random.uniform(30,60)))
def main():
    g12306=Get12306()
    g12306.date = input("请输入查询的日期 &例如2015-01-01：")
    g12306.source=input("请输入查询的起点 &例如：北京：")
    g12306.destination=input("请输入查询的终点 &例如：南京：")
    url=g12306.getUrl(g12306.date,g12306.source,g12306.destination)
    json_url=g12306.get12306Json(url)
    #间隔30秒刷新一下显示内容
    while True:
        g12306.get12306Table(json_url)
        time.sleep(g12306.return_randomTime())
    pass
if __name__=="__main__":
    main()

