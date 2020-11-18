import os
import urllib.request
import time
import json
# print(time.time())
urls = 'https://careers.tencent.com/tencentcareer/api/post/Query?&pageIndex=1&pageSize=10'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

# for i in range(610,615+2):
#     print(i)
response = urllib.request.urlopen(urls)
json_data = response.read().decode()
data = json.loads(json_data)
count = data['Data']['Count'] // 10
print(type(count))