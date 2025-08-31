#1. Task Class (Vazifa Classi):

#Vazifaning nomi (title)
#Vazifaning tavsifi (description)
#Tugash muddati (due date)
#Holati (status: bajarilgan yoki yo‘q)

from datetime import datetime, date

class Task:
    def __init__(self, title: str, description: str = "", due_date=None):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title matn bo'lishi va bo'sh bo'lmasligi kerak.")
        self.title = title.strip()
        self.description = description.strip() if isinstance(description, str) else str(description)

        if due_date is None:
            self.due_date = None
        elif isinstance(due_date, date):
            self.due_date = due_date
        elif isinstance(due_date, str):
            parsed = None
            for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
                try:
                    parsed = datetime.strptime(due_date, fmt).date()
                    break
                except ValueError:
                    continue
            if parsed is None:
                raise ValueError("due_date format: 'YYYY-MM-DD' yoki 'DD.MM.YYYY' yoki 'DD/MM/YYYY'")
            self.due_date = parsed
        else:
            raise TypeError("due_date None, str yoki datetime.date bo'lishi kerak.")

        self.status = "Bajarilmagan"

    def mark_complete(self):
        self.status = "Bajarildi"

    def __str__(self):
        due = self.due_date.isoformat() if isinstance(self.due_date, date) else (str(self.due_date) if self.due_date else "—")
        return f"Nomi: {self.title} | Tavsif: {self.description} | Tugash muddati: {due} | Holat: {self.status}"


# Misol uchun ishlatish:
if __name__ == "__main__":
    t1 = Task("Uy ishlarini qilish", "Xonani tozalash va idishlarni yuvish", "2025-08-30")
    print(t1)
    t1.mark_complete()
    print(t1)

    t2 = Task("Kitob o'qish", "Python bo'yicha 30 sahifa", "30.08.2025")
    print(t2)

#2. ToDoList Class (Ro‘yxat Classi):
#Vazifa qo‘shish
#Vazifani “bajarildi” deb belgilash
#Barcha vazifalarni chiqarish
#Faqat tugallanmagan (incomplete) vazifalarni ko‘rsatish

from datetime import datetime, date

class Task:
    def __init__(self, title: str, description: str = "", due_date=None):
        self.title = title.strip()
        self.description = description.strip() if isinstance(description, str) else str(description)

        if due_date is None:
            self.due_date = None
        elif isinstance(due_date, date):
            self.due_date = due_date
        elif isinstance(due_date, str):
            parsed = None
            for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
                try:
                    parsed = datetime.strptime(due_date, fmt).date()
                    break
                except ValueError:
                    continue
            if parsed is None:
                raise ValueError("due_date format: 'YYYY-MM-DD' yoki 'DD.MM.YYYY' yoki 'DD/MM/YYYY'")
            self.due_date = parsed
        else:
            raise TypeError("due_date None, str yoki datetime.date bo'lishi kerak.")

        self.status = "Bajarilmagan"

    def mark_complete(self):
        self.status = "Bajarildi"

    def __str__(self):
        due = self.due_date.isoformat() if isinstance(self.due_date, date) else (str(self.due_date) if self.due_date else "—")
        return f"Nomi: {self.title} | Tavsif: {self.description} | Tugash muddati: {due} | Holat: {self.status}"


# ToDoList Classi
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_task_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("❌ Noto‘g‘ri indeks!")

    def list_tasks(self):
        if not self.tasks:
            print("📌 Vazifalar ro‘yxati bo‘sh!")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Bajarilmagan"]
        if not incomplete:
            print("✅ Barcha vazifalar bajarilgan!")
        else:
            for i, task in enumerate(incomplete, start=1):
                print(f"{i}. {task}")


