import requests

# API documentation https://pastebin.com/doc_api#1

# POST Method

# API endpoint
URL = "https://pastebin.com/api/api_post.php"

# API key
API_KEY = "xxxxxxxxxxxxxxxxxxxxxx"

# code to be injected into test_server
test_code = '''
                this is some random text
            '''

# data to be sent to API
data = {
    'api_dev_key': API_KEY, 
    'api_option': 'paste', 
    'api_paste_code': test_code, 
    'api_paste_format': 'python'
}

# Make sure to send data as: 
# 1 - UTF-8 charset
# 2 - 'Content-Type': 'text/html'
r = requests.post(url=URL, data=data )

print(r.status_code)
print(r.text)
