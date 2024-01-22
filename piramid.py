def piramid(tinggi):
    for i in range(tinggi, 0 ,-1):
        print(' ' *(tinggi - i) + '*' * (2 * i - 1))
tinggi_piramid = int(input("Masukkan tinggi piramid: "))
piramid(tinggi_piramid)