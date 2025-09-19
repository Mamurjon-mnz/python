#1) Yangi ma’lumotlar bazasi yarating va unda Roster nomli jadval bo‘lsin. Jadvalda uchta ustun bo‘lishi kerak: Name (Ism), Species (Tur) va Age (Yosh). Name va Species ustunlari matn (text) turida, Age ustuni esa butun son (integer) turida bo‘lsin.
import sqlite3

# 1) Yangi ma'lumotlar bazasi yaratish
conn = sqlite3.connect(":memory:")  # vaqtinchalik xotirada DB
cursor = conn.cursor()

# Jadval yaratish
cursor.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")


# 2) Jadvalni qiymatlar bilan to‘ldirish

data = [
    ("Benjamin Sisko", "Inson", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)
conn.commit()

# 3) Jadzia Dax ismini Ezri Dax ga yangilash
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()
# 4) Bajoran turi bo‘yicha Ism va Yosh ustunlarini chiqarish
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

print("Bajoran turi odamlari:")
for row in results:
    print(row)

# Ulashni yopamiz
conn.close()
