import requests
import time

url_base = "https://api.unich.com"

# ✅ Baca token dari file tokens.txt
with open("tokens.txt") as f:
    TOKENS = [line.strip() for line in f if line.strip()]

# ✅ Fungsi cek info akun
def my_info(headers):
    url = f"{url_base}/airdrop/user/v1/mining/recent"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        print(f"💎 Points: {data['data']['mUn']}")
    else:
        print(f"❌ Error: {r.status_code} - {r.text}")

# ✅ Fungsi klaim task
def claim_task(headers, task_id, evidence):
    url = f"{url_base}/airdrop/user/v1/social/claim/{task_id}"
    payload = {"evidence": evidence}
    r = requests.post(url, headers=headers, json=payload)
    data = r.json()
    if r.status_code == 200 or r.status_code == 201:
        print(f"✅ Task {task_id} completed successfully!")
    else:
        print(f"⚠️ Task {task_id} failed: {data.get('message')}")

# ✅ Fungsi mining
def mining(headers):
    url = f"{url_base}/airdrop/user/v1/mining/start"
    r = requests.post(url, headers=headers)
    if r.status_code in (200, 201):
        print("🚀 Mining started successfully!")
    else:
        try:
            msg = r.json().get("message")
        except:
            msg = r.text
        print(f"❌ Mining failed: {msg}")

# ✅ Fungsi ulang: hanya mining semua akun setiap 24 jam
def ulang():
    while True:
        print("\n⏳ Cek mining semua akun...")
        for token in TOKENS:
            headers = {
                "Authorization": token,
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            print(f"\n🔑 Mining akun: {token[:30]}...")
            mining(headers)
            time.sleep(1)  # jeda aman antar akun
        print("✅ Semua akun selesai mining. Tunggu 24 jam...")
        time.sleep(60 * 60 * 24)  # tunggu 24 jam

# ✅ Daftar Task ID
TASK_IDS = [
    "66c7054a50155435d01c4b80",
    "66e2725db598145b78c4e6b0",
    "666c70ad450155435d01c4bd8",
    "674fd08ef10a765092881c90",
    "686fa0acad6220f27eafd90b",
    "6879bb24ad6220f27eaff279",
    "6885b002f78a74e8ac5e946e",
    "68887d46f78a74e8ac5e9d2f",
    "6888381ff78a74e8ac5e9b6b",
    "66c705cd50155435d01c4ba5",
    "66d13fc9bcdb0182deb370b5",
    "66c7096250155435d01c4bcd",
    "66c7094950155435d01c4bc3",
    "66c705e450155435d01c4bab"
]

if __name__ == "__main__":
    evidence = "https://x.com/unich_com/status/1941450264764088565"

    # ✅ Pertama kali: jalankan task untuk semua akun
    for token in TOKENS:
        print("\n" + "=" * 50)
        print(f"🔑 LOGIN AKUN: {token[:30]}...")

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        my_info(headers)

        for task_id in TASK_IDS:
            claim_task(headers, task_id, evidence)
            time.sleep(1)  # jeda aman

        # Mining pertama kali
        mining(headers)

    print("\n✅ Semua akun selesai klaim task dan mining pertama kali!")

    # ✅ Mulai loop harian hanya untuk mining
    ulang()
