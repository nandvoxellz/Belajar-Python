# --- Set (set) ---
# set adalah tipe data yang tidak berurutan, tidak mengizinkan duplikat,
# tetapi dapat diubah (item bisa ditambah atau dihapus).

# properti set:

# Dapat diubah? (mutable): Ya
# Dapat menyimpan tipe data campuran (heterogen): Ya
# Dapat menyimpan duplikat: Tidak
# Dapat diindeks: Tidak

# Contoh penggunaan set
# set kosong:
kosong: set = set()

# set dengan beberapa item:
angka: set = {1, 2, 3, 4, 5}

# beberapa operasi dasar pada set

# add: menambahkan item ke set
angka.add(6)

# remove: menghapus item dari set
angka.remove(3) # jika item tidak ditemukan, akan menghasilkan error

# update: menambahkan item dari set lain atau iterable lain ke set
angka.update({7, 8, 9}) # menambahkan item dari set lain

# union: menggabungkan dua set
set_a: set = {1, 2, 3}
set_b: set = {3, 4, 5}
gabungan: set = set_a.union(set_b) # hasilnya adalah {1, 2, 3, 4, 5}

# atau dengan operator |
gabungan2: set = set_a | set_b # hasilnya juga {1, 2, 3, 4, 5}

# intersection: mendapatkan item yang ada di kedua set
irisan: set = set_a.intersection(set_b) # hasilnya adalah {3}

# difference: mendapatkan item yang ada di set pertama tetapi tidak di set kedua
beda: set = set_a.difference(set_b) # hasilnya adalah {1, 2}

# symmetric_difference: mendapatkan item yang ada di salah satu set tetapi tidak di kedua set
beda_simetris: set = set_a.symmetric_difference(set_b) # hasilnya adalah {1, 2, 4, 5}