# Misol uchun ishlatish
if __name__ == "__main__":
    todo = ToDoList()

    # Vazifa qo‘shamiz
    todo.add_task(Task("Uy ishlarini qilish", "Xonani tozalash va idishlarni yuvish", "2025-08-30"))
    todo.add_task(Task("Kitob o‘qish", "Python bo‘yicha 30 sahifa", "30.08.2025"))
    todo.add_task(Task("Sport", "30 daqiqa yugurish"))

    print("\n📋 Barcha vazifalar:")
    todo.list_tasks()

    print("\n⏳ Bajarilmagan vazifalar:")
    todo.list_incomplete_tasks()

    # Ikkinchi vazifani bajarilgan deb belgilaymiz
    todo.mark_task_complete(1)

    print("\n📋 Yangilangan vazifalar:")
    todo.list_tasks()

    print("\n⏳ Qolgan bajarilmagan vazifalar:")
    todo.list_incomplete_tasks()

#3. Asosiy Dastur (CLI):
#Vazifa qo‘shish
#Vazifani bajarildi deb belgilash
#Barcha vazifalarni ko‘rish
#Faqat tugallanmagan vazifalarni ko‘rish

from datetime import datetime, date

class Task:
    def __init__(self, title: str, description: str = "", due_date=None):
        self.title = title.strip()
        self.description = description.strip() if isinstance(description, str) else str(description)

        if due_date is None:
            self.due_date = None
        elif isinstance(due_date, date):
            self.due_date = due_date
        elif isinstance(due_date, str):
            parsed = None
            for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
                try:
                    parsed = datetime.strptime(due_date, fmt).date()
                    break
                except ValueError:
                    continue
            if parsed is None:
                raise ValueError("due_date format: 'YYYY-MM-DD' yoki 'DD.MM.YYYY' yoki 'DD/MM/YYYY'")
            self.due_date = parsed
        else:
            raise TypeError("due_date None, str yoki datetime.date bo'lishi kerak.")

        self.status = "Bajarilmagan"

    def mark_complete(self):
        self.status = "Bajarildi"

    def __str__(self):
        due = self.due_date.isoformat() if isinstance(self.due_date, date) else (str(self.due_date) if self.due_date else "—")
        return f"Nomi: {self.title} | Tavsif: {self.description} | Tugash muddati: {due} | Holat: {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_task_complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("✅ Vazifa bajarilgan deb belgilandi!")
        else:
            print("❌ Noto‘g‘ri indeks!")

    def list_tasks(self):
        if not self.tasks:
            print("📌 Vazifalar ro‘yxati bo‘sh!")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Bajarilmagan"]
        if not incomplete:
            print("✅ Barcha vazifalar bajarilgan!")
        else:
            for i, task in enumerate(incomplete, start=1):
                print(f"{i}. {task}")


# === CLI menyu ===
def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menyu ---")
        print("1. Vazifa qo‘shish")
        print("2. Vazifani bajarildi deb belgilash")
        print("3. Barcha vazifalarni ko‘rish")
        print("4. Faqat tugallanmagan vazifalarni ko‘rish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ").strip()

        if choice == "1":
            title = input("Vazifa nomi: ")
            description = input("Tavsif: ")
            due_date = input("Tugash muddati (YYYY-MM-DD yoki DD.MM.YYYY) [ixtiyoriy]: ").strip()
            due_date = due_date if due_date else None
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("✅ Vazifa qo‘shildi!")

        elif choice == "2":
            todo.list_tasks()
            try:
                index = int(input("Qaysi vazifa bajarildi deb belgilanadi? (raqam): ")) - 1
                todo.mark_task_complete(index)
            except ValueError:
                print("❌ Iltimos, son kiriting!")

        elif choice == "3":
            print("\n📋 Barcha vazifalar:")
            todo.list_tasks()

        elif choice == "4":
            print("\n⏳ Faqat tugallanmagan vazifalar:")
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("👋 Dasturdan chiqildi.")
            break

        else:
            print("❌ Noto‘g‘ri tanlov! Qaytadan urinib ko‘ring.")


