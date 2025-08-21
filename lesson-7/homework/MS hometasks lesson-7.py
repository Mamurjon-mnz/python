# map ва filter funksiyalari haqida o'rganing va sinfda ularni tushintirib berishga tayyorlaning.
#  lambda ifodalari bilan ushbu funksiyalardan foydalanishga misollar keltiring
#1.1 map va filter funksiyalari bo'yicha misollar
#Ro'yxat keltirilgan ushbu ro'yxatdan toq sonlarni toping va ularning kvadratlarini chiqaring
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

kvadratlar = list(map(lambda x: x**2, sonlar))

print("Asosiy sonlar:", sonlar)
print("Kvadratlar:", kvadratlar)
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))

print("Asosiy sonlar:", sonlar)
print("Juft sonlar:", juft_sonlar)
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

toq_kvadratlar = list(map(lambda x: x**2, filter(lambda x: x % 2 ==1, sonlar)))

print("Asosiy sonlar:", sonlar)
print("Toq sonlar kvadratlari", toq_kvadratlar)
#1. is_prime(n) funksiyasi
#is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, 
# aks holda False qiymat qaytarsin.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4)) 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
#2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum(k):
    yigindi = 0
    for raqam in str(k):
        yigindi += int(raqam)
    return yigindi
print(digit_sum(24))
print(digit_sum(502))
print(digit_sum(701))

#3. Ikki sonning darajalari
#Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def powers_of_two(N):
    natija = []
    k = 1
    while 2**k <= N:
        natija.append(2**k)
        k += 1
    return natija

print(powers_of_two(10))
