import os
import pandas as pd
from datetime import datetime
import time
from tabulate import tabulate

def buat_file():
    if not os.path.exists('daftar_komoditas.csv'):
        pd.DataFrame(columns=["Daftar Komoditas", "Harga Komoditas"]).to_csv('daftar_komoditas.csv', index=False)
    if not os.path.exists('data_pengguna.csv'):
        pd.DataFrame(columns=["Username", "Password"]).to_csv('data_pengguna.csv', index=False)
    if not os.path.exists('data_petani.csv'):
        pd.DataFrame(columns=["Username", "Tanggal", "Komoditas", "Biaya_Bahan", "Biaya_Tenaga_Kerja", "Biaya_Operasional", "Jumlah_Panen", "Keuntungan"]).to_csv('data_petani.csv', index=False)
    if not os.path.exists("log_aktivitas.csv"):
        pd.DataFrame(columns=["Username", "Waktu", "Aksi", "Detail"]).to_csv("log_aktivitas.csv", index=False)

buat_file()


def tampilanawal() :
    os.system('cls')
    print('''
    ═════════════════════๑ஓஓ๑♡๑ஓஓ๑════════════════════
             .---------------------------------.               
                   | | A G R O C A L C | |                             
           | |----------------------------------| | 
                  SELAMAT DATANG DI AGROCALC      
    
    ═════════════════════๑ஓஓ๑♡๑ஓஓ๑════════════════════

    Silahkan pilih menu register atau login
    1. LOGIN 
    2. REGISTER''')
    pilihan = input("Masukkan pilihan menu anda: ").lower()
    if pilihan == "1" or pilihan == "login" :
        login()
    elif pilihan == "2" or pilihan == 'register' :
        buat_akun()
    else :
        input('Pilihan tidak valid, tekan enter untuk melanjutkan')
    tampilanawal()

def buat_akun():
    os.system('cls')
    print('========== Hai! Ayo buat akun anda! ==========\n')
    pengguna = pd.read_csv('data_pengguna.csv')
    username = input('Masukkan username baru : ').strip()
    password = input('Masukkan password baru : ').strip()

    if username in pengguna['Username'].values:
        print('Username sudah ada! Gunakan username lain!')
        input('Enter untuk kembali')
        os.system('cls')
        buat_akun()

    baru = {
        'Username': username,
        'Password': password
    }
    pengguna = pd.concat([pengguna, pd.DataFrame([baru])], ignore_index=True)
    pengguna.to_csv('data_pengguna.csv', index=False)
    print('Akun berhasil dibuat!\n')
    input('Tekan enter untuk melanjutkan ke Log In ')
    os.system('cls')
    login()


def login():
    global Username
    os.system('cls')
    print('==================== LOGIN ====================')
    print('             Ayo masuk ke akun anda!           \n')
    akun = pd.read_csv('data_pengguna.csv')
    username = input('Masukkan username : ').strip()
    password = input('Masukkan password : ').strip()

    if username == 'admin' and password == '123':
        print('\n============ Selamat datang Admin! ============')
        menu_admin()
    else:
        if username in akun['Username'].values:
            password_benar = akun.loc[akun['Username'] == username, 'Password'].values[0]
            if password == password_benar:
                Username = username
                print('\n=========== Anda berhasil Log In! ===========')
                print(f'============ Selamat datang {username}! ============')
                input('\nTekan enter untuk melanjutkan')
                menu_petani()
            else:
                print('Password yang anda masukkan salah!')
                input('Tekan enter untuk kembali melakukan login')
                login()
        else:
            print('Username tidak ditemukan!')
            input('Enter untuk kembali melakukan Login')
            login()

