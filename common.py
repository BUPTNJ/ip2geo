import pandas as pd
import ip138
import json
import yaml
import file_tool
import time

#config

columns = ['ip','country','province','city']
wait_s = 0.5

#end config

addr = '114.114.114.114'
addr2 = '8.8.8.8'
file_name = 'ip138.csv'

# 批量返回
def m_geo(ips, geoer):
    res = []
    for ip in ips:
        time.sleep(wait_s)
        res.append(geoer(ip))
    return res

# 利用各包中的creater批量创建字典
def m_create_dict(raw_dicts, creater):
    dicts = []
    for raw_dict in raw_dicts:
        dicts.append(creater(raw_dict))
    return dicts

# 根据ip地址列表请求json并存csv，全流程
def m_addrs_to_csv(addrs, geo_src, f_name, refresh = True):
    dicts = m_geo(addrs, geo_src.geo)
    creater = geo_src.create_dict
    file_tool.save_csv(m_create_dict(dicts, creater), f_name, columns, refresh)

if __name__ == '__main__':
    m_addrs_to_csv([addr, addr2], ip138, 'ip138.csv', True)