if __name__ == "__main__":
    main()

#4. Sinov (Test):
#Vazifa qo‘shib, metodlarni tekshirish

# === Test uchun ===
# Oldingi yozgan classlar kerak bo‘ladi (Task, ToDoList)

# Vazifalar ro‘yxati obyektini yaratamiz
todo = ToDoList()

# 1) Vazifa qo‘shamiz
task1 = Task("Python darsini o‘qish", "OOP mavzusini ko‘rish", "2025-09-01")
task2 = Task("Sport bilan shug‘ullanish", "Yugurish 30 daqiqa", "2025-09-02")

todo.add_task(task1)
todo.add_task(task2)

print("\n📋 Barcha vazifalar:")
todo.list_tasks()

# 2) Birinchi vazifani bajarilgan deb belgilaymiz
print("\n✅ 1-vazifa bajarildi deb belgilaymiz:")
todo.mark_task_complete(0)

# 3) Barcha vazifalarni yana chiqaramiz
print("\n📋 Yangilangan vazifalar:")
todo.list_tasks()

# 4) Faqat tugallanmagan vazifalarni chiqaramiz
print("\n⏳ Faqat tugallanmagan vazifalar:")
todo.list_incomplete_tasks()

#II.Oddiy Blog Tizimi
#1. Post Class (Maqola Classi):
#Sarlavha (title)
#Matn (content)
#Muallif (author)

# Maqola (Post) Classi
class Post:
    def __init__(self, title, content, author):
        self.title = title          # Sarlavha
        self.content = content      # Matn
        self.author = author        # Muallif

    def display_post(self):
        """Maqolani chiroyli chiqarish"""
        print(f"Sarlavha: {self.title}")
        print(f"Matn: {self.content}")
        print(f"Muallif: {self.author}")
        print("-" * 40)


# Misol uchun ishlatish
post1 = Post("Python OOP", "Bugun biz classlarni o‘rganamiz.", "Ma'mur")
post2 = Post("Sportning foydasi", "Har kuni sport bilan shug‘ullanish kerak.", "Zulaykho")

# Maqolalarni chiqaramiz
post1.display_post()
post2.display_post()


#2. Blog Class (Blog Classi):
#Post qo‘shish
#Barcha postlarni ko‘rsatish
#Muallif bo‘yicha postlarni ko‘rsatish

# Blog Classi
class Blog:
    def __init__(self):
        self.posts = []   # Barcha maqolalarni saqlash uchun ro'yxat

    def add_post(self, post):
        """Yangi post qo'shish"""
        self.posts.append(post)

    def show_all_posts(self):
        """Barcha postlarni chiqarish"""
        if not self.posts:
            print("Hozircha postlar yo‘q.")
        else:
            for post in self.posts:
                post.display_post()

    def show_posts_by_author(self, author):
        """Muallif bo‘yicha postlarni chiqarish"""
        found = False
        for post in self.posts:
            if post.author == author:
                post.display_post()
                found = True
        if not found:
            print(f"{author} tomonidan yozilgan postlar topilmadi.")
            

# Sinov uchun foydalanamiz
post1 = Post("Python OOP", "Bugun biz classlarni o‘rganamiz.", "Ma'mur")
post2 = Post("Sportning foydasi", "Har kuni sport bilan shug‘ullanish kerak.", "Zulaykho")
post3 = Post("Kitob o‘qish", "Kitob insonni bilimli qiladi.", "Ma'mur")

# Blog yaratamiz
blog = Blog()

# Post qo'shamiz
blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)

print("\n--- Barcha postlar ---")
blog.show_all_posts()

print("\n--- Ma'mur yozgan postlar ---")
blog.show_posts_by_author("Ma'mur")

print("\n--- Zulaykho yozgan postlar ---")
blog.show_posts_by_author("Zulaykho")

print("\n--- Ali yozgan postlar ---")
blog.show_posts_by_author("Ali")

