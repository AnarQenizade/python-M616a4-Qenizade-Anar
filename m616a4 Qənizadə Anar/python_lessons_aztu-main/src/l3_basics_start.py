# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
print("=== Kərpic 1 ===")
# Bu sətir şərhdie: Python onu icra etmir, bu - insan üçün qeyddir
print("Salam, data mühəndisliyi!")
print("Baza sansiyası:", "BAK-0207")
print(2+3)
print("2+3")
print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops
print("=== Kərpic 2 ===")
cell = "BAK-0207"
rsrp = -95.5
print(cell, rsrp)

rsrp = -108.1
print(cell, rsrp)

drops = 2
drops = drops + 1
print("drops =", drops)

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»
print("=== Kərpic 3 ===")
print(type(3))
print(type(-95.5))
print(type("BAK-0207"))
print(type(True))
print(type(None))
print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==

# ad = input("adınızı daxil edin")
# soyad = input("soyadınızı daxil edin")
# yaşım = input ("yaşınızı daxil edin")
# yaşım = int(yaşım)+1
# print("menim adim", ad , "soyadim", soyad, "bir il sonra yasim", yaşım)

# print(yaşım<25)
# print(yaşım>25)

print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta

deyisen_list = [-91.5, -108.1, -86.2, -103.3, -97.4]
input1= int(input ("elementin nomresini sec"))

print("sizin element", deyisen_list[input1-1])


print("=== Kərpic 6 ===")   # Lüğət (dict)
# TODO: row = {...}, row["region"]

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# TODO: zəif ölçmələri saymaq

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
