import requests
import threading
from utils import load_wordlist, get_timestamped_filename

def brute_force_directories(url, wordlist_file="../resources/common.txt"):
    directories = load_wordlist(wordlist_file)
    output_file = get_timestamped_filename("../results/directory_bruteforce_results")
    found_directories = []

    def request_directory(directory):
        target_url = f"{url}/{directory}"
        try:
            response = requests.get(target_url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found directory: {target_url}")
                found_directories.append(target_url)
            elif response.status_code == 403:
                print(f"[+] Access forbidden: {target_url}")
        except requests.RequestException:
            print(f"[!] Error connecting to {target_url}")

    threads = [threading.Thread(target=request_directory, args=(directory,)) for directory in directories]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    with open(output_file, "w") as file:
        for directory in found_directories:
            file.write(directory + "\n")

    print(f"\n[+] Directory brute-force complete. Results saved to {output_file}")
