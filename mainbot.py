import requests
import json
import random
import urllib3
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Sizin Dəqiq və Doğrudan API Ünvanınız (Sərt şəkildə bərkidildi)
API_URL = "https://pantheonsite.io"
WP_USER = "admin"
WP_APP_PASS = "JDZl seRQ fHjN W3yl QRB2 gl4t"

SAMPLE_POSTS = [
    {
        "title": "How to Fix QuickBooks Error Code H202 on Windows 11 Easily",
        "content": "<!-- wp:paragraph --><p>Are you facing QuickBooks Error H202 while switching to multi-user mode? Don't panic. This error usually occurs when QuickBooks cannot reach the server computer.</p><!-- /wp:paragraph -->"
    },
    {
        "title": "Fix: Photoshop 2026 Random Crash on M3 Mac Devices During Export",
        "content": "<!-- wp:paragraph --><p>Many graphic designers are reporting that Photoshop 2026 unexpectedly crashes on M3 Max and M3 Pro Macs during export. Here is the solution.</p><!-- /wp:paragraph -->"
    }
]

def post_to_wordpress(title, content):
    credential_string = f"{WP_USER}:{WP_APP_PASS}"
    base64_credentials = base64.b64encode(credential_string.encode('utf-8')).decode('utf-8')
    
    payload = {"title": title, "content": content, "status": "publish"}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64_credentials}",
        "User-Agent": "Mozilla/5.0"
    }
    
    print(f"Müraciət birbaşa bu ünvana göndərilir: {API_URL}")
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload), timeout=30, verify=False)
        if response.status_code == 201:
            print(f"\n[UĞURLU] Məqalə avtomatik olaraq sayta yükləndi: {title}")
        else:
            print(f"\nXəta kodu: {response.status_code}\nCavab: {response.text}")
    except Exception as e:
        print(f"\nBağlantı zamanı xəta yarandı: {e}")

if __name__ == "__main__":
    chosen_post = random.choice(SAMPLE_POSTS)
    post_to_wordpress(chosen_post["title"], chosen_post["content"])
