import requests
import json
import random
import urllib3
import base64

# Sertifikat xəbərdarlıqlarını tamamilə gizlət
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Sizin Dəqiq və Doğrudan API Ünvanınız
API_URL = "https://pantheonsite.io"
WP_USER = "admin"
WP_APP_PASS = "JDZl seRQ fHjN W3yl QRB2 gl4t"

# Botun yazacağı ingiliscə sınaq məqalələri
SAMPLE_POSTS = [
    {
        "title": "How to Fix QuickBooks Error Code H202 on Windows 11 Easily",
        "content": "<!-- wp:paragraph --><p>Are you facing QuickBooks Error H202 while switching to multi-user mode? Don't panic. This multi-user mode error usually occurs when QuickBooks cannot reach the server computer hosting the company file.</p><!-- /wp:paragraph --><!-- wp:heading --><h2>Step 1: Check Hosting Settings</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Open QuickBooks on your host computer, go to File > Utilities, and ensure 'Host Multi-User Access' is enabled.</p><!-- /wp:paragraph -->"
    },
    {
        "title": "Fix: Photoshop 2026 Random Crash on M3 Mac Devices During Export",
        "content": "<!-- wp:paragraph --><p>Many graphic designers are reporting that Photoshop 2026 unexpectedly crashes on M3 Max and M3 Pro Macs during the image export process. Here is the permanent solution.</p><!-- /wp:paragraph --><!-- wp:heading --><h2>Step 1: Disable GPU Acceleration Temporarily</h2><!-- /wp:heading --><!-- wp:paragraph --><p>Go to Preferences > Performance and uncheck Use Graphics Processor. Restart Photoshop and try exporting again.</p><!-- /wp:paragraph -->"
    }
]

def post_to_wordpress(title, content):
    # Giriş məlumatlarını Base64 formatına salırıq
    credential_string = f"{WP_USER}:{WP_APP_PASS}"
    credential_bytes = credential_string.encode('utf-8')
    base64_credentials = base64.b64encode(credential_bytes).decode('utf-8')
    
    payload = {
        "title": title,
        "content": content,
        "status": "publish"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64_credentials}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"Müraciət birbaşa bu ünvana göndərilir: {API_URL}")
    print("Məqalə ötürülür, zəhmət olmasa gözləyin...")
    
    try:
        response = requests.post(
            API_URL, 
            headers=headers, 
            data=json.dumps(payload), 
            timeout=30, 
            verify=False
        )
        
        if response.status_code == 201:
            print(f"\n[UĞURLU] Məqalə avtomatik olaraq sayta yükləndi: {title}")
            print("Yoxlamaq üçün saytınızın ana səhifəsini yeniləyin!")
        else:
            print(f"\nXəta kodu: {response.status_code}")
            print(f"Cavab: {response.text}")
            
    except Exception as e:
        print(f"\nBağlantı zamanı xəta yarandı: {e}")

if __name__ == "__main__":
    chosen_post = random.choice(SAMPLE_POSTS)
    post_to_wordpress(chosen_post["title"], chosen_post["content"])
