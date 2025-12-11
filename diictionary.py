# Nuri Zilvani
# D0425008


# Membuat dictionary
mahasiswa = {
    "nama": "Nurul Arifka",
    "umur": "21",
    "jurusan": "Teknik Informatika",
    "ipk": 3.75
}

# Akses data
print("Nama mahasiswa:", mahasiswa["nama"])
print("umur:", mahasiswa.get("umur"))

# Menambah data
mahasiswa["semester"] = 5

# Iterasi
print("\nData lengkap:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")