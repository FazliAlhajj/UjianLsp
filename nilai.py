print('Masukkan Lima Buah Nilai')
nilaiA = int(input("Masukkan Nilai A : "))
nilaiB = int(input("Masukkan Nilai B : "))
nilaiC = int(input("Masukkan Nilai C : "))
nilaiD = int(input("Masukkan Nilai D : "))
nilaiE = int(input("Masukkan Nilai E : "))

mylist = [nilaiA, nilaiB, nilaiC, nilaiD, nilaiE]

for i in range(len(mylist) - 1, 0, -1):
    for j in range(i):
        if mylist[j] > mylist[j + 1]:
            simpan = mylist[j]
            mylist[j] = mylist[j + 1]
            mylist[j + 1] = simpan
print(f"Urutan Nilai Descending {mylist}")

for i in range(len(mylist) - 1, 0, -1 ):
    for j in range(i):
        if mylist[j] < mylist[j + 1]:
            simpan = mylist[j]
            mylist[j] = mylist[j + 1]
            mylist[j + 1] = simpan
print(f"Urutan Nilai Ascending {mylist}")

total = nilaiA + nilaiB + nilaiC + nilaiD + nilaiE

print(f"Nilai MAX : {max(mylist)}")
print(f"Nilai MIN : {min(mylist)}")
print(f"Nilai Rata-rata : {int(total / 5)}")
