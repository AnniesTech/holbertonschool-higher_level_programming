#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
if __name__ == '__main__':
    from requests import get
    from requests.auth import HTTPBasicAuth
    import sys
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = get("https://api.github.com/user", auth=auth)
    print(r.json().get('id'))
