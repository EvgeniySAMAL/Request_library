import requests

headers ={
    "User-Agent":"IT Overone"
}

# response=requests.get("https://httpbin.org/get", headers=headers,params={'a':'b'}) #get запрос
response=requests.post("https://httpbin.org/post",
                       headers=headers,
                       params={'a':'b'},
                       json={'username':'supersecret'})

# response.raise_for_status()
# print(response.json())
print(response.text)