import requests

# website = "https://jsonplaceholder.typicode.com/posts" # post запрос
#
# response = requests.post(website, data={               # post запрос
#     "userid":12,
#     "title":"my new posts",
#     "body":"body for my post IT OVERONE",
#     "photo":{"1.jpg","2.jpg"}
#
# })
# print(response.text)                                   # post запрос


website = "https://jsonplaceholder.typicode.com/posts/2"   # put запрос
print(requests.get(website).json())
response = requests.put(website, data={
    "id":2,
    "userid":12,
    "title":"this is old posts",
    "photo":{"1.jpg","2.jpg"}

 })

print(response.json())