import requests

# Making a get request
response = requests.get('http://google.com/')

# print response
print(response)

# print elapsed time
print(response.elapsed)
