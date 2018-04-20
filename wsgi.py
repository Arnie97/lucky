#!/usr/bin/env python3

import requests
from bottle import route, app, abort, HTTPResponse

URL = 'https://www.google.com.hk/search'


@route('/<keyword:path>')
def feeling_lucky(keyword):
    params = {'q': keyword, 'hl': 'zh-CN', 'btnI': ''}
    r = requests.get(URL, params, allow_redirects=False)
    if r.status_code == 302:
        return HTTPResponse(r.content, r.status_code, r.headers.items())
    else:
        abort(404, 'Not understood.')


if __name__ == '__main__':
    app().run(host='0.0.0.0', port=80, debug=True)