def menu_admin():
    os.system('cls')
    print('══════════════════════════๑ஓஓ๑♡๑ஓஓ๑════════════════════════')
    print('||----------------------- MENU ADMIN ----------------------||')
    print('||                  1. Lihat Daftar Komoditas              ||')
    print('||                  2. Tambah Komoditas                    ||')
    print('||                  3. Hapus Komoditas                     ||')
    print('||                  4. Ubah Komoditas                      ||')
    print('||                  5. Lihat Daftar Pengguna               ||')
    print('||                  6. Keluar                              ||')
    print('══════════════════════════๑ஓஓ๑♡๑ஓஓ๑════════════════════════')
    pilihan = input("Masukkan pilihan anda: ").lower()
    if pilihan == '1' or pilihan == 'lihat daftar komoditas':
        lihat_daftar_komoditas()
    elif pilihan == '2' or pilihan == 'tambah komoditas':
        tambah_komoditas()
    elif pilihan == '3' or pilihan == 'hapus komoditas':
        hapus_komoditas()
    elif pilihan == '4' or pilihan == 'ubah daftar komoditas':
        ubah_komoditas()
    elif pilihan == '5' or pilihan == 'lihat daftar pengguna':
        daftar_pengguna()
    elif pilihan == '6' or pilihan == 'keluar':
        print("Keluar dari akun admin")
        input("Tekan enter untuk kembali ke menu utama")
        tampilanawal()
    else:
        print("Pilihan anda tidak valid")
        input("Tekan enter untuk kembali")
        menu_admin()

def lihat_daftar_komoditas():
    os.system('cls')
    daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
    
    if daftar_komoditas.empty:
        print("Belum ada komoditas yang tercatat.")
        input("Tekan enter untuk kembali")
        menu_admin()
    else:
        print('\n ======================= Daftar Komoditas =======================\n')
        print(tabulate(daftar_komoditas.values, headers=daftar_komoditas.columns, tablefmt="grid"))

    input("\nTekan enter untuk kembali")
    menu_admin()

def tambah_komoditas():
    os.system('cls')
    daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
    print('\n ======================= Daftar Komoditas =======================\n')
    print(tabulate(daftar_komoditas.values, headers=daftar_komoditas.columns, tablefmt="grid"))
    print("\n===================== TAMBAH KOMODITAS =====================\n")
    print("Masukkan data komoditas\n")
    nama_komoditas = input('Masukkan nama komoditas : ').capitalize()
    if nama_komoditas == '':
        menu_admin()
    else :
        try :
            harga = int(input('Masukkan harga komoditas/kg : '))
            daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
            daftar_komoditas = pd.concat([daftar_komoditas, pd.DataFrame([{'Daftar Komoditas': nama_komoditas, 'Harga Komoditas': harga}])], ignore_index=True)
            daftar_komoditas.to_csv('daftar_komoditas.csv', index=False)
            print('Daftar komoditas berhasil ditambahkan!')
            
        except ValueError:
            print("Harga harus berupa angka")
            input("Tekan enter untuk mengulang")
            tambah_komoditas()

    lagi = input(
        'Apakah anda ingin menambahkan daftar komoditas lagi? Tekan enter jika tidak').lower()
    if lagi == 'ya' or lagi == 'iya' or lagi =='y':
        tambah_komoditas()
    else:
        menu_admin()
        
def hapus_komoditas():
    daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
    
    if daftar_komoditas.empty:
        print("Belum ada komoditas yang tercatat.")
        input("Tekan enter untuk kembali")
        menu_admin()
    else:
        print('\n ======================= Daftar Komoditas =======================\n')
        print(tabulate(daftar_komoditas.values, headers=daftar_komoditas.columns, tablefmt="grid"))

    print("\n===================== HAPUS KOMODITAS =====================\n")
    nama_komoditas = input("Masukkan nama komoditas yang ingin dihapus: ").capitalize()
    if nama_komoditas == '':
        menu_admin()
    else : 
        daftar_komoditas = pd.read_csv('daftar_komoditas.csv') 
        daftar_komoditas = daftar_komoditas[daftar_komoditas['Daftar Komoditas'] != nama_komoditas] 
        daftar_komoditas.to_csv('daftar_komoditas.csv', index=False) 
        print(f'Komoditas {nama_komoditas} berhasil dihapus!')

    lagi = input(
        'Apakah anda ingin menghapus daftar komoditas lagi? Tekan enter jika tidak').lower()
    if lagi == 'ya' or lagi == 'iya' or lagi =='y':
        hapus_komoditas()
    else:
        menu_admin()

