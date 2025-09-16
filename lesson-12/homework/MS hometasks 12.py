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

