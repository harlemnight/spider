# import urllib.parse
# import urllib.request
# import urllib.error
# import socket
#
# try:
#     response = urllib.request.urlopen('https://www.python.org',timeout=60)
#     print(response.status)
#     print(response.getheaders())
#     print(response.getheader('Server'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('time out')
#
#
#
# data = bytes(urllib.parse.urlencode({'word ':'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

import requests
#
# data = {
# 'name': 'germey',
# 'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
# print(r.json())
# print(type(r.json()))

# r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)

def exm():
    #return None
    return 0

if __name__ == '__main__':
    rs = exm()
    print(type(rs))
    #print(len(rs))
    if rs:
        print('yes')
    else:
        print('no')