def ubah_komoditas():
    daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
    
    if daftar_komoditas.empty:
        print("Belum ada komoditas yang tercatat.")
        input("Tekan enter untuk kembali")
        menu_admin()
    else:
        print('\n======================= Daftar Komoditas =======================\n')
        print(tabulate(daftar_komoditas.values, headers=daftar_komoditas.columns, tablefmt="grid"))

    print("===================== UBAH KOMODITAS =====================\n")
    nama_komoditas = input("Masukkan nama komoditas yang ingin diubah: ").capitalize()
    
    if nama_komoditas == '':
        menu_admin()
    else : 
        try :
            harga = int(input("Masukkan harga baru: "))
            daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
            daftar_komoditas.loc[daftar_komoditas['Daftar Komoditas'] == nama_komoditas, ['Daftar Komoditas', 'Harga Komoditas']] = [nama_komoditas, harga]
            daftar_komoditas.to_csv('daftar_komoditas.csv', index=False) 
            print('Daftar komoditas berhasil diubah!')

        except ValueError:
            print("Harga harus berupa angka")
            input("Tekan enter untuk mengulang")
            ubah_komoditas()

    lagi = input(
        'Apakah anda ingin mengubah daftar komoditas lagi? Tekan enter jika tidak').lower()
    if lagi == 'ya' or lagi == 'iya' or lagi =='y':
        tambah_komoditas()
    else:
        menu_admin()

def daftar_pengguna():
    os.system('cls')
    daftar_pengguna = pd.read_csv('data_pengguna.csv')
    
    if daftar_pengguna.empty:
        print("Belum ada daftar pengguna.")
        input("\nTekan enter untuk kembali ke menu admin...")
        menu_admin()
    else:
        if 'Password' in daftar_pengguna.columns:
            daftar_pengguna = daftar_pengguna.drop(columns=['Password'])
        print(
            '\n================= Daftar Pengguna =================\n'
        )
        print(tabulate(daftar_pengguna.values, headers=daftar_pengguna.columns, tablefmt="grid"))

    input("\nTekan enter untuk kembali")
    menu_admin()

data_sesi = {}

def menu_petani():
    os.system('cls')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ══════════════════════════')
    print('||---------------------- MENU PETANI ----------------------||')
    print('||                   1. Jenis Komoditas                    ||')
    print('||                   2. Biaya Bahan Produksi               ||')
    print('||                   3. Biaya Tenaga Kerja                 ||')
    print('||                   4. Biaya Operasional                  ||')
    print('||                   5. Update Biaya                       ||')
    print('||                   6. Jumlah Panen                       ||')
    print('||                   7. Prediksi Keuntungan                ||')
    print('||                   8. Riwayat Penggunaan                 ||')
    print('||                   9. Keluar                             ||')
    print('══════════════════════════๑ஓஓ๑♡๑ஓ๑ஓ══════════════════════════')
    pilihan = input("Masukkan pilihan anda: ").lower()
    if pilihan == '1' or pilihan == 'jenis komoditas':
        input_komoditas()
    elif pilihan == '2' or pilihan == 'biaya bahan produksi':
        biaya_bahan()
    elif pilihan == '3' or pilihan == 'biaya tenaga kerja':
        biaya_tenaga_kerja()
    elif pilihan == '4' or pilihan == 'biaya operasional':
        biaya_operasional()
    elif pilihan == '5' or pilihan == 'update biaya':
        update_biaya()
    elif pilihan == '6' or pilihan == 'jumlah panen':
        jumlah_panen()
    elif pilihan == '7' or pilihan == 'prediksi keuntungan':
        prediksi_keuntungan()
    elif pilihan == '8' or pilihan == 'riwayat penggunaan':
        riwayat()
    elif pilihan == '9' or pilihan == 'keluar':
        keluar()
    else:
        print("Pilihan tidak valid")
        input("Tekan enter untuk kembali")
        menu_petani()

def log_aktivitas(username, aksi, detail):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = pd.DataFrame([{
        "Username": username,
        "Waktu": waktu,
        "Aksi": aksi,
        "Detail": detail
    }])

    if not os.path.exists("log_aktivitas.csv"):
        log.to_csv("log_aktivitas.csv", index=False)
    else:
        lama = pd.read_csv("log_aktivitas.csv")
        gabung = pd.concat([lama, log], ignore_index=True)
        gabung.to_csv("log_aktivitas.csv", index=False)


