ulang = 'Y'
while ulang == 'Y':
    print('program menginap di hotel')
    print('|        |  Superior     |  Delux       |  Premium     |')
    print('|________|_______________|______________|______________|')
    print('|1-2 Hari|110.000/night  |160.000/night |210.000/night |')
    print('|3-4 Hari|95.000/night   |145.000/night |190.000/night |')
    print('|>5 Hari |85.000/night   |130.000/night |170.000/night |')
    print('|________|_______________|______________|______________|')

    nama = input('Masukan nama: ')
    print('Tipe kamar')
    print('1.Superior')
    print('2.Deluxe')
    print('3.Premium')
    tipe_kamar = int(input('Pilih tipe kamar: '))
    lama_menginap = int(input('Lama menginap: '))
    # harga_per_malam = ''

    print('===== Pembayaran =====')
    print('Nama: '+nama)
    if tipe_kamar == 1:     
        print('Tipe kamar: Superior')
    elif tipe_kamar == 2:
        print('Tipe kamar: Deluxe')
    elif tipe_kamar == 3:
        print('Tipe kamar: premium')

    print(f"Lama menginap: {lama_menginap}")

    if lama_menginap == 1 or lama_menginap == 2:
        if tipe_kamar == 1:
            total = 110000 * lama_menginap
            print(f'Total pembayaran: {total}')
        elif tipe_kamar == 2:
            total = 160000 * lama_menginap
            print(f'Total pembayaran: {total}')
        elif tipe_kamar == 3:
            total = 210000 * lama_menginap
            print(f'Total pembayaran: {total}')
            
    elif lama_menginap == 3 or lama_menginap == 4:
        if tipe_kamar == 1:
            total = 95000 * lama_menginap
            print(f'Total pembayaran: {total}')
        elif tipe_kamar == 2:
            total = 145000 * lama_menginap
            print(f'Total pembayaran: {total}')
        elif tipe_kamar == 3:
            total = 190000 * lama_menginap
            print(f'Total pembayaran: {total}')
            
    elif lama_menginap >= 5:
        if tipe_kamar == 1:
            total = 85000 * lama_menginap
            print(f'Total pembayaran: {total}')
        elif tipe_kamar == 2:
            total = 130000 * lama_menginap
            print(f'Total pembayaran: {total}')
        elif tipe_kamar == 3:
            total = 170000 * lama_menginap
            print(f'Total pembayaran: {total}')

    ulang = input('Ingin memesan ulang?(Y/N)')
        
print('Terimakasih telah memesan')