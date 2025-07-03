import requests
import sys

# 🔐 Replace this with your actual Cloudflare API Token (must have Account-level permissions)
API_TOKEN = ""

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def block_ip_globally(ip):
    url = "https://api.cloudflare.com/client/v4/user/firewall/access_rules/rules"
    payload = {
        "mode": "block",
        "configuration": {
            "target": "ip",
            "value": ip
        },
        "notes": "Global block via API"
    }

    resp = requests.post(url, headers=HEADERS, json=payload)
    data = resp.json()

    if data.get("success"):
        print(f"✅ IP {ip} globally blocked across all zones.")
    else:
        print(f"❌ Failed to block IP globally: {data}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ban_ip_global.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]
    block_ip_globally(ip_address)

if __name__ == "__main__":
    main()