def input_komoditas():
    os.system('cls')
    daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
    if daftar_komoditas.empty:
        print("Belum ada komoditas tersedia.")
        input("Tekan enter untuk kembali")
        menu_petani()
    else:
        print("Daftar Komoditas:")
        for i, row in daftar_komoditas.iterrows():
            print(f"{i+1}. {row['Daftar Komoditas']} - Rp{row['Harga Komoditas']}/kg")
        print("\nKetik 0 jika ingin kembali ke menu utama petani.")
        try:
            pilihan = int(input("Pilih nomor komoditas: ")) - 1
            if pilihan == -1:
                menu_petani()
            elif 0 <= pilihan < len(daftar_komoditas):
                komoditas = daftar_komoditas.iloc[pilihan]['Daftar Komoditas']
                data_sesi['komoditas'] = komoditas
                print(f"Komoditas dipilih: {komoditas}")
                input("Tekan enter untuk kembali")
                menu_petani()
            else:
                print("Pilihan tidak valid")
                input("Tekan enter")
                input_komoditas()
        except ValueError:
            print("Input harus berupa angka")
            input("Tekan enter")
            input_komoditas()

def biaya_bahan():
    os.system('cls')
    print("Input Biaya Bahan Produksi")
    print("Ketik '0' pada input pertama untuk kembali ke menu utama.")
    try:
        bibit_input = input("Biaya Bibit: ")
        if bibit_input == '0':
            menu_petani()
        bibit = float(bibit_input)
        pupuk = float(input("Biaya Pupuk: "))
        pestisida = float(input("Biaya Pestisida: "))
        irigasi = float(input("Biaya Irigasi: "))
        total_bahan = bibit + pupuk + pestisida + irigasi
        
        data_sesi['biaya_bahan'] = total_bahan
        print(f"Total Biaya Bahan: {total_bahan}")

        log_aktivitas(Username, "Input Biaya Bahan", f"Total: {total_bahan}")

        input("Tekan enter untuk kembali")
        menu_petani()
    except ValueError:
        print("Input harus berupa angka")
        input("Tekan enter")
        biaya_bahan()

def biaya_tenaga_kerja():
    os.system('cls')
    print("Input Biaya Tenaga Kerja")
    print("Ketik '0' pada input pertama untuk kembali ke menu utama.")
    try:
        jumlah_tk_input = input("Jumlah Tenaga Kerja: ")
        if jumlah_tk_input == '0':
            menu_petani()
        jumlah_tk = int(jumlah_tk_input)
        upah_hari = float(input("Upah per Hari: "))
        jumlah_hari = int(input("Jumlah Hari Bekerja: "))
        total_tk = jumlah_tk * upah_hari * jumlah_hari
        
        data_sesi['biaya_tenaga_kerja'] = total_tk
        print(f"Total Biaya Tenaga Kerja: {total_tk}")

        log_aktivitas(Username, "Input Biaya Tenaga Kerja", f"Total: {total_tk}")

        input("Tekan enter untuk kembali")
        menu_petani()
    except ValueError:
        print("Input harus berupa angka")
        input("Tekan enter")
        biaya_tenaga_kerja()

def biaya_operasional():
    os.system('cls')
    print("Input Biaya Operasional (Alat Bajak)")
    print("Ketik '0' untuk kembali ke menu utama.")
    biaya_op_input = input("Biaya Operasional: ")
    if biaya_op_input == '0':
        menu_petani()
    try:
        biaya_op = float(biaya_op_input)
        data_sesi['biaya_operasional'] = biaya_op
        print(f"Biaya Operasional: {biaya_op}")

        log_aktivitas(Username, "Input Biaya Operasional", f"Total: {biaya_op}")

        input("Tekan enter untuk kembali")
        menu_petani()
    except ValueError:
        print("Input harus berupa angka")
        input("Tekan enter")
        biaya_operasional()

