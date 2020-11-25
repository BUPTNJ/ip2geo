import pandas as pd
import yaml

# 文件内容to字符串
def file_to_str(f_name):
    with open(f_name, 'r') as f:
        content = f.read()
    return content

# 读取yaml文件并保存到字典
def load_config(f_name):
    content = file_to_str(f_name)
    return yaml.load(content)

# 保存至csv
def save_csv(dicts, f_name, columns, refresh):
    df = pd.DataFrame(dicts,columns = columns)
    if refresh:
        df.to_csv(f_name)
    else :
        df.to_csv(f_name, mode = 'a', header=False)