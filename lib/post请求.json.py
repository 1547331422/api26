import requests
url="http://httpbin.org/post"

data='''{
     "name":"zhangsan",
     "age":"18"
     }   
'''
'{"name":"zhangsan","age","18"}'

r=requests.post(url=url,data=data)
print(r.text)