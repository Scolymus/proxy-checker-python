from proxy_checker import ProxyChecker

checker = ProxyChecker(verbose=False)
print(f"my IP {checker.ip}")
proxy = '3.98.231.179:3128'
ip = proxy.split(':')[0]
print(f"proxy IP {ip}")
result = checker.check_proxy(proxy, True)
print(result)
print(f"is proxy ip same {checker.ip == ip}")
