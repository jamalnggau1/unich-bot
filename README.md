# 🤖 Bot Unich Mining – Multi Akun Auto Mining

Bot ini dibuat untuk membantu **hunter airdrop** menjalankan **mining otomatis setiap 24 jam** pada platform Unich dengan dukungan **multi akun**.

---

## ✨ Fitur Utama

- 🔥 **Multi Akun Support** → token dibaca dari `tokens.txt`  
- ✅ **Klaim task hanya dilakukan sekali saat pertama kali menjalankan bot**  
- ⏳ **Mining otomatis** semua akun setiap 24 jam  
- 🚫 **Tidak ada pengulangan task** (hanya mining yang diulang)  
- 📊 **Cek poin tiap akun** sebelum eksekusi  
- 🛡️ **Delay aman** untuk menghindari rate limit & banned  

---

## 📂 Struktur Folder

project-folder/  
├── tokens.txt   # daftar token akun (1 token per baris)  
├── main.py   # script utama bot  

---

## 🚀 Cara Menggunakan Bot

### 1. Install Python & Library
- Pastikan Python 3 sudah terinstall  
- Install library `requests`:

pip install requests

---

### 2. Siapkan File `tokens.txt`
Masukkan semua token akunmu ke dalam file `tokens.txt`, **1 token per baris**:

Bearer token_akun_1  
Bearer token_akun_2  
Bearer token_akun_3  

---

### 3. Jalankan Bot
Eksekusi bot dengan perintah:

python unich_auto.py

---

## ⚙️ Cara Kerja Bot

1. Bot membaca seluruh token dari `tokens.txt`.  
2. Saat pertama kali berjalan:  
   - Mengecek saldo poin (`mUn`) tiap akun  
   - Melakukan klaim semua task sekali  
   - Menjalankan mining pertama  
3. Setelah itu:  
   - Bot masuk ke loop harian untuk menjalankan mining otomatis setiap 24 jam  
4. **Task tidak akan diulang**; hanya mining yang berjalan otomatis.  

---

## ✅ Kesimpulan

- 🔄 Task diklaim **sekali di awal**  
- ⏳ Mining berjalan otomatis setiap hari  
- 👥 Cocok untuk hunter airdrop dengan banyak akun  

---

## ⚠️ Disclaimer

- Script ini dibuat hanya untuk pembelajaran dan pengelolaan akun pribadi.  
- Penyalahgunaan bot dapat menyebabkan **ban permanen** dari layanan terkait.  
- Developer tidak bertanggung jawab atas kerugian yang terjadi akibat penggunaan bot ini.  

---

## ❤️ Dukungan

Jika bot ini membantu:  
- ⭐ Beri bintang pada repo GitHub  
- 🔁 Bagikan dengan komunitas hunter lainnya  
- 🛠️ Modifikasi dan kembangkan sesuai kebutuhanmu  
