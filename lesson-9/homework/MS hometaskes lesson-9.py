#Obyektga Yo‘naltirilgan Dasturlash (OOP)
#1. Aylana Class
#Aylanani ifodalovchi class yarating. Uning yuzasi va perimetrini (uzunligini) hisoblaydigan metodlarni qo‘shing.

import math

class Aylana:
    def __init__(self, radius):
        self.radius = radius   # aylana radiusi

    def yuza(self):
        return math.pi * self.radius ** 2   # π * r^2

    def perimetr(self):
        return 2 * math.pi * self.radius   # 2 * π * r

aylana = Aylana(10)   # radius = 10
print("Radius:", aylana.radius)
print("Yuza:", aylana.yuza())
print("Perimetr:", aylana.perimetr())
#2. Shaxs (Person) Class
#Shaxsni ifodalovchi class yarating. Unda ism, mamlakat va tug‘ilgan sana kabi atributlar bo‘lsin. Shaxsning yoshini aniqlaydigan metodni qo‘shing.

from datetime import date

class Shaxs:
    def __init__(self, ism, mamlakat, tugilgan_sana):
        self.ism = ism
        self.mamlakat = mamlakat
        self.tugilgan_sana = tugilgan_sana  # tug‘ilgan sana (yyyy, mm, dd)

    def yosh(self):
        bugun = date.today()
        yil, oy, kun = self.tugilgan_sana
        tugilgan = date(yil, oy, kun)
        yosh = bugun.year - tugilgan.year
        # agar tug‘ilgan kun hali o‘tmagan bo‘lsa, yildan bitta ayriladi
        if (bugun.month, bugun.day) < (tugilgan.month, tugilgan.day):
            yosh -= 1
        return yosh


# Sinov uchun
shaxs1 = Shaxs("Zulaykho", "O‘zbekiston", (2000, 5, 15))
print("Ism:", shaxs1.ism)
print("Mamlakat:", shaxs1.mamlakat)
print("Yosh:", shaxs1.yosh())

#Kalkulyator Class
#Oddiy arifmetik amallarni bajaradigan class yarating. Unda qo‘shish, ayirish, ko‘paytirish va bo‘lish metodlari bo‘lsin.

