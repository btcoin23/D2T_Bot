import re
import requests
import json
import os

def detect_solana_token_address(message):
    # Check if message contains dexscreener URL
    dexscreener_pattern = r'dexscreener\.com/solana/([1-9A-HJ-NP-Za-km-z]{32,44})'
    dex_match = re.search(dexscreener_pattern, message)
    
    if dex_match:
        contract_address = dex_match.group(1)
        # Call dexscreener API
        api_url = f"https://api.dexscreener.com/latest/dex/pairs/solana/{contract_address}"
        try:
            response = requests.get(api_url)
            data = response.json()
            if data.get("pairs") and len(data["pairs"]) > 0:
                return [data["pairs"][0]["baseToken"]["address"]]
        except Exception as e:
            print(f"Error fetching dexscreener API: {e}")
            return [contract_address]  # Fallback to original address if API fails
    
    # Original Solana address detection for non-dexscreener URLs
    pattern = r'[1-9A-HJ-NP-Za-km-z]{32,44}'
    matches = re.findall(pattern, message)
    return [match for match in matches if len(match) >= 32 and len(match) <= 44]



# At the start of your script, load or create the JSON file
TRACKED_ADDRESSES_FILE = 'tracked_addresses.json'

def load_tracked_addresses():
    if os.path.exists(TRACKED_ADDRESSES_FILE):
        with open(TRACKED_ADDRESSES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_address(address):
    addresses = load_tracked_addresses()
    addresses.append(address)
    with open(TRACKED_ADDRESSES_FILE, 'w') as f:
        json.dump(addresses, f)

