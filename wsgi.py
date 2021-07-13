#!/usr/bin/env python3

import requests
from bottle import route, app, abort, redirect
from urllib.parse import urlparse, parse_qs

URL = 'https://www.google.com.hk/search'


@route('/robots.txt')
def robots():
    return 'User-Agent: *\nDisallow: /\n'


@route(r'/<:re:favicon\.ico|.+\.php(/.*)?>')
def block():
    abort(403, "Demonstrate you're not a robot.")


@route('/<keyword:path>')
def feeling_lucky(keyword):
    params = {'q': keyword, 'hl': 'zh-CN', 'btnI': ''}
    r = requests.get(URL, params, allow_redirects=False)
    if r.is_redirect:
        query = urlparse(r.headers['Location'])[4]
        target_url = parse_qs(query).get('q', [''])[0]
        redirect(target_url)
    else:
        abort(404, 'Not understood.')


if __name__ == '__main__':
    app().run(host='0.0.0.0', port=80, debug=True)
