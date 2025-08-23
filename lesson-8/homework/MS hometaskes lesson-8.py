# Istisnolar bo‘yicha mashqlar:
#1.	Nolga bo‘lishda ZeroDivisionError xatosini ushlab qoladigan Python dasturini yozing.

try:
    x = 387/ 0
except ZeroDivisionError:
    print("Error: Nolga bo‘lish mumkin emas!")
#2.Foydalanuvchidan butun son kiritishni so‘rab, noto‘g‘ri qiymat kiritilsa ValueError xatosini ko‘rsatadigan Python dasturini yozing.
try:
    n = int(input("Butun son kiriting: "))
    print("Siz kiritgan son:", n)
except ValueError:
    print("Xato: Faqat butun son kiriting!")
#3.Faylni ochishga harakat qilib, agar fayl mavjud bo‘lmasa FileNotFoundError xatosini ushlab qoladigan Python dasturini yozing.
try:
    f = open("mustaqil_fayl.txt")
except FileNotFoundError:
    print("Error: Fayl topilmadi!")
#4.	Foydalanuvchidan ikkita son kiritishni so‘rab, son bo‘lmagan qiymat kiritilsa TypeError xatosini ko‘rsatadigan Python dasturini yozing.
try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")
    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Faqat son kiriting!")
    print("Yig‘indi:", int(a) + int(b))
except TypeError as e:
    print("Xato:", e)


#5.	Faylni ochishga harakat qilib, agar ruxsat muammosi bo‘lsa PermissionError xatosini ushlab qoladigan Python dasturini yozing.
try:
    with open("C:\\Windows\\System32\\test.txt", "w") as f:
        f.write("Salom!")
except PermissionError:
    print("Error: Sizda ushbu faylga ruxsat yo‘q!")

#6.	Ro‘yxat (list) ustida amal bajarib, agar indeks diapazondan tashqarida bo‘lsa IndexError xatosini ushlab qoladigan Python dasturini yozing.
my_list = [10, 20, 30, 40, 50]

try:
        print(my_list[100])
except IndexError:
    print("Xato: Siz murojaat qilgan indeks ro‘yxat chegarasidan tashqarida!")
#7.	Foydalanuvchidan son kiritishni so‘rab, foydalanuvchi kiritishni bekor qilsa KeyboardInterrupt xatosini ushlab qoladigan Python dasturini yozing
try:
    son = int(input("Son kiriting: "))
    print("Siz kiritgan son:", son)
except KeyboardInterrupt:
    print("\nXato: Kiritish bekor qilindi (Ctrl+C bosildi)!")
except ValueError:
    print("Xato: Faqat butun son kiriting!")
#8.	Bo‘lish amalini bajarib, arifmetik xato bo‘lsa ArithmeticError xatosini ushlab qoladigan Python dasturini yozing.
try:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    natija = a / b
    print("Natija:", natija)
except ArithmeticError:
    print("Xato: Arifmetik amal bajarib bo‘lmadi (masalan, 0 ga bo‘lish)!")
except ValueError:
    print("Xato: Faqat butun son kiriting!")

#9.	Faylni ochib, kodlash (encoding) muammosi bo‘lsa UnicodeDecodeError xatosini ushlab qoladigan Python dasturini yozing.
try:
    with open("test.txt", "r", encoding="utf-8") as f:
        matn = f.read()
    print("Fayldan o‘qilgan matn:", matn)
except UnicodeDecodeError:
    print("Xato: Fayl kodlash muammosi (UnicodeDecodeError)!")
except FileNotFoundError:
    print("Xato: Fayl topilmadi!")

#10.	Ro‘yxat ustida amal bajarib, mavjud bo‘lmagan atributga murojaat qilinganda AttributeError xatosini ushlab qoladigan Python dasturini yozing.
my_list = [1, 2, 3]

try:
    my_list.push(4)
except AttributeError:
    print("Xato: Ro‘yxatda bunday atribut yoki metod mavjud emas!")

# Python’da Fayl Kiritish/Chiqarish: Mashqlar, Amaliyot va Yechimlar
#Fayl bilan ishlash mashqlari:

#1.	Butun matnli faylni o‘qiydigan Python dasturini yozing.
with open("matn.txt", "r") as f:
    data = f.read()

print(data)
#2.	Faylning dastlabki n qatorini o‘qiydigan Python dasturini yozing.
def read_daslabki_n_qator(matnfayl, n):
    with open(matnfayl, "r") as f:
        for i in range(n):
            line = f.readline()   
            if not line:          
                break
            print(line, end="")


read_daslabki_n_qator("matnfayl.txt", 5)

#3.	Faylga matn qo‘shib, so‘ng qo‘shilgan matnni ko‘rsatadigan Python dasturini yozing.
with open("matn.txt", "a") as f: 
    f.write(", lekin ayrim joylari qiyin kechyabdi.") 

with open("matn.txt", "r") as f:
    print(f.read())


#4.	Faylning oxirgi n qatorini o‘qiydigan Python dasturini yozing.
def read_last_n_lines(filename, n):
    with open(filename, "r") as f:
        lines = f.readlines()   
        last_lines = lines[-n:] 
        for line in last_lines:
            print(line, end="")


read_last_n_lines("matn.txt", 1)   
#5.	Faylni qatorma-qator o‘qib, ro‘yxatga joylaydigan Python dasturini yozing.
def file_to_list(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line.strip()) 
    return lines


result = file_to_list("matn.txt")
print(result)

#6.	Faylni qatorma-qator o‘qib, bitta o‘zgaruvchiga joylaydigan Python dasturini yozing.
with open("matn.txt", "r") as f:
    matn = ""
    for line in f:
        matn += line  

print(matn)

