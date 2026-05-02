# --- Dictionary (dict) ---
# Dictionary adalah tipe data yang digunakan untuk menyimpan pasangan kunci-nilai (key-value pairs).
# Dictionary dibuat dengan menggunakan tanda kurung kurawal {} dan setiap pasangan kunci-nilai
# dipisahkan dengan koma. Kunci dan nilai dipisahkan dengan tanda titik dua :.

# {kunci1: nilai1, kunci2: nilai2, ...}

# properti dictionary:

# Dapat diubah? (mutable): Ya
# Dapat menyimpan tipe data campuran (heterogen): Ya
# Dapat menyimpan duplikat: Tidak (kunci harus unik)
# Dapat diindeks: Tidak (tapi dapat diakses melalui kunci)

# cara membuat dictionary
profile: dict[str, str] = {
    "nama": "Nand",
    "best_friend": "Miwa",
    "hobby": "coding"
}

# tipe data campuran
data_campuran: dict[str, str | int | bool] = {
    "nama": "Nand",
    "umur": 20,
    "is_student": True
}

# dictionary kosong
kosong: dict = {}
#atau
kosong_lagi: dict[str, int] = {}

# beberapa operasi dasar pada dictionary

dict_domisil: dict[str, str] = {
    "Nand": "Banjarmasin",
    "Miwa": "Karawang",
    "Neweya": "Surabaya"
}

# kunci
print(dict_domisil.keys()) # output: dict_keys(['Nand', 'Miwa', 'Neweya'])

# nilai
print(dict_domisil.values()) # output: dict_values(['Banjarmasin', 'Karawang', 'Surabaya'])

# pasangan kunci-nilai
print(dict_domisil.items()) 
# output: dict_items([('Nand', 'Banjarmasin'), ('Miwa', 'Karawang'), ('Neweya', 'Surabaya')])

# mengecek apakah sebuah kunci ada dalam dictionary
print("Nand" in dict_domisil) # output: True
print("Vox" in dict_domisil) # output: False

# atau nilai
print("Banjarmasin" in dict_domisil.values()) # output: True
print("Jakarta" in dict_domisil.values()) # output: False

# mengakses nilai melalui kunci
print(dict_domisil["Nand"]) # output: Banjarmasin
print(dict_domisil["Miwa"]) # output: Karawang
print(dict_domisil["Neweya"]) # output: Surabaya

# atau dengan metode get (lebih aman karena tidak akan menghasilkan error jika kunci tidak ditemukan)
print(dict_domisil.get("Nand")) # output: Banjarmasin
print(dict_domisil.get("Vox")) # output: None (karena kunci "Vox" tidak ditemukan)

# mengubah nilai pada kunci tertentu
dict_domisil["Neweya"] = "Bandung" # sekarang nilai untuk kunci "Neweya" adalah "Bandung"

# mengupdate dictionary dengan pasangan kunci-nilai baru
dict_domisil.update({"Vox": "Jakarta"}) # menambahkan kunci "Vox" dengan nilai "Jakarta"

# menghapus pasangan kunci-nilai dengan kunci tertentu
dict_domisil.pop("Vox") # menghapus pasangan dengan kunci "Vox"

# menggabungkan dua dictionary
dict_ibukota_asean: dict[str, str] = {
    "Indonesia": "Jakarta",
    "Malaysia": "Kuala Lumpur",
    "Vietnam" : "Hanoi"
}

dict_ibukota_nordic: dict[str, str] = {
    "Swedia": "Stockholm",
    "Norwegia": "Oslo",
    "Denmark": "Kopenhagen"
}

# union (Python 3.9+)
gabungan: dict[str, str] = dict_ibukota_asean | dict_ibukota_nordic
print(gabungan)