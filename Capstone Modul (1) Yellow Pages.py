from tabulate import tabulate

dataYellowPages = {
    'Restoran': [
        {'ID': 111, 'Nama Perusahaan': 'Terrasa', 'Alamat': 'Palembang', 'Nomor Telepon': '082120221000'},
        {'ID': 112, 'Nama Perusahaan': 'Coventown', 'Alamat': 'Palembang', 'Nomor Telepon': '082150005000'}
    ],
    'Perhotelan': [
        {'ID': 221, 'Nama Perusahaan': 'Santika', 'Alamat': 'Jakarta Selatan', 'Nomor Telepon': '082120222000'},
        {'ID': 222, 'Nama Perusahaan': 'Aryaduta', 'Alamat': 'Palembang', 'Nomor Telepon': '082120232026'}
    ],
    'Elektronik': [
        {'ID': 331, 'Nama Perusahaan': 'Raja Sejuk', 'Alamat': 'Lampung', 'Nomor Telepon': '082120223000'}
    ]
}

def tampilkan_data():
    if not dataYellowPages:
        print('Data Tidak Tersedia')
    else:
        headers = ['ID', 'Kategori Bisnis', 'Nama Perusahaan', 'Alamat', 'Nomor Telepon']
        rows = []
        for kategori, perusahaan in dataYellowPages.items():
            for data in perusahaan:
                rows.append([data['ID'], kategori, data['Nama Perusahaan'], data['Alamat'], data['Nomor Telepon']])
        print(tabulate(rows, headers=headers, tablefmt='grid'))


def tambah_data():
    while True:
        kategori = input('Kategori Bisnis: ')
        namaPerusahaan = input('Nama Perusahaan: ')
        alamat = input('Alamat: ')
        nomorTelepon = input('Nomor Telepon: ')

        if not validasi_nomor_telepon(nomorTelepon):
            print('Nomor Telepon tidak valid. Harus berupa 12 digit angka.')
            continue

        if not kategori.replace(" ", "").isalpha():
            print('Kategori Bisnis tidak valid. Hanya boleh mengandung huruf dan spasi.')
            continue

        if not namaPerusahaan.replace(" ", "").isalpha():
            print('Nama Perusahaan tidak valid. Hanya boleh mengandung huruf dan spasi.')
            continue

        if not alamat.replace(" ", "").isalpha():
            print('Alamat tidak valid. Hanya boleh mengandung huruf dan spasi.')
            continue

        if kategori not in dataYellowPages:
            dataYellowPages[kategori] = []

        def data_sudah_ada(data_list, nama, alamat):
            for data in data_list:
                if data['Nama Perusahaan'] == nama and data['Alamat'] == alamat:
                    return True
            return False

        if data_sudah_ada(dataYellowPages[kategori], namaPerusahaan, alamat):
            print('Data dengan nama perusahaan dan alamat yang sama sudah ada.')
        else:
            if not dataYellowPages[kategori]:
                ID = 1
            else:
                max_id = max(data['ID'] for data in dataYellowPages[kategori])
                ID = max_id + 1

            dataYellowPages[kategori].append({'ID': ID, 'Nama Perusahaan': namaPerusahaan, 'Alamat': alamat, 'Nomor Telepon': nomorTelepon})
            print('Data berhasil ditambahkan.')

        while True:
            pilihan = input('Apakah Anda ingin menambahkan data lagi? (y/n): ').strip().lower()
            if pilihan == 'y':
                break
            elif pilihan == 'n':
                return
            else:
                print('Pilihan tidak valid. Masukkan "y" untuk ya atau "n" untuk tidak.')




def update_data():
    try:
        ID = int(input('Masukkan ID perusahaan yang ingin diupdate: '))
        if ID <= 0:
            print('ID perusahaan harus merupakan bilangan bulat positif.')
            return

        for kategori, perusahaan in dataYellowPages.items():
            for data in perusahaan:
                if data['ID'] == ID:
                    print('Pilih kolom yang ingin diupdate:')
                    print('1. Kategori Bisnis')
                    print('2. Nama Perusahaan')
                    print('3. Alamat')
                    print('4. Nomor Telepon')
                    kolom = int(input('Nomor kolom: '))
                    if 1 <= kolom <= 4:
                        new_value = input(f'Masukkan nilai baru untuk kolom {kolom}: ')

                        konfirmasi = input('Anda yakin ingin mengupdate data ini? (y/n): ').strip().lower()
                        if konfirmasi != 'y':
                            print('Batal mengupdate data.')
                            return

                        if kolom == 1:
                            kategori_lama = data['Kategori Bisnis']
                            if kategori_lama != new_value:
                                dataYellowPages[kategori_lama].remove(data)
                                if new_value not in dataYellowPages:
                                    dataYellowPages[new_value] = []
                                data['Kategori Bisnis'] = new_value
                            else:
                                print('Kategori tidak berubah.')
                        elif kolom == 2:
                            if data['Nama Perusahaan'] != new_value:
                                data['Nama Perusahaan'] = new_value
                                print('Nama Perusahaan berhasil diupdate.')
                            else:
                                print('Nama Perusahaan tidak berubah.')
                        elif kolom == 3:
                            if data['Alamat'] != new_value:
                                data['Alamat'] = new_value
                                print('Alamat berhasil diupdate.')
                            else:
                                print('Alamat tidak berubah.')
                        elif kolom == 4:
                            if data['Nomor Telepon'] != new_value:
                                data['Nomor Telepon'] = new_value
                                print('Nomor Telepon berhasil diupdate.')
                            else:
                                print('Nomor Telepon tidak berubah.')

                        print('Data berhasil diupdate.')
                        return
        print('ID perusahaan tidak ditemukan.')
    except ValueError:
        print('Masukkan ID perusahaan yang valid (bilangan bulat positif).')


