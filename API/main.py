#doccumentation : API learning...
# real public api for testing purpose : https://jsonplaceholder.typicode.com/
# we will us erequest module to make api calls to the above public api

import requests
#get request to the above api
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code) # it will print the status code of the response
print(response.json())   # it will print the json response from the api

#post request to the above api
data = { 
    "title" : "foo",
    "body" : "bar",
    "user_ID" : 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data,timeout=5)

try:
  if response.status_code == 201:
    print("Post Request Succsessfull")
  else:
    raise Exception("API call failed with status code : {}".format(response.status_code))
except Exception as e:
 print("Error Occured : {}".format(e))

print(response.status_code)
print(response.json())



#documentation : handling timeouts in requests module
# what is timeout ? -> timeout is the maximum time to wait for a response from the server.
# if the server does not respond within the timeout period, a timeout exception is raised.
# how to handle timeouts in requests module ? -> we can handle timeouts in requests module by using the timeout parameter in the request method.
# the timeout parameter takes a float value that represents the number of seconds to wait for a response