class Kalkulyator:
    def qosh(self, a, b):
        return a + b

    def ayir(self, a, b):
        return a - b

    def kopaytir(self, a, b):
        return a * b

    def bol(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Nolga bo‘lish mumkin emas!")
        return a / b


# Sinov:
calc = Kalkulyator()
print("Qo‘shish: 7 + 3 =", calc.qosh(7, 3))
print("Ayirish: 7 - 3 =", calc.ayir(7, 3))
print("Ko‘paytirish: 7 * 3 =", calc.kopaytir(7, 3))
print("Bo‘lish: 7 / 3 =", calc.bol(7, 3))

#4. Shakl va Uning Voris Classlari
#Shaklni ifodalovchi class yarating. Uning yuzasi va perimetrini hisoblaydigan metodlari bo‘lsin. Keyin undan Aylana, Uchburchak, Kvadrat kabi voris classlarni yarating.

import math

# Asosiy Shakl classi
class Shakl:
    def yuza(self):
        raise NotImplementedError("Yuza metodi hali aniqlanmagan")

    def perimetr(self):
        raise NotImplementedError("Perimetr metodi hali aniqlanmagan")


# Aylana classi
class Aylana(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius


# Kvadrat classi
class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

    def perimetr(self):
        return 4 * self.tomon


# Uchburchak classi (teng tomonli deb olaylik)
class Uchburchak(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        # Geron formulasi (teng tomonli uchun)
        return (math.sqrt(3) / 4) * self.tomon ** 2

    def perimetr(self):
        return 3 * self.tomon


# Sinov
aylana = Aylana(8)
print("Aylana -> Yuza:", aylana.yuza(), " Perimetr:", aylana.perimetr())

kvadrat = Kvadrat(4)
print("Kvadrat -> Yuza:", kvadrat.yuza(), " Perimetr:", kvadrat.perimetr())

uchburchak = Uchburchak(6)
print("Uchburchak -> Yuza:", uchburchak.yuza(), " Perimetr:", uchburchak.perimetr())
#5. Ikkilik Qidiruv Daraxti (Binary Search Tree) Class
#Ikkilik qidiruv daraxtini ifodalovchi class yarating. Unda daraxtga element qo‘shish va uni qidirish metodlari bo‘lsin.

# Tugun (Node) classi
class Node:
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.left = None   # chap bolasi
        self.right = None  # o‘ng bolasi


# Ikkilik qidiruv daraxti classi
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Element qo‘shish
    def insert(self, qiymat):
        if self.root is None:
            self.root = Node(qiymat)
        else:
            self._insert(self.root, qiymat)

    def _insert(self, current, qiymat):
        if qiymat < current.qiymat:   # chap tomonga
            if current.left is None:
                current.left = Node(qiymat)
            else:
                self._insert(current.left, qiymat)
        elif qiymat > current.qiymat:  # o‘ng tomonga
            if current.right is None:
                current.right = Node(qiymat)
            else:
                self._insert(current.right, qiymat)
        # teng bo‘lsa, hech nima qilmaymiz (dublikat kiritmaymiz)

    # Qidirish
    def search(self, qiymat):
        return self._search(self.root, qiymat)

    def _search(self, current, qiymat):
        if current is None:
            return False
        if current.qiymat == qiymat:
            return True
        elif qiymat < current.qiymat:
            return self._search(current.left, qiymat)
        else:
            return self._search(current.right, qiymat)


# Sinov uchun
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(7)

print("8 bor:", bst.search(7))     # True
print("21 bor:", bst.search(20))   # False

#6. Stek (Stack) Ma’lumotlar Tuzilmasi
#Stekni ifodalovchi class yarating. Unda element qo‘shish (push) va olib tashlash (pop) metodlari bo‘lsin.

class Stack:
    def __init__(self):
        self.items = []   # stek elementlari ro‘yxatda saqlanadi

    # Element qo‘shish
    def push(self, item):
        self.items.append(item)

    # Elementni olib tashlash
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stek bo‘sh!"

    # Stek bo‘shligini tekshirish
    def is_empty(self):
        return len(self.items) == 0


# Sinov uchun
stek = Stack()
stek.push(10)
stek.push(20)
stek.push(30)

print("Pop:", stek.pop())  # 30
print("Pop:", stek.pop())  # 20
print("Pop:", stek.pop())  # 10
print("Pop:", stek.pop())  # Stek bo‘sh!

#7. Bog‘langan Ro‘yxat (Linked List) Ma’lumotlar Tuzilmasi
#Bog‘langan ro‘yxatni ifodalovchi class yarating. Unda ro‘yxatdagi elementlarni chiqarish, tugun qo‘shish va o‘chirish metodlari bo‘lsin.

# Tugun (Node) classi
class Node:
    def __init__(self, data):
        self.data = data    # qiymat
        self.next = None    # keyingi tugunga ishora


# Bog‘langan ro‘yxat (Linked List) classi
class LinkedList:
    def __init__(self):
        self.head = None    # ro‘yxat bosh tuguni

    # Ro‘yxat oxiriga tugun qo‘shish
    def insert(self, data):
        yangi = Node(data)
        if self.head is None:
            self.head = yangi
        else:
            current = self.head
            while current.next:   # oxirgi tugunni topish
                current = current.next
            current.next = yangi

    # Tugunni qiymat bo‘yicha o‘chirish
    def delete(self, data):
        current = self.head

        # agar bosh tugun o‘chirilsa
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        # boshqa tugunlar uchun
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return "Topilmadi!"

        prev.next = current.next
        current = None

    # Ro‘yxatni chiqarish
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


# Sinov uchun
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Ro‘yxat:", ll.display())   # [10, 20, 30]

ll.delete(20)
print("O‘chirildi (20):", ll.display())   # [10, 30]

ll.delete(50)
print("O‘chirildi (50):", ll.display())   # [10, 30]

#8. Savatcha (Shopping Cart) Class
#Savatchani ifodalovchi class yarating. Unda mahsulot qo‘shish, mahsulotni olib tashlash va umumiy narxni hisoblash metodlari bo‘lsin.

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {mahsulot: narx}

    # Mahsulot qo‘shish
    def add_item(self, nomi, narx):
        self.items[nomi] = narx

    # Mahsulotni olib tashlash
    def remove_item(self, nomi):
        if nomi in self.items:
            del self.items[nomi]
        else:
            print(f"{nomi} savatchada yo‘q!")

    # Umumiy narxni hisoblash
    def total_price(self):
        return sum(self.items.values())

    # Savatchani ko‘rsatish
    def show_cart(self):
        if not self.items:
            return "Savatcha bo‘sh!"
        return self.items


# Sinov uchun
cart = ShoppingCart()
cart.add_item("Non", 5000)
cart.add_item("Sut", 10000)
cart.add_item("Olma", 15000)

print("Savatcha:", cart.show_cart())   # {'Non': 5000, 'Sut': 10000, 'Olma': 15000}
print("Umumiy narx:", cart.total_price())  # 30000

cart.remove_item("Sut")
print("Sut olib tashlandi:", cart.show_cart())  # {'Non': 5000, 'Olma': 15000}
print("Yangi umumiy narx:", cart.total_price())  # 20000

#9. Stek (Stack) va Uni Ko‘rsatish
#Stekni ifodalovchi class yarating. Unda element qo‘shish, olib tashlash va stekdagi elementlarni ko‘rsatish metodlari bo‘lsin.

class Stack:
    def __init__(self):
        self.items = []

    # Element qo‘shish
    def push(self, item):
        self.items.append(item)

    # Elementni olib tashlash
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stek bo‘sh!"

    # Stek bo‘shligini tekshirish
    def is_empty(self):
        return len(self.items) == 0

    # Stekni ko‘rsatish
    def display(self):
        if self.is_empty():
            return "Stek bo‘sh!"
        return self.items


# Sinov uchun
stek = Stack()
stek.push(10)
stek.push(20)
stek.push(30)

print("Stek:", stek.display())  # [10, 20, 30]

print("Olib tashlandi:", stek.pop())  # 30
print("Stek:", stek.display())        # [10, 20]

print("Olib tashlandi:", stek.pop())  # 20
print("Stek:", stek.display())        # [10]

#10. Navbat (Queue) Ma’lumotlar Tuzilmasi
#Navbatni ifodalovchi class yarating. Unda element qo‘shish (enqueue) va olib tashlash (dequeue) metodlari bo‘lsin.

class Queue:
    def __init__(self):
        self.items = []

    # Element qo‘shish (oxiriga)
    def enqueue(self, item):
        self.items.append(item)

    # Elementni olib tashlash (boshidan)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Navbat bo‘sh!"

    # Navbat bo‘shligini tekshirish
    def is_empty(self):
        return len(self.items) == 0

    # Navbatni ko‘rsatish
    def display(self):
        if self.is_empty():
            return "Navbat bo‘sh!"
        return self.items


# Sinov uchun
navbat = Queue()
navbat.enqueue("Ali")
navbat.enqueue("Vali")
navbat.enqueue("Hasan")

print("Navbat:", navbat.display())  # ['Ali', 'Vali', 'Hasan']

print("Olib tashlandi:", navbat.dequeue())  # Ali
print("Navbat:", navbat.display())          # ['Vali', 'Hasan']

print("Olib tashlandi:", navbat.dequeue())  # Vali
print("Navbat:", navbat.display())          # ['Hasan']

#11. Bank Class
#Bankni ifodalovchi class yarating. Unda mijoz hisoblari va tranzaksiyalarni boshqaradigan metodlar bo‘lsin.

class Bank:
    def __init__(self):
        self.accounts = {}  # mijozlar hisoblari

    # Yangi hisob ochish
    def create_account(self, name, balance=0):
        if name in self.accounts:
            return f"{name} nomida hisob allaqachon mavjud!"
        self.accounts[name] = balance
        return f"{name} nomida {balance} so‘m bilan hisob ochildi."

    # Hisobga pul qo‘shish
    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            return f"{amount} so‘m {name} hisobiga qo‘shildi. Jami: {self.accounts[name]} so‘m"
        return f"{name} nomida hisob topilmadi!"

    # Hisobdan pul yechish
    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                return f"{amount} so‘m {name} hisobidan olindi. Qoldiq: {self.accounts[name]} so‘m"
            else:
                return "Hisobda yetarli mablag‘ yo‘q!"
        return f"{name} nomida hisob topilmadi!"

    # Hisobdan hisobga pul o‘tkazish
    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            return "Hisoblardan biri mavjud emas!"
        if self.accounts[sender] < amount:
            return "Yuboruvchi hisobida mablag‘ yetarli emas!"
        self.accounts[sender] -= amount
        self.accounts[receiver] += amount
        return f"{amount} so‘m {sender} hisobidan {receiver} hisobiga o‘tkazildi."

    # Hisobdagi pulni ko‘rish
    def get_balance(self, name):
        if name in self.accounts:
            return f"{name} hisobidagi qoldiq: {self.accounts[name]} so‘m"
        return f"{name} nomida hisob topilmadi!"


# Sinov uchun
bank = Bank()
print(bank.create_account("Ali", 1000))
print(bank.create_account("Vali", 500))
print(bank.deposit("Ali", 300))
print(bank.withdraw("Vali", 200))
print(bank.transfer("Ali", "Vali", 400))
print(bank.get_balance("Ali"))
print(bank.get_balance("Vali"))
