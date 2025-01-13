import requests

# Parameters to be sent with the request
params = {'userId': 1}

# Make a GET request to JSONPlaceholder API with the given parameters
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# Print the JSON response from the API
print(response.json())

# Print the headers of the request (after fixing the typo)
print('Request Headers:')
for header, value in response.request.headers.items():
    print(header, '-->', value)

# Print the headers of the response
print('Response Headers:')
for header, value in response.headers.items():
    print(header, '-->', value)

# Send a POST request to httpbin with sample data
post_response = requests.post('https://httpbin.org/post', data={'key': 'value'})

# Send a PUT request to httpbin with sample data
put_response = requests.put('https://httpbin.org/put', data={'key': 'value'})