def hapus_data():
    try:
        ID = int(input('Masukkan ID perusahaan yang ingin dihapus: '))
    except ValueError:
        print('ID perusahaan harus berupa bilangan bulat.')
        return
    

    for kategori, perusahaan in dataYellowPages.items():
        for data in perusahaan:
            if data['ID'] == ID:
                perusahaan.remove(data)
                print('Data berhasil dihapus.')
                return
    print('ID perusahaan tidak ditemukan.')


def hapus_semua_data_kategori():
    kategori_hapus = input('Masukkan kategori bisnis yang ingin dihapus beserta semua datanya: ')
    if kategori_hapus in dataYellowPages:
        konfirmasi = input(f'Anda yakin ingin menghapus semua data dalam kategori {kategori_hapus}? (y/n): ').strip().lower()
        if konfirmasi == 'y':
            dataYellowPages.pop(kategori_hapus, None)
            print(f'Semua data dalam kategori {kategori_hapus} telah dihapus.')
        else:
            print('Batal menghapus data.')
    else:
        print(f'Kategori {kategori_hapus} tidak ditemukan.')



def cari_data():
    print("Pilih metode pencarian:")
    print("1. Berdasarkan Nama Perusahaan")
    print("2. Berdasarkan Alamat")
    pilihanPencarian = input("Masukkan nomor metode pencarian (1/2): ").strip().lower()

    if pilihanPencarian not in ["1", "2"]:
        print("Pilihan pencarian tidak valid.")
        return
    

    keyword = input("Masukkan kata kunci pencarian: ").strip().lower()
    found = False
    print("Hasil Pencarian:\n")
    print("ID\t| Nama Perusahaan\t| Alamat\t\t| Nomor Telepon")

    
    for kategori, perusahaan in dataYellowPages.items():
        for data in perusahaan:
            nama_perusahaan_lower = data["Nama Perusahaan"].lower()
            alamat_lower = data["Alamat"].lower()

            if (pilihanPencarian == "1" and keyword in nama_perusahaan_lower) or (pilihanPencarian == "2" and keyword in alamat_lower):
                print(f'{data["ID"]}\t| {data["Nama Perusahaan"]}\t\t| {data["Alamat"]}\t\t| {data["Nomor Telepon"]}')
                found = True

    if not found:
        print("Data tidak ditemukan.")



def urutkan_data():
    print('Pilihan Pengurutan Data:')
    print('1. Berdasarkan ID (ascending)')
    print('2. Berdasarkan Nama Perusahaan (ascending)')
    print('3. Berdasarkan ID (descending)')
    print('4. Berdasarkan Nama Perusahaan (descending)')
    pilihanUrutan = input('Pilih metode pengurutan (1/2/3/4): ')

    if pilihanUrutan in ['1', '2', '3', '4']:
        ascending = True if pilihanUrutan in ['1', '2'] else False
        by_name = True if pilihanUrutan in ['2', '4'] else False

        for kategori, perusahaan in dataYellowPages.items():
            dataYellowPages[kategori] = sorted(perusahaan, key=lambda x: x['ID'] if not by_name else x['Nama Perusahaan'], reverse=not ascending)
        
        urutan = 'ID' if not by_name else 'Nama Perusahaan'
        urutan_str = 'ascending' if ascending else 'descending'
        
        print(f'Data berhasil diurutkan berdasarkan {urutan} ({urutan_str}).')
    else:
        print('Pilihan pengurutan tidak valid.')


def validasi_nomor_telepon(nomorTelepon):
    if not nomorTelepon.isdigit() or len(nomorTelepon) != 12:
        return False
    return True


def statistik_data():
    if not dataYellowPages:
        print('Data Tidak Tersedia')
        return

    total_perusahaan = 0
    kategori_perusahaan = {}

    for kategori, perusahaan in dataYellowPages.items():
        total_perusahaan += len(perusahaan)
        kategori_perusahaan[kategori] = len(perusahaan)

    print('\nStatistik Data:\n')
    print(f'Total Perusahaan: {total_perusahaan}')
    print('\nJumlah Perusahaan per Kategori Bisnis:')
    for kategori, jumlah in kategori_perusahaan.items():
        print(f'{kategori}: {jumlah}')
    print('\n')




password = "Admin01"

input_password = input("Masukkan kata sandi: ")
if input_password != password:
    print("Kata sandi salah. Akses ditolak.")
else:

    while True:
        print('''
        Selamat Datang di Yellow Pages
        Menu Utama Yellow Pages:
        1. Menampilkan Daftar Perusahaan
        2. Menambah Data Perusahaan
        3. Mengupdate Data Perusahaan
        4. Menghapus Data Perusahaan (Satu per Satu)
        5. Menghapus Semua Data dalam Kategori
        6. Cari Data Perusahaan
        7. Urutkan Data
        8. Statistik Data
        9. Keluar
        ''')


        pilihanMainMenu = input('Masukkan nomor menu yang ingin dijalankan: ')

        if pilihanMainMenu == '9':
            print('Anda telah keluar dari program.')
            break


        if pilihanMainMenu == '1':
            tampilkan_data()
        elif pilihanMainMenu == '2':
            tambah_data()
        elif pilihanMainMenu == '3':
            update_data()
        elif pilihanMainMenu == '4':
            hapus_data()
        elif pilihanMainMenu == '5':
            hapus_semua_data_kategori()
        elif pilihanMainMenu == '6':
            cari_data()
        elif pilihanMainMenu == '7':
            urutkan_data()
        elif pilihanMainMenu == '8':
            statistik_data()
        else:
            print('Pilihan yang Anda masukkan salah.')

