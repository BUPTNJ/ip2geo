# 爬取所有城市政府网站对应的url
import re
import requests
from lxml import etree
import file_tool
import time
import copy
from socket import gethostbyname
from urllib import parse

# 一次性使用文件，内部全写死
if __name__ == '__main__':
    wait_s = 0.2

    resp = requests.get('http://www.114piaowu.com/zhengfu')
    content = resp.text


    html = etree.HTML(content)
    prov_blocks = html.xpath('//dl')
    dicts = []
    prov_names= []
    columns = ['province', 'city', 'hostname', 'ip']
    for prov_block in prov_blocks:
        dict = {}
        provs = prov_block.xpath('./dt/a/text()')
        if provs != []:
            prov_name = provs[0].replace('政府网','')
        else:
            continue
        dict['province'] = prov_name
        city_blocks = prov_block.xpath('./dd/a')
        for city_block in city_blocks:
            
            time.sleep(wait_s)
            city_name = city_block.xpath('text()')[0]
            dict['city'] = city_name
            city_href = city_block.xpath('@href')[0]
            new_resp = requests.get(city_href)
            new_html = etree.HTML(new_resp.text)

            url = new_html.xpath('.//div[@class="sub-left"]')[0].xpath('./dl')[1].xpath('./dd')[0].xpath('./a/text()')[0]
            hostname = parse.urlparse(url).hostname
            if hostname == None:
                hostname = url
            dict['hostname'] = hostname
            try:
                dict['ip'] = gethostbyname(hostname)
            except Exception as e:
                print ("Error: dns解析失败: ",dict['hostname'])
                dict['ip'] = '缺失'
            dicts.append(copy.deepcopy(dict)) # 深坑，注意使用深拷贝
            print(dict)
            
            file_tool.save_csv([dict], 'gov_bac.csv', columns,False)    
    file_tool.save_csv(dicts,'gov.csv',columns,True)