#Asosiy Dastur (CLI):
#Post qo‘shish
#Barcha postlarni ko‘rish
#Muallif bo‘yicha postlarni ko‘rish

# Post Class (Maqola)
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        print(f"\nSarlavha: {self.title}")
        print(f"Matn: {self.content}")
        print(f"Muallif: {self.author}")


# Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def show_all_posts(self):
        if not self.posts:
            print("\nHozircha postlar yo‘q.")
        else:
            for post in self.posts:
                post.display_post()

    def show_posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author == author:
                post.display_post()
                found = True
        if not found:
            print(f"\n{author} tomonidan yozilgan postlar topilmadi.")


# Asosiy dastur (CLI)
def main():
    blog = Blog()

    while True:
        print("\n--- BLOG TIZIMI ---")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlarni ko‘rish")
        print("4. Chiqish")

        choice = input("Tanlang (1-4): ")

        if choice == "1":
            title = input("Sarlavha: ")
            content = input("Matn: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("✅ Post qo‘shildi!")

        elif choice == "2":
            blog.show_all_posts()

        elif choice == "3":
            author = input("Muallif ismini kiriting: ")
            blog.show_posts_by_author(author)

        elif choice == "4":
            print("Dastur tugadi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.")


# Dastur ishga tushirish
if __name__ == "__main__":
    main()

#4. Qo‘shimcha imkoniyatlar:
#Postni o‘chirish
#Postni tahrirlash
#Eng so‘nggi postlarni ko‘rsatish

# Post Class (Maqola)
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        print(f"\nSarlavha: {self.title}")
        print(f"Matn: {self.content}")
        print(f"Muallif: {self.author}")


# Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def show_all_posts(self):
        if not self.posts:
            print("\nHozircha postlar yo‘q.")
        else:
            for i, post in enumerate(self.posts, 1):
                print(f"\n[{i}]")
                post.display_post()

    def show_posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author == author:
                post.display_post()
                found = True
        if not found:
            print(f"\n{author} tomonidan yozilgan postlar topilmadi.")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts.pop(index)
            print("✅ Post o‘chirildi.")
        else:
            print("❌ Noto‘g‘ri indeks.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content
            print("✅ Post tahrirlandi.")
        else:
            print("❌ Noto‘g‘ri indeks.")

    def show_latest_posts(self, count=3):
        if not self.posts:
            print("\nHozircha postlar yo‘q.")
        else:
            print(f"\nOxirgi {count} ta post:")
            for post in self.posts[-count:]:
                post.display_post()


# Asosiy dastur (CLI)
def main():
    blog = Blog()

    while True:
        print("\n--- BLOG TIZIMI ---")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlarni ko‘rish")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. Eng so‘nggi postlarni ko‘rsatish")
        print("7. Chiqish")

        choice = input("Tanlang (1-7): ")

        if choice == "1":
            title = input("Sarlavha: ")
            content = input("Matn: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("✅ Post qo‘shildi!")

        elif choice == "2":
            blog.show_all_posts()

        elif choice == "3":
            author = input("Muallif ismini kiriting: ")
            blog.show_posts_by_author(author)

        elif choice == "4":
            blog.show_all_posts()
            index = int(input("O‘chirish uchun post raqamini tanlang: ")) - 1
            blog.delete_post(index)

        elif choice == "5":
            blog.show_all_posts()
            index = int(input("Tahrirlash uchun post raqamini tanlang: ")) - 1
            new_title = input("Yangi sarlavha: ")
            new_content = input("Yangi matn: ")
            blog.edit_post(index, new_title, new_content)

        elif choice == "6":
            blog.show_latest_posts()

        elif choice == "7":
            print("Dastur tugadi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.")


# Dastur ishga tushirish
if __name__ == "__main__":
    main()

#5. Sinov (Test):
#Post qo‘shib, metodlarni sinab ko‘rish

# === Sinov (Test) ===
def test_blog():
    blog = Blog()

    # 1. Post qo‘shish
    post1 = Post("Python darsi", "Bugun class o‘rgandik", "Ali")
    post2 = Post("Sport yangiliklari", "Messi gol urdi!", "Vali")
    post3 = Post("Kitob tavsiyasi", "Alkimyogar kitobi juda qiziq", "Ali")
    post4 = Post("Film", "Titanic juda zo‘r edi", "Hasan")

    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)
    blog.add_post(post4)

    print("\n--- 1. Barcha postlar ---")
    blog.show_all_posts()

    # 2. Muallif bo‘yicha
    print("\n--- 2. Ali yozgan postlar ---")
    blog.show_posts_by_author("Ali")

    # 3. Postni o‘chirish
    print("\n--- 3. Ikkinchi postni o‘chiramiz ---")
    blog.delete_post(1)  # (0-indeksdan boshlanadi)
    blog.show_all_posts()

    # 4. Postni tahrirlash
    print("\n--- 4. Birinchi postni tahrir qilamiz ---")
    blog.edit_post(0, "Python Advanced", "Bugun inheritance haqida o‘rgandik")
    blog.show_all_posts()

    # 5. Eng so‘nggi 3 post
    print("\n--- 5. Oxirgi 3 ta post ---")
    blog.show_latest_posts()


# Sinovni ishga tushirish
if __name__ == "__main__":
    test_blog()

#III.Oddiy Bank Tizimi
#1. Account Class (Hisob Classi):
#Hisob raqami (account number)
#Egasi (account holder)
#Balans (balance)

# Account Class (emojilar yo'q, toza kod)
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: miqdor musbat bo'lishi kerak!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: yetarli mablag' yo'q yoki noto'g'ri summa!")

    def __str__(self):
        return f"Hisob raqami: {self.account_number}, Egasi: {self.account_holder}, Balans: {self.balance}"


# Sinov (test) — bu ham emojisiz
if __name__ == "__main__":
    acc1 = Account("12345", "Ali", 1000)
    print(acc1)
    acc1.deposit(500)
    acc1.withdraw(300)
    print("Joriy balans:", acc1.get_balance())

# Natija (shuni kodga emas, komment sifatida qo'ying):
# Hisob raqami: 12345, Egasi: Ali, Balans: 1000
# 500 so'm qo'shildi. Yangi balans: 1500
# 300 so'm yechildi. Yangi balans: 1200
# Joriy balans: 1200


#2. Bank Class (Bank Classi):
#Hisob qo‘shish
#Balansni tekshirish
#Pul qo‘yish (deposit)
#Pul yechish (withdraw)

# Account Class
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: miqdor musbat bo'lishi kerak!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: yetarli mablag' yo'q yoki noto'g'ri summa!")

    def __str__(self):
        return f"Hisob raqami: {self.account_number}, Egasi: {self.account_holder}, Balans: {self.balance}"


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # hisob raqamlarini saqlash

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"{account.account_holder} uchun hisob qo'shildi.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Balans: {account.get_balance()} so'm")
        else:
            print("Bunday hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Bunday hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Bunday hisob topilmadi!")