def update_biaya():
    os.system('cls')
    print("Update Biaya")
    
    biaya_bahan_val = data_sesi.get('biaya_bahan', 0)
    biaya_tenaga_kerja_val = data_sesi.get('biaya_tenaga_kerja', 0)
    biaya_operasional_val = data_sesi.get('biaya_operasional', 0)

    print("\nBiaya saat ini:")
    print(f"1. Biaya Bahan Produksi: {biaya_bahan_val}")
    print(f"2. Biaya Tenaga Kerja: {biaya_tenaga_kerja_val}")
    print(f"3. Biaya Operasional: {biaya_operasional_val}")

    print("\nPilih biaya yang ingin diubah:")
    print("1. Biaya Bahan Produksi")
    print("2. Biaya Tenaga Kerja")
    print("3. Biaya Operasional")
    print("4. Kembali ke Menu Petani")
    
    pilihan = input("Pilih (1-4): ")

    if pilihan == '1':
        try:
            print(f"\nBiaya Bahan Produksi saat ini: {biaya_bahan_val}")
            nilai_baru = input("Masukkan Biaya Bahan Produksi yang baru (ketik 'batal' untuk kembali): ")
            if nilai_baru.lower() == 'batal':
                update_biaya()
            nilai_baru = float(nilai_baru)
            data_sesi['biaya_bahan'] = nilai_baru
            log_aktivitas(Username, "Update Biaya Bahan", f"Lama: {biaya_bahan_val}, Baru: {nilai_baru}")
            print(f"Biaya Bahan Produksi berhasil diubah menjadi: {nilai_baru}")
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan enter untuk kembali")
            update_biaya()
            return
    elif pilihan == '2':
        try:
            print(f"\nBiaya Tenaga Kerja saat ini: {biaya_tenaga_kerja_val}")
            nilai_baru = input("Masukkan Biaya Tenaga Kerja yang baru (ketik 'batal' untuk kembali): ")
            if nilai_baru.lower() == 'batal':
                update_biaya()
            nilai_baru = float(nilai_baru)
            data_sesi['biaya_tenaga_kerja'] = nilai_baru
            log_aktivitas(Username, "Update Biaya Tenaga Kerja", f"Lama: {biaya_tenaga_kerja_val}, Baru: {nilai_baru}")
            print(f"Biaya Tenaga Kerja berhasil diubah menjadi: {nilai_baru}")
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan enter untuk kembali")
            update_biaya()
            return
    elif pilihan == '3':
        try:
            print(f"\nBiaya Operasional saat ini: {biaya_operasional_val}")
            nilai_baru = input("Masukkan Biaya Operasional yang baru (ketik 'batal' untuk kembali): ")
            if nilai_baru.lower() == 'batal':
                update_biaya()
            nilai_baru = float(nilai_baru)
            data_sesi['biaya_operasional'] = nilai_baru
            log_aktivitas(Username, "Update Biaya Operasional", f"Lama: {biaya_operasional_val}, Baru: {nilai_baru}")
            print(f"Biaya Operasional berhasil diubah menjadi: {nilai_baru}")
        except ValueError:
            print("Input harus berupa angka.")
            input("Tekan enter untuk kembali")
            update_biaya()
            return
    elif pilihan == '4':
        menu_petani()
        return
    else:
        print("Pilihan tidak valid.")
        input("Tekan enter untuk mencoba lagi")
        update_biaya()
        return

    input("\nTekan enter untuk kembali ke menu update biaya")
    update_biaya()

def jumlah_panen():
    os.system('cls')
    print("Input Jumlah Panen (kg)")
    print("Ketik '0' untuk kembali ke menu utama.")
    panen_input = input("Jumlah Panen: ")
    if panen_input == '0':
        menu_petani()
    try:
        panen = float(panen_input)
        data_sesi['jumlah_panen'] = panen
        print(f"Jumlah Panen: {panen} kg")

        log_aktivitas(Username, "Input Jumlah Panen", f"{panen} kg")

        input("Tekan enter untuk kembali")
        menu_petani()
    except ValueError:
        print("Input harus berupa angka")
        input("Tekan enter")
        jumlah_panen()

