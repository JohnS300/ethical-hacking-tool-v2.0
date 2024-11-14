import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        print("[+] Links found on the page:")
        
        links = []
        for a_tag in soup.find_all('a', href=True):
            link_info = (a_tag.get_text().strip(), a_tag['href'])
            links.append(link_info)
            print(f"Title: {link_info[0]}, Link: {link_info[1]}")

        return links
    except requests.RequestException:
        print(f"[!] Failed to connect to {url}")
        return []