#7.	Faylni qatorma-qator o‘qib, massivga joylaydigan Python dasturini yozing.
with open("matn.txt", "r") as f:
    massiv = [line.strip() for line in f]  

print(massiv)

# 8.Fayldan eng uzun so‘zlarni topadigan Python dasturini yozing.
def find_longest_words(filename):
    with open(filename, "r") as f:
        text = f.read()              
        words = text.split()        
        max_len = max(len(w) for w in words) 
        longest_words = [w for w in words if len(w) == max_len]
        return longest_words


result = find_longest_words("matn.txt")
print("Eng uzun so‘z(lar):", result)

#9.	Matnli fayldagi qatorlar sonini hisoblaydigan Python dasturini yozing.
def count_lines(filename):
    with open(filename, "r") as f:
        count = sum(1 for _ in f) 
    return count


soni = count_lines("matn.txt")
print("Fayldagi qatorlar soni:", soni)

#10.Fayldagi so‘zlarning chastotasini (necha marta ishlatilganini) hisoblaydigan Python dasturini yozing.
def word_frequency(filename):
    with open(filename, "r") as f:
        text = f.read().lower()          
        words = text.split()             
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1 
        return freq


natija = word_frequency("matn.txt")
print("So‘z chastotalari:")
for soz, soni in natija.items():
    print(soz, "->", soni)

#11.Oddiy matnli fayl hajmini topadigan Python dasturini yozing.
import os


def file_size(filename):
    return os.path.getsize(filename)  


hajm = file_size("matn.txt")
print("Fayl hajmi:", hajm, "bayt")

#12.Ro‘yxatni faylga yozadigan Python dasturini yozing.
def write_list_to_file(filename, data):
    with open(filename, "w") as f:
        for item in data:
            f.write(str(item) + "\n") 


my_list = ["Salom", "Python", 123, "Dasturlash"]
write_list_to_file("matn1.txt", my_list)

print("Ro‘yxat faylga yozildi!")

#13.Fayldagi ma’lumotlarni boshqa faylga nusxa qiladigan Python dasturini yozing.
def copy_file(src, dest):
    with open(src, "r") as f1:       
        data = f1.read()
    with open(dest, "w") as f2:      
        f2.write(data)


copy_file("matn1.txt", "nusxa.txt")
print("Fayl nusxalandi!")

# 14. Birinchi fayldagi har bir qatorni ikkinchi fayldagi mos keladigan qator bilan birlashtiradigan Python dasturini yozing.
def merge_files(file1, file2, outfile):
    with open(file1, "r", encoding="utf-8") as f1, \
         open(file2, "r", encoding="utf-8") as f2, \
         open(outfile, "w", encoding="utf-8") as out:
        
        # zip ikkala fayldan ham bir xil tartibda qator oladi
        for line1, line2 in zip(f1, f2):
            out.write(line1.strip() + " " + line2.strip() + "\n")

# Foydalanish
merge_files("fayl1.txt", "fayl2.txt", "birlashtirilgan_file.txt")
print("✅ Fayllar birlashtirildi!")
#15.	Fayldan tasodifiy bir qatorni o‘qiydigan Python dasturini yozing.
import random

def random_line(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()   # barcha qatorlarni ro‘yxatga olamiz
    return random.choice(lines).strip()  # tasodifiy bittasini tanlaymiz


print("Tasodifiy qator:", random_line("matn1.txt"))

#16.	Fayl yopilganmi yoki yo‘qmi tekshiradigan Python dasturini yozing.
f = open("matn.txt", "r", encoding="utf-8")

# Tekshiramiz
print("Fayl yopilganmi?", f.closed)  # ❌ False (ochiq)

# Faylni yopamiz
f.close()

# Yana tekshiramiz
print("Fayl yopilganmi?", f.closed)  # ✅ True (yopiq)

#17.Fayldagi yangi qator belgilarini olib tashlaydigan Python dasturini yozing
def remove_newlines(infile, outfile):
    with open(infile, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # har bir qator oxiridan \n belgisini olib tashlaymiz
    clean_lines = [line.strip() for line in lines]

    # yangi faylga yozamiz
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(" ".join(clean_lines))  # qatorlarni bitta matn qilib yozadi


remove_newlines("matn1.txt", "tozalangan.txt")
print("Yangi qator belgilar olib tashlandi!")

#18.Matnli faylni kiritma sifatida qabul qilib, undagi so‘zlar sonini qaytaradigan Python dasturini yozing.
def remove_newlines(infile, outfile):
    with open(infile, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # har bir qator oxiridan \n belgisini olib tashlaymiz
    clean_lines = [line.strip() for line in lines]

    # yangi faylga yozamiz
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(" ".join(clean_lines))  # qatorlarni bitta matn qilib yozadi

# Foydalanish
remove_newlines("matn1.txt", "tozalangan.txt")
print("Yangi qator belgilar olib tashlandi!")

#19.Turli matnli fayllardan belgilarni ajratib olib, ro‘yxatga joylaydigan Python dasturini yozing.
def chars_from_files(files):
    belgi_royxat = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            matn = f.read()
            for belgi in matn:     # har bir belgini olish
                belgi_royxat.append(belgi)
    return belgi_royxat


# Foydalanish
fayllar = ["matn1.txt", "matn2.txt", "matn3.txt"]
natija = chars_from_files(fayllar)

#20.	A.txt, B.txt, … Z.txt nomli 26 ta matnli fayl yaratadigan Python dasturini yozing.
import string

# Alfavit harflari bo‘yicha fayllar yaratish
for harf in string.ascii_uppercase:  # A, B, C, ... Z
    filename = f"{harf}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Bu fayl {harf}.txt nomli fayldir.\n")

print("✅ 26 ta fayl yaratildi: A.txt dan Z.txt gacha")