# Sinov (Test)
if __name__ == "__main__":
    # Bank yaratamiz
    my_bank = Bank("Milliy Bank")

    # Hisoblar yaratamiz
    acc1 = Account("111", "Ali", 1000)
    acc2 = Account("222", "Vali", 2000)

    # Hisoblarni bankka qo'shamiz
    my_bank.add_account(acc1)
    my_bank.add_account(acc2)

    # Amallarni sinash
    my_bank.check_balance("111")
    my_bank.deposit("111", 500)
    my_bank.withdraw("111", 700)

    my_bank.check_balance("222")
    my_bank.withdraw("222", 3000)  # xatolik, yetarli mablag‘ yo‘q

#3. Asosiy Dastur (CLI):
#Hisob qo‘shish
#Balansni tekshirish
#Pul qo‘yish
#Pul yechish

# Account Class
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: miqdor musbat bo'lishi kerak!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: yetarli mablag' yo'q yoki noto'g'ri summa!")

    def __str__(self):
        return f"Hisob raqami: {self.account_number}, Egasi: {self.account_holder}, Balans: {self.balance}"


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"{account.account_holder} uchun hisob qo'shildi.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Balans: {account.get_balance()} so'm")
        else:
            print("Bunday hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Bunday hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Bunday hisob topilmadi!")


