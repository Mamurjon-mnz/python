#Yosh hisoblagich: Foydalanuvchidan tug‘ilgan sanasini kiritishini so‘rang. Yil, oy va kunlarda yoshini hisoblab chiqib ekranga chiqaring.
import datetime

# 1. Yosh hisoblagich
def age_calculator():
    birthdate = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = datetime.date.today()
    
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day
    
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12
    
    print(f"Siz {years} yil, {months} oy, {days} kun yashagansiz.")

# 🔹 Funksiyani tashqarida chaqirish kerak
age_calculator()

#Keyingi tug‘ilgan kunga qadar qolgan kunlar: Foydalanuvchidan tug‘ilgan kunini kiritishini so‘rang va keyingi tug‘ilgan kunigacha qolgan kunlarni hisoblab chiqib ekranga chiqaring.
# 2. Keyingi tug‘ilgan kunga qadar qolgan kunlar
import datetime

def days_until_birthday():
    birthdate = input("Tug‘ilgan kuningizni kiriting (MM-DD): ")
    today = datetime.date.today()
    
    month, day = map(int, birthdate.split("-"))
    this_year_birthday = datetime.date(today.year, month, day)
    
    if this_year_birthday < today:
        this_year_birthday = datetime.date(today.year + 1, month, day)
    
    days_left = (this_year_birthday - today).days
    print(f"Keyingi tug‘ilgan kuningizga {days_left} kun qoldi.")

# 🔹 Funksiyani ishga tushirish
days_until_birthday()

#Uchrashuv rejalashtirgich: Foydalanuvchidan joriy sana va vaqtni hamda uchrashuv davomiyligini (soat va daqiqalarda) kiritishini so‘rang. Uchrashuv tugaydigan sana va vaqtni hisoblab chiqib ekranga chiqaring.
import datetime

def meeting_scheduler(now_str, duration_str):
    # Sana va vaqtni parse qilish
    now = datetime.datetime.strptime(now_str, "%Y-%m-%d %H:%M")
    
    # Soat va daqiqalarni ajratib olish
    hours, minutes = map(int, duration_str.split(","))
    
    # Yakuniy vaqtni hisoblash
    end_time = now + datetime.timedelta(hours=hours, minutes=minutes)
    
    return end_time.strftime('%Y-%m-%d %H:%M')


# 🔹 Funksiyani chaqirish (input() o‘rniga bevosita parametr beriladi)
natija = meeting_scheduler("2025-09-16 18:30", "2,15")
print("Uchrashuv tugaydigan vaqt:", natija)

#Vaqt zonalari konvertori: Foydalanuvchidan sana va vaqtni, shuningdek, joriy vaqt zonasini kiritishini so‘rang va tanlagan boshqa vaqt zonasiga o‘girib ekranga chiqaring.
# timezone_converter.py
from datetime import datetime
try:
    # Python 3.9+ uchun: tavsiya etilgan
    from zoneinfo import ZoneInfo
except Exception as e:
    raise RuntimeError("Sizda Python 3.9+ kerak (zoneinfo mavjud emas). Yoki pytz o'rnatib, kodni moslashtiring.") from e

def parse_datetime(text):
    """Turli formatlarni qabul qiladi:
       YYYY-MM-DD HH:MM:SS
       YYYY-MM-DD HH:MM
       YYYY-MM-DD
    """
    text = text.strip()
    formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"]
    for fmt in formats:
        try:
            dt = datetime.strptime(text, fmt)
            # agar faqat sana bo'lsa, vaqtini 00:00:00 qilib qo'yamiz
            if fmt == "%Y-%m-%d":
                dt = dt.replace(hour=0, minute=0, second=0)
            return dt
        except ValueError:
            continue
    raise ValueError("Sana/vaqt formati noto'g'ri. Ruxsat etilgan: 'YYYY-MM-DD', 'YYYY-MM-DD HH:MM' yoki 'YYYY-MM-DD HH:MM:SS'.")

def convert_timezone(dt_str, from_zone_str, to_zone_str):
    """
    dt_str: sana/vaqt matni (yuqoridagi formatlardan biri)
    from_zone_str, to_zone_str: misol uchun 'Asia/Tashkent', 'Europe/London', 'UTC'
    """
    dt = parse_datetime(dt_str)
    try:
        from_zone = ZoneInfo(from_zone_str)
    except Exception as e:
        raise ValueError(f"'{from_zone_str}' vaqt zonasi topilmadi. Masalan: 'Asia/Tashkent', 'Europe/London', 'UTC'.") from e
    try:
        to_zone = ZoneInfo(to_zone_str)
    except Exception as e:
        raise ValueError(f"'{to_zone_str}' vaqt zonasi topilmadi. Masalan: 'Asia/Tashkent', 'Europe/London', 'UTC'.") from e

    # joriy (naive) datetimega timezone qo'shamiz
    dt_with_tz = dt.replace(tzinfo=from_zone)
    converted = dt_with_tz.astimezone(to_zone)
    return converted

# --- CLI wrapper (Jupyter/Notebook uchun parametrli chaqirishni ham qo'llab-quvvatlaydi) ---
def run_interactive():
    print("Vaqt zonalari konvertori")
    print("Kiritish formatlari: 'YYYY-MM-DD', 'YYYY-MM-DD HH:MM' yoki 'YYYY-MM-DD HH:MM:SS'")
    dt_str = input("Sana va vaqtni kiriting: ").strip()
    from_zone = input("Joriy vaqt zonasi (masalan: Asia/Tashkent): ").strip()
    to_zone = input("O‘giriladigan vaqt zonasi (masalan: Europe/London): ").strip()

    try:
        result = convert_timezone(dt_str, from_zone, to_zone)
        # chiroyli chiqarish: sana, vaqt, zona nomi va offset
        print("O‘girilgan vaqt:", result.strftime("%Y-%m-%d %H:%M:%S %Z %z"))
    except Exception as e:
        print("Xato:", e)

