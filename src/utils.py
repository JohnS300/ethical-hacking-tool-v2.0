from datetime import datetime

def get_timestamped_filename(base_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.txt"

def load_wordlist(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Wordlist file '{filename}' not found.")
        return []
