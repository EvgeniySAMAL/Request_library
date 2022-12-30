import requests

# website = "https://jsonplaceholder.typicode.com/posts" # post запрос
#
# response = requests.post(website, data={
#     "userid":12,
#     "title":"my new posts",
#     "body":"body for my post IT OVERONE",
#     "photo":{"1.jpg","2.jpg"}
#
# })
# print(response.text)


# website = "https://jsonplaceholder.typicode.com/posts/2"   # put запрос
# print(requests.get(website).json())
# response = requests.put(website, data={
#     "id":2,
#     "userid":12,
#     "title":"this is old posts",
#     "photo":{"1.jpg","2.jpg"}
#
#  })
#
# print(response.json())


# website = "https://jsonplaceholder.typicode.com/posts/2"   # patch запрос
# print(requests.patch(website).json())
# response = requests.put(website, data={
#     "id":2,
#     "userid":12,
#     "title":"this is old posts",
#
#  })
#
# print(response.json())


website = "https://jsonplaceholder.typicode.com/posts/2"   # delete запрос
print(requests.get(website).json())
response = requests.delete(website, data={
    "id":2,
    "userid":12,
    "title":"this is old posts",
    "photo":{"1.jpg","2.jpg"}

 })

print(response.status_code)