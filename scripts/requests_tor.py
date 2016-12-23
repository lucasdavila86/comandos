"""
pip freeze
PySocks==1.6.5
requests==2.12.4
win-inet-pton==1.0.1

pip install requests[socks]
pip install win-inet-pton

"""

import requests

resp = requests.get('https://httpbin.org/ip', proxies=dict(http='socks5://localhost:9150', https='socks5://localhost:9150'))
print 'ip: {}'.format(resp.text.strip())
