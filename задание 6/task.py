import random

def generate_log(filename, n=10000):
    methods = ["GET", "POST", "PUT", "DELETE"]
    urls = ["/index.html", "/login", "/api/users", "/admin", "/home"]
    codes = [200, 201, 404, 403, 500, 401, 400]
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(n):
            if i % 50 == 0:
                f.write("битая строка без формата\n")
                continue
            ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
            method = random.choice(methods)
            url = random.choice(urls)
            code = random.choice(codes)
            f.write(f"2026-09-01 12:15:{i % 60:02d} {ip} {method} {url} {code}\n")

def analyze_log(filename):
    count = 0
    ips = {}
    methods = {}
    urls = {}
    errors = 0
    with open(filename, "r", encoding="utf-8") as f:
        for s in f:
            parts = s.split()
            if len(parts) != 6:
                continue
            date, time, ip, method, url, code = parts
            if not code.isdigit():
                continue
            count += 1
            if ip not in ips:
                ips[ip] = 0
            ips[ip] += 1
            if method not in methods:
                methods[method] = 0
            methods[method] += 1
            if url not in urls:
                urls[url] = 0
            urls[url] += 1
            if code[0] == "4":
                errors += 1
    if count == 0:
        print("В файле нет корректных строк")
        return
    active_ip = max(ips, key=ips.get)
    popular_url = max(urls, key=urls.get)
    print("Количество запросов:", count)
    print("Уникальных IP:", len(ips))
    print("Самый активный IP:", active_ip, ips[active_ip])
    print("Методы:", methods)
    print("Ошибки 4xx:", errors)
    print("Самый частый URL:", popular_url, urls[popular_url])

generate_log("access.log")
analyze_log("access.log")
