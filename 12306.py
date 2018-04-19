import requests
import mod_config

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
    pass
    #定义函数返回12306的数据地址
    def getUrl(self,date,s,d):
        url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (date,self.getdqm(s),self.getdqm(d))
        return url
    #定义函数获取json数据
    def get12306Json(self,url):
        json_12306=requests.get(url).json()
        list_json=json_12306["data"]["result"]
        str_msg="找到%s个车辆匹配" % len(list_json)
        print("========%s=========" % str_msg)
        #封装车次信息
        for i in list_json:
            a=i.split("|")
            print("车次:%s,出发时间:%s，到站时间:%s,全程%s小时  软卧有%s张票    硬座有%s张票" % (a[3],a[8],a[9],a[10],a[23],a[29]))


def main():
    g12306=Get12306()
    date_s = input("请输入查询的日期 &例如2015-01-01：")
    road_s=input("请输入查询的起点 &例如：北京：")
    road_d=input("请输入查询的终点 &例如：南京：")
    url=g12306.getUrl(date_s,road_s,road_d)
    g12306.get12306Json(url)
    pass
if __name__=="__main__":
    main()

