#3. txt nomli string saqlovchi o'zgaruvchi berilgan. txtdagi har uchinchi belgidan
#  keyin pastki chiziqcha qo'yilishi kerak. Agar belgi unli harf yoki orqasidan
#  osti chiziqcha qo'yilgan bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. 
# Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha bo'lsa qo'yilmasin.

txt = "Huperizeingno"

def chiziqcha_qoish(txt):
    unlilar = "aeiouAEIOU"
    natija = ""
    count = 0
    skip_next = False  

    for i, ch in enumerate(txt):
        natija += ch
        count += 1

        if skip_next:
            if i != len(txt) - 1:   
                natija += "_"
            skip_next = False
            count = 0
            continue

        if count == 3:
            if ch in unlilar:  
                skip_next = True
            else:      
                if i != len(txt) - 1:
                    natija += "_"
            count = 0

    return natija


natija = chiziqcha_qoish(txt)
print(natija)
# Рўйхатлардаги умумий бўлмаган элементларни қайтаринг (тартиби муҳим эмас).
# berilgan: list1=[1,1,2], list2=[2,3,4]
# natija: [1,1,3,4]
list1=[1,1,2]
list2=[2,3,4]
def uncommon_elements(list1, list2):
    natija = []

    for x in list1:
        if x not in list2:
            natija.append(x)

    for y in list2:
        if y not in list1:
            natija.append(y)

    return natija


print(uncommon_elements(list1, list2))

list1=[1,2,3]
list2=[4,5,6]
def uncommon_elements(list1, list2):
    natija = []

    for x in list1:
        if x not in list2:
            natija.append(x)

    for y in list2:
        if y not in list1:
            natija.append(y)

    return natija


print(uncommon_elements(list1, list2))
list1=[1,1,2,3,4,2]
list2=[1,3,4,5]
def uncommon_elements(list1, list2):
    natija = []

    for x in list1:
        if x not in list2:
            natija.append(x)

    for y in list2:
        if y not in list1:
            natija.append(y)

    return natija


print(uncommon_elements(list1, list2))
