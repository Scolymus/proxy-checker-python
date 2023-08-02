import proxy_checkers

p = proxy_checkers.ProxyChecker(timeout=10000, verbose=True)

print(p.check_proxy("64.235.204.107:3128", check_all_protocols=True, tls=1.3, protocol=['https']))