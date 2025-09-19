#1. Ro‘yxatni 1D Massivga aylantirish
#Vazifa: Raqamli qiymatlar ro‘yxatini bitta o‘lchovli NumPy massiviga aylantiring.

import numpy as np

# Original ro‘yxat
my_list = [12.23, 13.32, 100, 36.32]
print("Asl ro‘yxat:", my_list)

# NumPy massiviga aylantirish
arr = np.array(my_list)
print("Bir o‘lchovli NumPy massivi:", arr)

2. #3x3 Matritsa (2 dan 10 gacha)

#Vazifa: 2 dan 10 gacha bo‘lgan qiymatlar bilan 3x3 matritsa yarating.
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

#3. 10 ta nol massivi va oltinchi qiymatni yangilash

#Vazifa: 10 ta nol (0) elementdan iborat massiv yarating va 6-qiymatini 11 ga o‘zgartiring.
massiv = np.zeros(10)
print("Boshlang‘ich:", massiv)

massiv[5] = 11  # 6-qiymat (indeks 5)
print("Yangilangandan keyin:", massiv)

#4. 12 dan 38 gacha massiv

#Vazifa: 12 dan 38 gacha bo‘lgan massiv yarating.
arr=np.arange(1,38,1)
print(arr)
arr = np.arange(12, 38)  # 1-usul
print(arr)

filter1=arr>11    #2-usul
filter2=arr<38
filter3=filter1 & filter2
arr[filter1]
#Massivni float turiga o‘tkazish

#Vazifa: Massivni float turiga aylantiring.
arr = np.array([1, 2, 3, 4])
print("Asl massiv:", arr)

arr_float = arr.astype(float)
print("Float massiv:", arr_float)

#6. Selsiydan Farangeytga o‘tkazish

#Vazifa: Selsiydagi qiymatlarni Farangeytga o‘tkazing. Formula:
#   F=C*9/5+32

celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32

print("Selsiy qiymatlari:", celsius)
print("Farangeyt qiymatlari:", fahrenheit)

#7. Massiv oxiriga qiymat qo‘shish

#Vazifa: Massiv oxiriga yangi qiymatlar qo‘shing.
arr = np.array([10, 20, 30])
print("Asl massiv:", arr)

new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("Qiymat qo‘shilgandan keyin:", new_arr)

#8. Statistik funksiyalar

#Vazifa: 10 ta elementli tasodifiy massiv yarating va uning o‘rtacha (mean), median, va standart og‘ishini toping.
arr = np.random.randint(1, 100, 10)
print("Massiv:", arr)

print("O‘rtacha:", np.mean(arr))
print("Median:", np.median(arr))
print("Standart og‘ish:", np.std(arr))

#9. Min va Max qiymat

#Vazifa: 10x10 o‘lchamli tasodifiy massiv yarating va uning eng kichik hamda eng katta qiymatini toping.
arr = np.random.rand(10, 10)
print("Massiv:\n", arr)

print("Minimal qiymat:", arr.min())
print("Maksimal qiymat:", arr.max())

#10. 3x3x3 o‘lchamli massiv

#Vazifa: 3x3x3 o‘lchamli tasodifiy massiv yarating.
arr = np.random.rand(3, 3, 3)
print(arr)
