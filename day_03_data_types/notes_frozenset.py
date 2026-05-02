# --- Frozenset (frozenset) ---
# frozenset adalah tipe data yang tidak berurutan, tidak mengizinkan duplikat,
# dan tidak dapat diubah (item tidak bisa ditambah atau dihapus).

# properti frozenset:

# Dapat diubah? (mutable): Tidak
# Dapat menyimpan tipe data campuran (heterogen): Ya
# Dapat menyimpan duplikat: Tidak
# Dapat diindeks: Tidak

# cara membuat frozenset
# dengan menggunakan fungsi frozenset()
set_beku: frozenset[int] = frozenset({1, 2, 3, 4, 5})

# sifatnya sama saja dengan set, tetapi tidak bisa diubah
# set_beku.add(6) # ini akan menghasilkan error karena frozenset tidak bisa diubah

# operasi pada frozenset sama dengan set, tetapi hasilnya juga berupa frozenset
nama: frozenset[str] = frozenset({"Nand", "Miwa", "Neweya"})
nama_lain: frozenset[str] = frozenset({"Miwa", "Alya", "Nand"})

# union
gabungan: frozenset[str] = nama.union(nama_lain)
# output: frozenset({'Nand', 'Miwa', 'Neweya', 'Alya'})

# intersection
irisan: frozenset[str] = nama.intersection(nama_lain)
# output: frozenset({'Nand', 'Miwa'})

# difference
beda: frozenset[str] = nama.difference(nama_lain)
# output: frozenset({'Neweya'})

# symmetric_difference
beda_simetris: frozenset[str] = nama.symmetric_difference(nama_lain)
# output: frozenset({'Neweya', 'Alya'})

# "tapi Nand, kalau frozenset itu tidak bisa diubah, buat apa sih?"
# T H I S

paket_nasi_goreng: frozenset = frozenset({"nasi goreng", "es teh", "kerupuk"})
paket_ayam_bakar: frozenset = frozenset({"ayam bakar", "nasi", "lalapan"})

harga: dict = {
    paket_nasi_goreng: 25_000,
    paket_ayam_bakar: 35_000
}