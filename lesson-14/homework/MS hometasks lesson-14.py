#Vazifa 1: JSON faylni o‘qish
#students.json faylini o‘qib, undagi har bir talabaning ma’lumotlarini ekranga chiqaradigan Python dastur yozing.

import json

# students.json faylini o‘qish
with open("students14.json", "r", encoding="utf-8") as f:
    students14= json.load(f)

# Har bir talabaning ma’lumotini chiqarish
for student in students14:
    print(f"Ism: {student['name']}, Yosh: {student['age']}, Kurs: {student['course']}")

#Vazifa 2: Ob-havo API
#Ushbu manzildan foydalaning: https://openweathermap.org/
#requests kutubxonasidan foydalanib, ma’lum bir shahar (masalan, sizning shahringiz: Toshkent) uchun ob-havo ma’lumotlarini olib keling va muhim ma’lumotlarni (harorat, namlik va boshqalar) ekranga chiqaring.

#Ob-havo API (Toshkent)
import requests

API_KEY = "df51284c2f7f301d30d8bb78b5936a1e"  # bu yerga haqiqiy API kalitingizni yozing
city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=uz"


response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Shahar: {data['name']}")
    print(f"Harorat: {data['main']['temp']}°C")
    print(f"Namlik: {data['main']['humidity']}%")
    print(f"Ob-havo: {data['weather'][0]['description']}")
else:
    print("Xatolik yuz berdi:", data.get("message", "Noma’lum xatolik"))

#Vazifa 3: JSONni o‘zgartirish
#books.json faylida foydalanuvchiga yangi kitob qo‘shish, mavjud kitob ma’lumotlarini yangilash va kitoblarni o‘chirish imkonini beradigan dastur yozing.

import json

# Fayldan ma’lumotlarni o‘qish
def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # agar fayl topilmasa bo‘sh ro‘yxat qaytadi

# Faylga saqlash
def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

# Kitob qo‘shish
def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print(f"✅ Kitob qo‘shildi: {title} - {author}")

# Kitobni yangilash
def update_book(old_title, new_title, new_author):
    books = load_books()
    updated = False
    for book in books:
        if book["title"] == old_title:
            book["title"] = new_title
            book["author"] = new_author
            updated = True
            break
    save_books(books)
    if updated:
        print(f"✏️ Kitob yangilandi: {old_title} → {new_title}")
    else:
        print(f"⚠️ '{old_title}' nomli kitob topilmadi!")

# Kitobni o‘chirish
def delete_book(title):
    books = load_books()
    new_books = [book for book in books if book["title"] != title]
    if len(new_books) != len(books):
        save_books(new_books)
        print(f"🗑️ Kitob o‘chirildi: {title}")
    else:
        print(f"⚠️ '{title}' nomli kitob topilmadi!")

# --- Namuna ishlatish ---
add_book("Sun’iy Intellekt", "Ali Valiyev")
update_book("Algoritmlar", "Algoritmlar va Ma’lumotlar tuzilmasi", "Zulaykho Karimova")
delete_book("Python Asoslari")
#Vazifa 4: Kino tavsiya qilish tizimi
#Ushbu manzildan foydalaning: http://www.omdbapi.com/
#Foydalanuvchidan film janrini so‘rab, shu janr bo‘yicha tasodifiy filmni tavsiya qiladigan dastur yozing.

import requests
import random

API_KEY = "SIZNING_API_KEY"  # OMDb API kalitingizni shu yerga yozing

def get_movie_by_genre(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
    response = requests.get(url)
    data = response.json()
    
    if "Search" in data:
        movie = random.choice(data["Search"])
        print("🎬 Kino tavsiyasi:")
        print(f"Nom: {movie['Title']}")
        print(f"Yil: {movie['Year']}")
        print(f"IMDB ID: {movie['imdbID']}")
    else:
        print("⚠️ Kino topilmadi. Boshqa janr kiriting!")

# --- Namuna ishlatish ---
genre = input("Qaysi janrdagi filmni xohlaysiz? (masalan: action, drama, comedy): ")
get_movie_by_genre(genre)
