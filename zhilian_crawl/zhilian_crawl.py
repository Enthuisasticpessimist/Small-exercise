from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
import re
##import pprint

pl = ['python','java','c','php']##创建需要搜索的职位信息列表,'java','c','php'
pl_index = 0##创建需要搜索的职位信息的列表索引

city = ['北京','上海','广州','深圳','南京','杭州']##创建需要搜索的城市列表,'上海','广州','深圳','南京','杭州'
city_index = 0##创建需要搜索的城市的列表索引

##爬取数据解析函数
def d_p(dic):
    res_dic = {'面议':0,
               '0-1000':0,
               '1001-3000':0,
               '3001-5000':0,
               '5001-8000':0,
               '8001-10000':0,
               '10001-15000':0,
               '15001-20000':0,
               '20001以上':0,
               }
    temp = list(dic.items())
    for k,v in temp:
        if k == '面议':
            res_dic['面议'] += v

        elif k == '1000元以下':
            res_dic['0-1000'] += v

        elif k == '49999元以上':
            res_dic['20001以上'] += v

        elif k == '50000元以上':
            res_dic['20001以上'] += v

        elif re.match('\d{1,5}-\d{1,5}',k):
            ave = (int(k.split('-')[0])+int(k.split('-')[1]))/2
            if ave <= 1000:
                res_dic['0-1000'] += v
            elif ave <= 3000:
                res_dic['1001-3000'] += v
            elif ave <= 5000:
                res_dic['3001-5000'] += v
            elif ave <= 8000:
                res_dic['5001-8000'] += v
            elif ave <= 10000:
                res_dic['8001-10000'] += v
            elif ave <= 15000:
                res_dic['10001-15000'] += v
            elif ave <= 20000:
                res_dic['15001-20000'] += v
            else: 
                res_dic['20001以上'] += v
        else:
            pass
    return res_dic
        
##//爬取数据解析函数



while city_index<=len(city)-1:
    while pl_index<=len(pl)-1:##对所有搜索关键字处理循环
        ##生成爬虫入口URL:
        url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl="+quote(quote(city[city_index]))+"&kw="+pl[pl_index]+"&p=1&isadv=0"
        salary_dic = {}##创建薪资字典
        while True:
                ##//将打开的网页导入bs4的对象
                html = urlopen(url).read().decode('utf-8')
                soup = BeautifulSoup(html,features='lxml')
                ##将打开的网页导入bs4的对象//
            
                ##//完成一个网页的薪资范围及其样本数量的采集
                salary = soup.find_all("td",{"class":"zwyx"})##查找当前网页的职位薪资的标签并存入bs4对象
                for sa in salary:
                    if sa.get_text() in salary_dic:
                        salary_dic[sa.get_text()]+=1 ##如果薪资字典中已有该薪资范围，则该key下数量加一
                    else:
                        salary_dic[sa.get_text()] =1 ##如果薪资字典中没有该薪资范围，则添加一个键值对，值为1
                ##完成一个网页的薪资范围及其样本数量的采集//
                        
                ##//判断是否同类搜索页面已爬取完毕
                if soup.find("a",{"class":"next-page nopress2"}) == None:
                    url = soup.find("a",{"class":"next-page"})['href']
                else:
                    break
                ##判断是否同类搜索页面已爬取完毕//

##        ##//类型爬取结果打印(测试用)
##        print(city[city_index]+"市"+pl[pl_index]+"语言相关职位薪资分布数据：\n-----------------------------------")
##        print(salary_dic)
##        print("-----------------------------------")
##        ##类型爬取结果打印//
                
        ##//将爬取数据写入txt文件(测试用)
        res = d_p(salary_dic)

        with open("ZhiLian_spider.xlsx","a") as f:
            f.write(city[city_index]+"市"+pl[pl_index]+"语言相关职位薪资分布数据\n")

            for key,value in res.items():
                f.write(key + '\t' + str(value)+"\n")
                
                
            f.write("\n")
        ##将爬取数据写入txt文件//
        
        pl_index+=1##搜索关键字列表索引加一
    city_index+=1
    pl_index=0
        
        
print('''It's done!!''')


##next_url = soup.find("a",{"class":"next-page"})['href']
##print(next_url)

##url = head_url+tail_url
##
##html = urlopen(url).read().decode('utf-8')
##soup = BeautifulSoup(html,features='lxml')
##
##chapter_name = soup.find("h3",{"class":"j_chapterName"}).get_text()
##chapter_content = soup.find_all("div",
##                    {"class":"read-content j_readContent"})
##tail_url = soup.find("a",{"id":"j_chapterNext"})['href']
##
##
##
##with open("Menshenxingtu.txt","a") as f:
##    f.write(chapter_name)
##    for child in chapter_content:
##        f.write(child.get_text()+'\n')



