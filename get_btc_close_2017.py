from __future__ import (absolute_import,division,print_function,unicode_literals)

try:
    # Python 2.0
    from urllib import  urlopen
except ImportError:
    # Python 3.0
    from urllib.request import urlopen
import json

json_url='xxx.com/btc_close_2017.json'
response=urlopen(json_url)
# 读取数据
req=response.read()
# 将数据写入文件
with open('btc_close_2017.json','wb') as f:
    f.write(req)
# 加载json格式
file_urllib=json.loads(req)
print(file_urllib)