def prediksi_keuntungan():
    os.system('cls')

    wajib = ['komoditas','biaya_bahan','biaya_tenaga_kerja','biaya_operasional','jumlah_panen']
    if any(w not in data_sesi for w in wajib):
        print("Data belum lengkap. Pastikan semua input telah dilakukan.")
        input("Tekan enter untuk kembali")
        menu_petani()
        return

    komoditas = data_sesi['komoditas']
    daftar_komoditas = pd.read_csv('daftar_komoditas.csv')
    harga = daftar_komoditas.loc[
        daftar_komoditas['Daftar Komoditas'] == komoditas,
        'Harga Komoditas'
    ].values[0]

    biaya_bahan_val = data_sesi['biaya_bahan']
    biaya_operasional_val = data_sesi['biaya_operasional']
    biaya_tenaga_kerja_val = data_sesi['biaya_tenaga_kerja']
    jumlah_panen_val = data_sesi['jumlah_panen']

    total_biaya = biaya_bahan_val + biaya_tenaga_kerja_val + biaya_operasional_val
    total_hasil_panen = jumlah_panen_val * harga
    prediksi = total_hasil_panen - total_biaya
    data_sesi['keuntungan'] = prediksi

    print("========== PREDIKSI KEUNTUNGAN ==========\n")
    print(f"1. Total biaya bahan : Rp{biaya_bahan_val:,.2f}")
    print(f"2. Biaya Operasional : Rp{biaya_operasional_val:,.2f}")
    print(f"3. Biaya tenaga kerja : Rp{biaya_tenaga_kerja_val:,.2f}")
    print(f"\nTotal biaya : Rp{total_biaya:,.2f}")
    print(f"Total hasil panen : Rp{total_hasil_panen:,.2f}")
    print(f"Prediksi Keuntungan : Rp{prediksi:,.2f}")

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    baru = {
        'Username': Username,
        'Tanggal': tanggal,
        'Komoditas': komoditas,
        'Biaya_Bahan': biaya_bahan_val,
        'Biaya_Tenaga_Kerja': biaya_tenaga_kerja_val,
        'Biaya_Operasional': biaya_operasional_val,
        'Jumlah_Panen': jumlah_panen_val,
        'Keuntungan': prediksi
    }

    data_petani = pd.read_csv('data_petani.csv')
    data_petani = pd.concat([data_petani, pd.DataFrame([baru])], ignore_index=True)
    data_petani.to_csv('data_petani.csv', index=False)

    log_aktivitas(Username, "Prediksi Keuntungan", f"Hasil: Rp{prediksi:,.2f}")

    print("\nData berhasil disimpan.")
    input("Tekan enter untuk kembali")
    menu_petani()

def riwayat():
    os.system('cls')
    data_petani = pd.read_csv('data_petani.csv')
    riwayat_user = data_petani[data_petani['Username'] == Username]

    if riwayat_user.empty:
        print("Belum ada riwayat.")
        input("Tekan enter untuk kembali")
        menu_petani()
        return

    print("========== RIWAYAT PENGGUNAAN ==========")
    print("1. Lihat semua riwayat")
    print("2. Cari berdasarkan Tanggal (contoh: 2025-11-25)")
    print("3. Cari berdasarkan Bulan (contoh: 2025-11)")
    print("4. Kembali ke menu utama")
    
    pilihan = input("\nPilih opsi (1-4): ").strip()

    if pilihan == '1':
        tampilkan_riwayat(riwayat_user)
    elif pilihan == '2':
        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(tanggal, "%Y-%m-%d")  # validasi format
            riwayat_filtered = riwayat_user[riwayat_user['Tanggal'].str.startswith(tanggal)]
            if riwayat_filtered.empty:
                print(f"Tidak ada riwayat pada tanggal {tanggal}.")
            else:
                tampilkan_riwayat(riwayat_filtered)
        except ValueError:
            print("Format tanggal salah! Gunakan format YYYY-MM-DD.")
            input("Tekan enter untuk kembali")
            riwayat()
            return
    elif pilihan == '3':
        bulan = input("Masukkan bulan (YYYY-MM): ").strip()
        try:
            datetime.strptime(bulan, "%Y-%m")  # validasi format
            riwayat_filtered = riwayat_user[riwayat_user['Tanggal'].str.startswith(bulan)]
            if riwayat_filtered.empty:
                print(f"Tidak ada riwayat pada bulan {bulan}.")
            else:
                tampilkan_riwayat(riwayat_filtered)
        except ValueError:
            print("Format bulan salah! Gunakan format YYYY-MM.")
            input("Tekan enter untuk kembali")
            riwayat()
            return
    elif pilihan == '4':
        menu_petani()
        return
    else:
        print("Pilihan tidak valid.")
        input("Tekan enter untuk kembali")
        riwayat()
        return

    log_aktivitas(Username, "Lihat Riwayat", "User membuka riwayat")
    input("Tekan enter untuk kembali ke menu utama")
    menu_petani()


def tampilkan_riwayat(df):
    # Ubah format angka agar lebih rapi (opsional)
    df_display = df.copy()
    for col in ['Biaya_Bahan', 'Biaya_Tenaga_Kerja', 'Biaya_Operasional', 'Keuntungan']:
        if col in df_display.columns:
            df_display[col] = df_display[col].apply(lambda x: f"Rp{x:,.2f}")
    df_display['Jumlah_Panen'] = df_display['Jumlah_Panen'].apply(lambda x: f"{x} kg")

    print("\n" + "="*80)
    print(df_display.to_string(index=False))
    print("="*80)

def keluar():
    print("Keluar dari akun petani")
    input("Tekan enter untuk kembali ke menu utama")
    tampilanawal()

tampilanawal()