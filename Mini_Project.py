# Sistem Pendataan Barang Yang Hilang

# Penyimpanan data menggunakan list untuk menyimpan data barang yang hilang
data_barang = [
    ["B001", "Dompet hitam", "Kantin", "Belum ditemukan"],
    ["B002", "Kunci motor", "Parkiran", "Belum ditemukan"],
]

# Fungsi Menampilkan Data

def tampilkan_data():
    print("\n=========== DAFTAR BARANG YANG HILANG ===========")

    if len(data_barang) == 0:
        print("Belum ada data barang.")
    else:
        for i, barang in enumerate(data_barang, start=1):
            print(f"\nData ke-{i}:")
            print(f"ID barang : {barang[0]}")
            print(f"Nama barang : {barang[1]}")
            print(f"Lokasi : {barang[2]}")
            print(f"Status : {barang[3]}")

# Program utama

while True:

    print("\n====================================")
    print("=== Sistem Pendataan Barang Yang Hilang ===")
    print("====================================")
    print("1. Tambah Data Barang")
    print("2. Tampilkan Data Barang")
    print("3. Ubah Data Barang")
    print("4. Hapus Data Barang")
    print("5. Keluar")
    print("====================================")

    pilihan = input("Masukkan pilihan (1-5): ")

    # Menu 1 - Tambah Data Barang

    if pilihan == "1":

        print("\n=== Tambah Data Barang ===")

        while True:
            id_barang = input("Masukkan ID barang: ").strip().upper()

            if id_barang == "":
                print("ID barang tidak boleh kosong !")
                continue

            # Cek apakah ID barang sudah ada
            id_tersedia = True

            for barang in data_barang:
                if barang[0] == id_barang:
                    id_tersedia = False
                    break
            if not id_tersedia:
                print("ID barang sudah ada, silakan masukkan ID lain.")
                continue

            break

        while True:
            nama = input("Masukkan nama barang: ").strip()

            if nama == "":
                print("Nama barang tidak boleh kosong !")
                continue

            break

        while True:
            lokasi = input("Masukkan Lokasi barang terakhir: ").strip()    

            if lokasi == "":
                print("Lokasi barang tidak boleh kosong !")
                continue

            break

        while True:
            print("\nPilih status barang:")
            print("1. Belum ditemukan")
            print("2. Ditemukan")

            status_pilihan = input("Pilih status (1/2): ")

            if status_pilihan == "1":
                status = "Belum ditemukan"
                break

            elif status_pilihan == "2":
                status = "Ditemukan"
                break

            else:
                print("Pilihan tidak valid! masukan 1 atau 2.")

        #Menambahkan data ke list
        data_barang.append([id_barang,nama,lokasi,status])       

        print("\nData berhasil ditambahkan!")
        print(f"ID barang   : {id_barang}")
        print(f"Nama barang : {nama}")
        print(f"Lokasi      : {lokasi}")
        print(f"Status      : {status}")

    # Menu 2 - Tampilkan data

    elif pilihan == "2":
        tampilkan_data()


        # Menu 3 - Ubah Data
    elif pilihan == "3":

        print("\n--- UBAH DATA BARANG ---")

        if len(data_barang) == 0:
            print("Belum ada data barang yang dapat diubah.")

        else:
            while True:
                id_cari = input(
                    "Masukkan ID barang yang ingin diubah: "
                ).strip().upper()

                if id_cari == "":
                    print("ID tidak boleh kosong!")
                    continue

                index_ditemukan = -1

                # Mencari ID barang
                for i in range(len(data_barang)):
                    if data_barang[i][0] == id_cari:
                        index_ditemukan = i
                        break

                if index_ditemukan == -1:
                    print("ID barang tidak ditemukan!")

                    ulang = input(
                        "Ingin mencari ID lagi? (y/n): "
                    ).strip().lower()

                    if ulang == "y":
                        continue
                    else:
                        print("Kembali ke menu utama.")
                        break

                # Menampilkan data lama
                print("\nData ditemukan!")
                print(f"Nama lama   : {data_barang[index_ditemukan][1]}")
                print(f"Lokasi lama : {data_barang[index_ditemukan][2]}")
                print(f"Status lama : {data_barang[index_ditemukan][3]}")

                # Input nama baru
                while True:
                    nama_baru = input("Masukkan nama baru: ").strip()

                    if nama_baru == "":
                        print("Nama tidak boleh kosong!")
                        continue

                    break

                # Input lokasi baru
                while True:
                    lokasi_baru = input("Masukkan lokasi baru: ").strip()

                    if lokasi_baru == "":
                        print("Lokasi tidak boleh kosong!")
                        continue

                    break

                # Input status baru
                while True:
                    print("\nPilih status baru:")
                    print("1. Belum ditemukan")
                    print("2. Ditemukan")

                    status_pilihan = input("Pilih status (1/2): ").strip()

                    if status_pilihan == "1":
                        status_baru = "Belum ditemukan"
                        break

                    elif status_pilihan == "2":
                        status_baru = "Ditemukan"
                        break

                    else:
                        print("Pilihan tidak valid! Masukkan 1 atau 2.")

                # Mengubah data
                data_barang[index_ditemukan][1] = nama_baru
                data_barang[index_ditemukan][2] = lokasi_baru
                data_barang[index_ditemukan][3] = status_baru

                print("\nData berhasil diubah!")
                print(f"ID barang   : {data_barang[index_ditemukan][0]}")
                print(f"Nama barang : {data_barang[index_ditemukan][1]}")
                print(f"Lokasi      : {data_barang[index_ditemukan][2]}")
                print(f"Status      : {data_barang[index_ditemukan][3]}")
                break

    # Menu 4 - Hapus Data
    elif pilihan == "4":
    
            print("\n--- HAPUS DATA BARANG ---")
    
            if len(data_barang) == 0:
                print("Belum ada data barang yang dapat dihapus.")
    
            else:
                while True:
                    id_hapus = input(
                        "Masukkan ID barang yang ingin dihapus: "
                    ).strip().upper()
    
                    if id_hapus == "":
                        print("ID tidak boleh kosong!")
                        continue
    
                    index_ditemukan = -1
    
                    # Mencari ID barang
                    for i in range(len(data_barang)):
                        if data_barang[i][0] == id_hapus:
                            index_ditemukan = i
                            break
    
                    if index_ditemukan == -1:
                        print("ID barang tidak ditemukan!")
    
                        ulang = input(
                            "Ingin mencoba lagi? (ya/tidak): "
                        ).strip().lower()
    
                        if ulang == "ya":
                            continue
                        else:
                            print("Kembali ke menu utama.")
                            break
    
                    # Menampilkan data yang akan dihapus
                    print("\nData yang akan dihapus:")
                    print(f"ID barang   : {data_barang[index_ditemukan][0]}")
                    print(f"Nama barang : {data_barang[index_ditemukan][1]}")
                    print(f"Lokasi      : {data_barang[index_ditemukan][2]}")
                    print(f"Status      : {data_barang[index_ditemukan][3]}")
    
                    # Konfirmasi penghapusan
                    while True:
                        konfirmasi = input(
                            "\nYakin ingin menghapus? (ya/tidak): "
                        ).strip().lower()
    
                        if konfirmasi == "ya":
                            data_barang.pop(index_ditemukan)
                            print("Data berhasil dihapus!")
                            break
    
                        elif konfirmasi == "tidak":
                            print("Penghapusan dibatalkan.")
                            break
    
                        else:
                            print("Pilihan tidak valid! Masukkan ya atau tidak.")
    
                    break

    # Menu 5 - Keluar

    elif pilihan == "5":

        print("\n=======================================")
        print("Terima kasih telah menggunakan program")   
        print("Program selesai.")
        print("=========================================")

        break

    # Validasi menu

    else:
        print("\nPilihan menu tidak valid")
        print("Silakan masukan angka 1 sampai 5.")             
