Quillbot Login Checker
Program ini adalah sebuah script sederhana yang digunakan untuk melakukan cek login pada website Quillbot dengan menggunakan daftar akun yang diberikan melalui file accounts.txt. Selain itu, program ini juga memeriksa apakah akun yang berhasil login adalah akun premium atau bukan.

Persyaratan
Python 3.x
Library requests
Library BeautifulSoup
Anda dapat menginstal library yang dibutuhkan dengan menggunakan pip:

bash
Copy code
pip install requests beautifulsoup4
Cara Penggunaan
Pastikan Anda memiliki file accounts.txt yang berisi daftar akun dengan format (username:password), seperti contoh di bawah ini:
scss
Copy code
johnnybravo@sika3.com:2na34la1
alice@example.com:password123
bob@example.com:securepass
Jalankan program dengan menjalankan script quillbot.py:
bash
Copy code
python quillbot.py
Program akan membaca setiap baris di file accounts.txt, mencoba login dengan username dan password yang sesuai, dan kemudian mencetak apakah login berhasil atau gagal. Selain itu, program juga akan memeriksa apakah akun yang berhasil login adalah akun premium atau bukan.

Hasil Output
Program akan menampilkan output dengan format yang rapi, termasuk angka dan simbol untuk menandai setiap langkah prosesnya. Selain itu, program juga akan mencetak summary hasil setelah semua akun diperiksa dengan informasi berikut:

Jumlah Akun: Total jumlah akun yang diperiksa
Tidak Premium: Jumlah akun yang berhasil login namun bukan akun premium
Premium: Jumlah akun premium yang berhasil login
Salah Format: Jumlah akun dengan format yang salah pada file accounts.txt
Catatan
Harap gunakan kode ini hanya untuk tujuan edukasi dan pastikan Anda memiliki izin untuk melakukan tes keamanan atau otomatisasi login pada website tertentu.
Jangan melakukan tindakan yang melanggar hukum atau kebijakan privasi.
Anda dapat menyalin teks di atas dan menyimpannya sebagai README.md di direktori proyek Anda. Pastikan untuk mengganti bagian "Persyaratan" dan "Cara Penggunaan" sesuai dengan kebutuhan dan struktur proyek Anda.
