# --- List (list) ---
# List adalah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel. 
# List dibuat dengan menggunakan tanda kurung siku [] dan item-item di dalamnya dipisahkan dengan koma.

# properti list:

# Dapat diubah? (mutable): Ya
# Dapat menyimpan tipe data campuran (heterogen): Ya
# Dapat menyimpan duplikat: Ya
# Dapat diindeks: Ya


# Contoh penggunaan list
angka: list = [1, 2, 3, 4, 5]
nama: list = ["Nand", "Miwa", "Neweya"]
elemen_campuran: list[str | int | bool] = ["Nand", 20, True]

# beberapa operasi dasar pada list

# append: menambahkan item ke akhir list
angka.append(6)

# extend: menambahkan item dari list lain ke akhir list
angka.extend([7, 8, 9])

# remove: menghapus item pertama yang ditemukan dalam list
angka.remove(9) # jika ada duplikat, hanya yang pertama yang dihapus
                # jika item tidak ditemukan, akan menghasilkan error

# pop: menghapus item pada indeks tertentu dan mengembalikan item tersebut
terakhir: int = angka.pop() # menghapus item terakhir
print(terakhir) # output: 8
# atau bisa juga dengan indeks tertentu
kedua: int = angka.pop(1) # menghapus item pada indeks 1 (yaitu angka 2)
print(kedua) # output: 2
# indeks selalu dimulai dari 0, jadi angka[0] adalah 1, angka[1] adalah 2, dan seterusnya

# insert: menambahkan item pada indeks tertentu
nama.insert(1, "Vox") # menambahkan "Vox" pada indeks 1

# index assignment: mengganti item pada indeks tertentu
nama[0] = "Velvette"

# clear: menghapus semua item dalam list
elemen_campuran.clear() # setelah ini, elemen_campuran akan menjadi list kosong []