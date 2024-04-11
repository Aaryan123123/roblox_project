import requests

# Replace these placeholders with your actual values
user = "1550072143"
api_key = "xGMJmeHg9EeE9raZ6u01e5Zo1Fd4pFz4fp9mI3sZcl+akGTU"

# Construct the URL with placeholders replaced
url = f"https://apis.roblox.com/cloud/v2/users/{user}:generateThumbnail"

# Add the API key to the headers
headers = {
    "x-api-key": api_key
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check the response status
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
