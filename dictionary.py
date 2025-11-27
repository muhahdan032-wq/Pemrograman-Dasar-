# Membuat dictionary
mahasiswa = {
    "nama": "Muhammad Ahdan",
    "nim": "D0425317",
    "Kelas": "B sistem informasi",
}

# Menampilkan seluruh data
print("Data Mahasiswa:", mahasiswa)

# Mengakses data dengan key
print("Nama:", mahasiswa["nama"])

# Menambah data baru
mahasiswa["angkatan"] = 2023
print("Setelah menambah data:", mahasiswa)

# Mengubah data
mahasiswa["ipk"] = 3.85
print("Setelah mengubah IPK:", mahasiswa)

# Menghapus data
del mahasiswa["jurusan"]
print("Setelah menghapus jurusan:", mahasiswa)

# Menelusuri dictionary
for key, value in mahasiswa.items():
    print(f"{key} : {value}")
