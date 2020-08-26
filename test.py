import requests

BASE = 'http://127.0.0.1:5000/'

# data = [{"likes": 42, "name": "DIY Arduino", "views": 343240},
#         {"likes": 170, "name": "RPi Intro", "views": 413130},
#         {"likes": 74, "name": "REST APIs", "views": 146230}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())
#
# input()
response = requests.delete(BASE + "video/1")
print(response)
input()

# response = requests.get(BASE + "video/2")
# print(response.json())
#
response = requests.patch(BASE + "video/1", {"name": "Raspberry Pi Tutorial", "likes": 159, "views": 10239})
print(response.json())