# Agar fayl to'g'ridan-to'g'ri ishlatilsa, run_interactive() ni chaqirishni mumkin:
if __name__ == "__main__":
    # Eslatma: Jupyter/Notebook ichida input() bilan muammo bo'lishi mumkin.
    # Shuning uchun agar Notebookda ishlatayotgan bo'lsang, quydagi misolni to'g'ridan-to'g'ri chaqir:
    # print(convert_timezone("2025-09-16 18:00", "Asia/Tashkent", "Europe/London"))
    run_interactive()
#Qaytim sanog‘i (Countdown Timer): Foydalanuvchidan kelajakdagi sana va vaqtni kiritishini so‘rang va har soniyada qolgan vaqtni ekranga chiqarib boring.
import datetime
import time

def countdown_timer():
    # 🔹 Foydalanuvchidan sana va vaqtni olish
    target_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
    target_time = datetime.datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

    print("⏳ Qaytim sanog‘i boshlandi...\n")

    while True:
        now = datetime.datetime.now()
        remaining = target_time - now

        if remaining.total_seconds() <= 0:
            print("\n⏰ Vaqt tugadi!")
            break

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Natijani chiqarish
        print(f"\rQolgan vaqt: {days} kun {hours:02d}:{minutes:02d}:{seconds:02d}", end="")

        time.sleep(1)  # Har 1 sekundda yangilanadi


# 🔹 Funksiyani ishga tushirish
countdown_timer()

#Email tekshirgich: Foydalanuvchidan email manzilini kiritishini so‘rang va u to‘g‘ri formatda yozilganmi yoki yo‘q, shuni tekshirib bering.
import re

def email_validator():
    email = input("Email manzilingizni kiriting: ")

    # Oddiy email regex
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

    if re.match(pattern, email):
        print("✅ Email manzilingiz to‘g‘ri formatda yozilgan.")
    else:
        print("❌ Email manzilingiz noto‘g‘ri formatda yozilgan.")


# 🔹 Funksiyani ishga tushirish
email_validator()

#Telefon raqamini formatlash: Foydalanuvchidan telefon raqamini kiritishini so‘rang va uni standart formatga keltiring. Masalan: "1234567890" → "(123) 456-7890".
import re

def phone_formatter():
    phone = input("Telefon raqamingizni kiriting (faqat raqamlar): ")

    # faqat raqamlarni olish
    digits = re.sub(r'\D', '', phone)

    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print("✅ Formatlangan raqam:", formatted)
    else:
        print("❌ Telefon raqam 10 ta raqamdan iborat bo‘lishi kerak.")


# 🔹 Funksiyani ishga tushirish
phone_formatter()
#Parol mustahkamligini tekshirgich: Foydalanuvchidan parol kiritishini so‘rang va parol quyidagi mezonlarga javob beradimi-yo‘qmi, tekshiring: minimal uzunlik, kamida bitta katta harf, bitta kichik harf va bitta raqam.
import re

def password_strength_checker():
    password = input("Parol kiriting: ")

    # Minimal uzunlik
    if len(password) < 8:
        print("❌ Parol kamida 8 ta belgidan iborat bo‘lishi kerak.")
        return

    # Katta harf tekshirish
    if not re.search(r"[A-Z]", password):
        print("❌ Parolda kamida bitta katta harf bo‘lishi kerak.")
        return

    # Kichik harf tekshirish
    if not re.search(r"[a-z]", password):
        print("❌ Parolda kamida bitta kichik harf bo‘lishi kerak.")
        return

    # Raqam tekshirish
    if not re.search(r"[0-9]", password):
        print("❌ Parolda kamida bitta raqam bo‘lishi kerak.")
        return

    print("✅ Parol mustahkam!")


# 🔹 Funksiyani ishga tushirish
password_strength_checker()

#So‘z topuvchi: Foydalanuvchidan bir so‘z kiritishini so‘rang va berilgan matndan shu so‘zning barcha uchrashuvlarini topib ekranga chiqaring.
import re

def word_finder():
    text = """Python — bu kuchli dasturlash tili.
    Python dasturlash tili juda mashhur va oson o‘rganiladi.
    Ko‘plab dasturchilar Python tilidan foydalanadi."""
    
    print("Matn:\n", text, "\n")
    
    word = input("Qaysi so‘zni qidirmoqchisiz? ")
    
    # So‘zlarni qidirish (katta-kichik harflarni farqlamaydi)
    matches = re.findall(rf"\b{re.escape(word)}\b", text, flags=re.IGNORECASE)
    
    if matches:
        print(f"✅ '{word}' so‘zi {len(matches)} marta uchradi.")
    else:
        print(f"❌ '{word}' so‘zi topilmadi.")


# 🔹 Funksiyani ishga tushirish
word_finder()

#Sanalarni ajratib oluvchi: Foydalanuvchidan matn kiritishini so‘rang va ichidagi barcha sanalarni topib ekranga chiqaring.
import re

def date_extractor():
    text = input("Matn kiriting: ")

    # Turli xil sana formatlari uchun regex
    pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}\.\d{2}\.\d{4}\b"

    dates = re.findall(pattern, text)

    if dates:
        print("✅ Matndan topilgan sanalar:")
        for d in dates:
            print("-", d)
    else:
        print("❌ Matndan sana topilmadi.")


# 🔹 Funksiyani ishga tushirish
date_extractor()
