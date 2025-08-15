#1. Kabisa yilin hisoblash bo'yicha Pythonda dastur yarating

yil=int(input("Yilni kiriting"))
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Kabisa yil")
else:
    print("Oddiy yil")

#2. Шартли операторлар машқи
#Бутун сон n берилган. Қуйидаги шартларга амал қилинг:
#•	Агар n тўқ бўлса, "Weird" деб чиқаринг.
#•	Агар n жўфт бўлса ва 2 дан 5 гача (ҳам киритилган ҳолда) оралиқда бўлса, "Not Weird" деб чиқаринг.
#•	Агар n жўфт бўлса ва 6 дан 20 гача (ҳам киритилган ҳолда) оралиқда бўлса, "Weird" деб чиқаринг.
#•	Агар n жўфт бўлса ва 20 дан катта бўлса, "Not Weird" деб чиқаринг.

#2.1 masala yechimi
n=int(input(["butun son kiriting"]))
if n%2!=0:
    print("weird")
else:
    print(" Not weird")

#2.2 masala yechimi- Агар n жўфт бўлса ва 2 дан 5 гача (ҳам киритилган ҳолда) оралиқда бўлса, "Not Weird" деб чиқаринг.
#2 va 4 raqamini kiritib tekshirib ko'ramiz
n=int(input(["butun son kiriting"]))
if n%2!=0:
    print("weird")
else:
    print(" Not weird")
# 2.3 masala yechimi--- Агар n жўфт бўлса ва 6 дан 20 гача (ҳам киритилган ҳолда) оралиқда бўлса, "Weird" деб чиқаринг.
n = int(input("Butun son kiriting: "))

if n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
#2.4 masala yechimi----Агар n жўфт бўлса ва 20 дан катта бўлса, "Not Weird" деб чиқаринг.
#20 dan katta ixiyoriy juft raqamni kiritish orqali hisoblab ko'ramiz (masalan 22,24,26)
n = int(input("Butun son kiriting: "))

if n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")






#3.1 Икки бутун сон a ва b берилган. a ва b (ҳам қўшиб ҳисобланади) орасидаги жўфт сонларни топинг. Цикл (loop) ишлатманг
# If va else operatorlarisiz--- 5 va 10 oralig'idagi raqamlar olindi
a = int(input("a = "))
b = int(input("b = "))

evens = list(range(a + (a % 2), b + 1, 2))
print(evens)
#3.2 Икки бутун сон a ва b берилган. a ва b (ҳам қўшиб ҳисобланади) орасидаги жўфт сонларни топинг. Цикл (loop) ишлатманг
# If va else operatorlarini ishlatgan holda--- 3 va 12 oralig'idagi raqamlar olindi
a = int(input("a = "))
b = int(input("b = "))

# a- juft songa to'g'rilaymiz
if a % 2 != 0:
    a += 1
else:
    a = a

# b- juft songa to'g'rilaymiz
if b % 2 != 0:
    b -= 1
else:
    b = b

# range orqali juft sonlar ro'yxatini chiqarib olamiz
evens = list(range(a, b + 1, 2))
print(evens)
