## Dictionary, tuple, set, if
# 1. Ro'yxat yaratish va elementlarga murojaat qilish
# Besh xil meva saqlovchi ro'yxat yarating va uchinchi mevani chop eting (print qiling).
txt=["Olma", "Nok", "Banan", "Shaftoli", "Olcha"]
print(txt[2])
#2. Ikki ro'yxatni birlashtirish
#Ikki raqamlar ro'yxatini yarating va ularni bitta ro'yxatga birlashtiring.

txt1=["Jamshid", "Dilshod"]
txt2=["Davron", "Sarvar"]
print(txt1+txt2)
#3. Ro'yxatdan elementlarni ajratib olish
#Berilgan raqamlar ro'yxatidan birinchi, o‘rta va oxirgi elementlarni ajratib olib, yangi ro'yxatga saqlang.

ruyxat = ['olma', 'olcha', 'anor', 'uzum']
yangi_ruyxat = []

yangi_ruyxat.append(ruyxat[0])
yangi_ruyxat.append(ruyxat[-1])

print(yangi_ruyxat)
#4. Ro'yxatni kortejga aylantirish
#Sevimli beshta filmingiz ro'yxatini yarating va uni kortejga aylantiring.

ruyxat='Olma','Banan','Uzum','Apelsin','Nok'
ruyxat
#5.Ro'yxatda element borligini tekshirish
#Shaharlar ro'yxati berilgan. Unda "Paris" bor-yo‘qligini tekshiring va natijani chop eting.

shaharlar = ['New York', 'Tokyo', 'Paris', 'London']
if 'Paris' in shaharlar:
    print("bor")
else:
    print("Yo'q")

#6. Ro'yxatni takrorlash (dublikat qilish) — sikllarsiz
#Raqamlar ro'yxatini yarating va uni sikl (loop) ishlatmasdan takrorlang.

sonlar=[1,2,3,4,5]
yangi_sonlar = sonlar * 2
print(yangi_sonlar)
#7.Ro'yxatda birinchi va oxirgi elementlarni almashtirish
#Berilgan raqamlar ro'yxatida birinchi va oxirgi elementlarni o‘zaro almashtiring.

sonlar = [1, 2, 3, 4, 5, 6, 7]

sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]

print(sonlar)
#8.8. Kortejdan bo‘lakni ajratib olish (slice)
#1 dan 10 gacha bo‘lgan raqamlardan tashkil topgan kortej yarating va 3-7 indeks oralig‘idagi bo‘lakni chop eting.

ruyxat=(1,2,3,4,5,6,7,8,9,10)
ruyxat[2:7]

#9. Ro'yxatda nechta marta uchrashini hisoblash
#Ranglar ro'yxatini yarating va unda "blue" so‘zi nechta marta uchrashini hisoblang.



list_rang=('blue','white', 'blue', 'red','yellow','green','blue')
soni=list_rang.count('blue')
soni
#10. Kortejda element indeksini topish
#Hayvonlar korteji berilgan. Undan "lion" elementining indeksini toping.

hayvonlar=("Bear","Fox", "Tiger", "Dog", "Monkey", "Cow", "Lion")
indeks=hayvonlar.index("Lion")
indeks
#11. Ikki kortejni birlashtirish
#Ikki raqamlar kortejini yarating va ularni bitta kortejga birlashtiring.

ruyxat1=("Akmal", "Sarvar")
ruyxat2=(1,3,7)
jamlanma=ruyxat1+ruyxat2
jamlanma
#12. Ro'yxat va kortej uzunligini topish
#Berilgan ro'yxat va kortej uzunligini toping va chop eting.

ruyxat=('Nodir',33, "Siroj","Humoyun","Jamshid",66)
uzunlik=len(ruyxat)
uzunlik
#13. Kortejni ro'yxatga aylantirish
#Besh raqamdan iborat kortej yarating va uni ro'yxatga aylantiring.

a=(1,2,3,4,5)
a=list(a)
a
#14. Kortejdagi maksimal va minimal qiymatlarni topish
#Berilgan raqamlar kortejidan eng katta va eng kichik qiymatlarni topib, chop eting

b=(15,8,9,23,75,43,89,14,5,32,88,98,56)
minimal=min(b)
minimal


maksimal=max(b)
maksimal
#15. Kortejni teskari tartibda chiqarish
#So‘zlardan iborat kortej yarating va uni teskari tartibda chop eting.

d=("olma", "suv", "asal", "lion", "moliya")
f=d[::-1]
f