# Asosiy Dastur (CLI)
if __name__ == "__main__":
    my_bank = Bank("Milliy Bank")

    while True:
        print("\n--- Bank Tizimi ---")
        print("1. Hisob qo'shish")
        print("2. Balansni tekshirish")
        print("3. Pul qo'yish")
        print("4. Pul yechish")
        print("5. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-5): ")

        if tanlov == "1":
            raqam = input("Hisob raqamini kiriting: ")
            egasi = input("Hisob egasini kiriting: ")
            boshlangich = float(input("Boshlang'ich balans: "))
            account = Account(raqam, egasi, boshlangich)
            my_bank.add_account(account)

        elif tanlov == "2":
            raqam = input("Hisob raqamini kiriting: ")
            my_bank.check_balance(raqam)

        elif tanlov == "3":
            raqam = input("Hisob raqamini kiriting: ")
            miqdor = float(input("Qo'yiladigan summa: "))
            my_bank.deposit(raqam, miqdor)

        elif tanlov == "4":
            raqam = input("Hisob raqamini kiriting: ")
            miqdor = float(input("Yechiladigan summa: "))
            my_bank.withdraw(raqam, miqdor)

        elif tanlov == "5":
            print("Dastur tugadi.")
            break

        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

#Qo‘shimcha imkoniyatlar:
#Pul o‘tkazish (transfer)
#Hisob tafsilotlarini ko‘rsatish
#Overdraft (hisobda mablag‘ yetmasa) bilan ishlash

# Account Class
class Account:
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.overdraft_limit = overdraft_limit  # qarz limiti

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: miqdor musbat bo'lishi kerak!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Xatolik: miqdor musbat bo'lishi kerak!")
            return

        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: Mablag' yetarli emas va overdraft limiti oshib ketdi!")

    def __str__(self):
        return (f"Hisob raqami: {self.account_number}, "
                f"Egasi: {self.account_holder}, "
                f"Balans: {self.balance}, "
                f"Overdraft limiti: {self.overdraft_limit}")


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"{account.account_holder} uchun hisob qo'shildi.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Balans: {account.get_balance()} so'm")
        else:
            print("Bunday hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Bunday hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Bunday hisob topilmadi!")

    def transfer(self, from_acc, to_acc, amount):
        account_from = self.accounts.get(from_acc)
        account_to = self.accounts.get(to_acc)

        if account_from and account_to:
            if amount > 0 and account_from.balance + account_from.overdraft_limit >= amount:
                account_from.withdraw(amount)
                account_to.deposit(amount)
                print(f"{amount} so'm {from_acc} dan {to_acc} ga o‘tkazildi.")
            else:
                print("Xatolik: mablag' yetarli emas yoki noto‘g‘ri summa!")
        else:
            print("Hisoblardan biri topilmadi!")

    def show_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Bunday hisob topilmadi!")


