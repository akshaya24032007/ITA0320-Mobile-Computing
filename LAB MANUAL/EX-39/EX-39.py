import requests
API="https://jsonplaceholder.typicode.com/posts"
local_data={"title":"Mobile App Data","body":"Data synchronization test","userId":1}
try:
    response=requests.post(API,json=local_data,timeout=10)
    response.raise_for_status()
    server_data=response.json()
    print("Data sent successfully!")
    print("Server Response:",server_data)
    result=requests.get(API,params={"userId":1},timeout=10)
    result.raise_for_status()
    print("Data received successfully!")
    print(result.json()[:3])
except requests.RequestException as e:
    print("Synchronization failed:",e)
