"""
Semua sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial :langkah berurutan.
2. Percabangan : langkah loncat jika suatu kondisi terpenuhi.
3. perulangan : mengulang langkah berkali-kali selama/sampai kondisi terpenuhi.
"""

# Sekuensial
print('Ibu memberi perintah,"Beli satu botol susu"')
print('Anak menjawab,"OK"')
print('Anak pergi ke toko')

# Percabangan
jumlah_botol_susu = 69
if jumlah_botol_susu >0:
    print('Anak mengecek harganya cukup')
    print('Anak membeli satu botol susu')
    jumlah_telur_ayam = 9
    print('Anak bertanya, "Apakah telur ada"')
    if jumlah_telur_ayam >0:
        print('Penjual menjawa,"Ada"')
        print('Anak membeli enam butir telur')
    else:
        print('Anak membeli satu botol susu')
else:
    print('Anak tidak jadi membeli susu')

print('Anak pulang ke rumah')
print('Menyerahkan hasil belanjanya kepada Ibu')