# Asosiy Dastur (CLI)
if __name__ == "__main__":
    my_bank = Bank("Milliy Bank")

    while True:
        print("\n--- Bank Tizimi ---")
        print("1. Hisob qo'shish")
        print("2. Balansni tekshirish")
        print("3. Pul qo'yish")
        print("4. Pul yechish")
        print("5. Pul o‘tkazish")
        print("6. Hisob tafsilotlarini ko‘rsatish")
        print("7. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-7): ")

        if tanlov == "1":
            raqam = input("Hisob raqamini kiriting: ")
            egasi = input("Hisob egasini kiriting: ")
            boshlangich = float(input("Boshlang'ich balans: "))
            overdraft = float(input("Overdraft limitini kiriting (qarz limiti): "))
            account = Account(raqam, egasi, boshlangich, overdraft)
            my_bank.add_account(account)

        elif tanlov == "2":
            raqam = input("Hisob raqamini kiriting: ")
            my_bank.check_balance(raqam)

        elif tanlov == "3":
            raqam = input("Hisob raqamini kiriting: ")
            miqdor = float(input("Qo'yiladigan summa: "))
            my_bank.deposit(raqam, miqdor)

        elif tanlov == "4":
            raqam = input("Hisob raqamini kiriting: ")
            miqdor = float(input("Yechiladigan summa: "))
            my_bank.withdraw(raqam, miqdor)

        elif tanlov == "5":
            from_acc = input("Qaysi hisobdan: ")
            to_acc = input("Qaysi hisobraqamga: ")
            miqdor = float(input("O‘tkaziladigan summa: "))
            my_bank.transfer(from_acc, to_acc, miqdor)

        elif tanlov == "6":
            raqam = input("Hisob raqamini kiriting: ")
            my_bank.show_account_details(raqam)

        elif tanlov == "7":
            print("Dastur tugadi.")
            break

        else:
            print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")

#Sinov (Test):
#Hisob qo‘shib, barcha funksiyalarni sinash

# Account Class
class Account:
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: miqdor musbat bo'lishi kerak!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Xatolik: miqdor musbat bo'lishi kerak!")
            return

        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance}")
        else:
            print("Xatolik: Mablag' yetarli emas va overdraft limiti oshib ketdi!")

    def __str__(self):
        return (f"Hisob raqami: {self.account_number}, "
                f"Egasi: {self.account_holder}, "
                f"Balans: {self.balance}, "
                f"Overdraft limiti: {self.overdraft_limit}")


# Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"{account.account_holder} uchun hisob qo'shildi.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"{account.account_holder} balans: {account.get_balance()} so'm")
        else:
            print("Bunday hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Bunday hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Bunday hisob topilmadi!")

    def transfer(self, from_acc, to_acc, amount):
        account_from = self.accounts.get(from_acc)
        account_to = self.accounts.get(to_acc)

        if account_from and account_to:
            if amount > 0 and account_from.balance + account_from.overdraft_limit >= amount:
                account_from.withdraw(amount)
                account_to.deposit(amount)
                print(f"{amount} so'm {from_acc} dan {to_acc} ga o‘tkazildi.")
            else:
                print("Xatolik: mablag' yetarli emas yoki noto‘g‘ri summa!")
        else:
            print("Hisoblardan biri topilmadi!")

    def show_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Bunday hisob topilmadi!")


# TEST QISMI
if __name__ == "__main__":
    print("\n--- TEST REJIMI BOSHLANDI ---\n")
    bank = Bank("Test Bank")

    # 1. Hisob qo'shish
    acc1 = Account("1001", "Ali", 50000, 20000)
    acc2 = Account("1002", "Vali", 30000, 10000)
    bank.add_account(acc1)
    bank.add_account(acc2)

    # 2. Balansni tekshirish
    bank.check_balance("1001")
    bank.check_balance("1002")

    # 3. Pul qo‘yish
    bank.deposit("1001", 20000)

    # 4. Pul yechish
    bank.withdraw("1002", 35000)  # overdraftdan foydalanadi

    # 5. Pul o‘tkazish
    bank.transfer("1001", "1002", 30000)

    # 6. Hisob tafsilotlari
    bank.show_account_details("1001")
    bank.show_account_details("1002")

    print("\n--- TEST REJIMI TUGADI ---")
