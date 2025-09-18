
import math_operations as mo
import string_utils as su

print("Qo‘shish:", mo.add(5, 3))
print("Ayirish:", mo.subtract(10, 4))
print("Ko‘paytirish:", mo.multiply(6, 7))
print("Bo‘lish:", mo.divide(8, 2))

print("Teskari satr:", su.reverse_string("Salom"))
print("Unlilar soni:", su.count_vowels("Assalomu alaykum"))



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Xatolik: nolga bo‘lib bo‘lmaydi!"
    return a / b



def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, txt):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(txt)

import math


def calculate_area(radius):
    return (radius**2)*2*math.pi

def calculate_circumference(radius):
    return radius*2*math.pi

