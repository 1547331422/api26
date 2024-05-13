import requests

url="http://httpbin.org/post"

data={
    "name":"zhangsan",
    "age":"18"
}

# headers={
#     "content-type":"x-www-form-urlencoded"
# }
#默认传统表单
r = requests.post(url=url,data=data)

print(r.text)
