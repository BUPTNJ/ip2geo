from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkgeoip.request.v20200101.DescribeIpv4LocationRequest import DescribeIpv4LocationRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

request = DescribeIpv4LocationRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))


import common

#init

conf_name = 'config.yaml'
conf_dict = common.load_config(conf_name)[__name__]

#end init


# 返回单个ip的响应json数据
def geo(ip):
    pass


# 生成统一格式字典
def create_dict(raw_dict):
    pass
    
if __name__ =='__main__':
    pass