#Uyga vazifa 1
#Tarjima:

# Pandas kutubxonasidan foydalanib DataFrame yarating.

# Ustunlar: "First Name", "Age", "City".

# Ustun nomlarini funksiya yordamida qayta nomlang:
# "First Name" → "first_name", "Age" → "age".

# DataFrame’ning dastlabki 3 qatordan iborat qismini chop eting.

# Shaxslarning o‘rtacha yoshini hisoblang.

# Faqat "first_name" va "City" ustunlarini tanlab chop eting.

# Yangi "Salary" ustunini qo‘shing (random qiymatlar bilan).

# DataFrame bo‘yicha umumiy statistikani (describe()) ko‘rsating.
import pandas as pd
import numpy as np

# Ma'lumotlar
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Ustunlarni qayta nomlash
df = df.rename(columns={"First Name": "first_name", "Age": "age"})

# 1) Dastlabki 3 qator
print("Dastlabki 3 qator:\n", df.head(3))

# 2) O‘rtacha yosh
print("\nO‘rtacha yosh:", df["age"].mean())

# 3) Faqat ism va shahar
print("\nIsm va Shahar ustunlari:\n", df[["first_name", "City"]])

# 4) Yangi ustun: ish haqi
df["Salary"] = np.random.randint(4000, 8000, size=len(df))
print("\nYangi Salary ustuni qo‘shildi:\n", df)

# 5) Statistik ma'lumotlar
print("\nUmumiy statistika:\n", df.describe())

# Uyga vazifa 2
# Tarjima:

# sales_and_expenses nomli DataFrame yarating.

# Ustunlar: "Month", "Sales", "Expenses".

# Jadval:

# Jan  5000  3000
# Feb  6000  3500
# Mar  7500  4000
# Apr  8000  4500


# Maksimal, minimal va o‘rtacha (average) savdo va xarajatlarni hisoblang.
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# Maksimal qiymatlar
print("Maksimal savdo va xarajatlar:\n", sales_and_expenses[["Sales", "Expenses"]].max())

# Minimal qiymatlar
print("\nMinimal savdo va xarajatlar:\n", sales_and_expenses[["Sales", "Expenses"]].min())

# O‘rtacha qiymatlar
print("\nO‘rtacha savdo va xarajatlar:\n", sales_and_expenses[["Sales", "Expenses"]].mean())

# Uyga vazifa 3
# Tarjima:

# expenses nomli DataFrame yarating.

# Ustunlar: "Category", "January", "February", "March", "April".

# Jadval:

# Rent           1200  1300  1400  1500
# Utilities       200   220   240   250
# Groceries       300   320   330   350
# Entertainment   150   160   170   180


# Har bir kategoriya bo‘yicha: maksimal, minimal va o‘rtacha xarajatlarni hisoblang.

# .set_index("Category") metodidan foydalaning.
data = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)

# Category ni indeks qilish
expenses = expenses.set_index("Category")

# Maksimal xarajatlar
print("Maksimal xarajatlar:\n", expenses.max(axis=1))

# Minimal xarajatlar
print("\nMinimal xarajatlar:\n", expenses.min(axis=1))

# O‘rtacha xarajatlar
print("\nO‘rtacha xarajatlar:\n", expenses.mean(axis=1))
