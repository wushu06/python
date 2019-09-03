import requests
 
local_proxy = 'socks5://localhost:9050'
socks_proxy = {
    'http': local_proxy,
    'https': local_proxy
}
 
current_ip = requests.get(
    url='http://icanhazip.com/',
    proxies=socks_proxy,
    verify=False
)
