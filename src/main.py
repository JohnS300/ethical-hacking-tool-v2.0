from directory_bruteforce import brute_force_directories
from network_scan import scan_network
from login_bruteforce import brute_force_login
from scraper import scrape_website
from sql_injection_scanner import scan_for_sql_injection

def main():
    while True:
        print("\nChoose a tool to execute: ")
        print("1. [+] Directory Brute Force")
        print("2. [+] Network Scan")
        print("3. [+] Brute Force Login")
        print("4. [+] Website Scraper")
        print("5. [+] SQL Injection Scanner")
        print("0. [+] Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            url = input("[+] Enter the URL of the target website: ")
            brute_force_directories(url)
        elif choice == '2':
            network_range = input("[+] Enter the network range (e.g., 192.168.1.0/24): ")
            scan_network(network_range)
        elif choice == '3':
            url = input("[+] Enter the URL of the login page: ")
            brute_force_login(url)
        elif choice == '4':
            url = input("[+] Enter the website URL to scrape: ")
            scrape_website(url)
        elif choice == '5':
            url = input("[+] Enter the target URL for SQL injection: ")
            scan_for_sql_injection(url)
        elif choice == '0':
            print("[+] Exiting...")
            break
        else:
            print("[+] Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
