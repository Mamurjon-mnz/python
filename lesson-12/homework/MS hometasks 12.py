#Mashq 1: Iplar yordamida tub sonlarni tekshirish
#Python dasturi yozing: berilgan sonlar oralig‘ida tub sonlar bor-yo‘qligini tekshirsin. Oralig‘ni bir nechta ip (thread) ga bo‘lib oling va har bir ip o‘ziga tegishli qismdagi sonlarni tekshirsin. Dastur oxirida asosiy qism topilgan barcha tub sonlarni ro‘yxat qilib chiqarsin.

import threading

# Tub sonni tekshiruvchi funksiya
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Iplar bajaradigan funksiya
def check_primes(start, end, result):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result.extend(primes)

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4  # nechta ip ishlatamiz

    threads = []
    results = []
    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step - 1 if i < num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes, args=(start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results.sort()
    print("Tub sonlar:", results)

#Mashq 2: Iplar yordamida faylni qayta ishlash
#Katta matnli faylni o‘qiydigan dastur yozing (har qatorida matn bor). Iplardan foydalanib, fayldagi so‘zlarning nechta marta uchrashganini sanang. Har bir ip faylning o‘ziga tegishli qismini ishlovchi bo‘lsin. Dastur oxirida barcha iplar natijasini birlashtirib, so‘zlarning umumiy uchrashish sonini ekranga chiqarsin.

#Mashq 2: Threaded File Processing
import threading
from collections import Counter

# Har bir ip bajaradigan funksiya
def count_words(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)

if __name__ == "__main__":
    filename = "sample.txt"  # katta fayl nomi
    num_threads = 4
    counters = []

    # Faylni o‘qish
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    step = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], counters))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Natijalarni birlashtirish
    final_counter = Counter()
    for c in counters:
        final_counter.update(c)

    print("So‘zlar soni:")
    for word, count in final_counter.items():
        print(word, ":", count)
