import requests
import json
import file_tool

#init

conf_name = 'config.yaml'
conf_dict = file_tool.load_config(conf_name)[__name__]

#end init

# 返回单个ip的响应json数据
def geo(ip):
    url = conf_dict['url'] + '/ipv4/?ip=' + ip + '&datatype=jsonp&token=' + conf_dict['token']
    resp = requests.get(url)
    return resp.json()

# 生成统一格式字典
def create_dict(raw_dict):
    dict = {
        'ip' : raw_dict['ip'],
        'country' : raw_dict['data'][0],
        'province' : raw_dict['data'][1],
        'city' : raw_dict['data'][2],
    }
    return dict

if __name__ =='__main__':
    pass