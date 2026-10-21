aylar = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"]
for i in aylar:
    print(i)

bos_setir = [1, 2, 3, 4, 5, None, None, None, None, None]

aylar[6] = "dilqem"
print(aylar[6])

class Node:
    def __init__(self, ad, qiymet):
        self.ad = ad         
        self.qiymet = qiymet  
        self.next = None     
        self.prev = None   

duyun = Node(None, 65)
duyunn = Node(None, 65)
duyunnn = Node(None, 65)
duyunnnn = Node("dilqem", 65)
duyunnnnn = Node("dilqem", 65)


duyun.next = duyunn
duyunn.next = duyunnn
duyunnn.next = duyunnnn
duyunnnn.next = duyunnnnn


duyunn.prev = duyun
duyunnn.prev = duyunn
duyunnnn.prev = duyunnn
duyunnnnn.prev = duyunnnn



print("ireli getdikce")
cari = duyun
son = None
while cari is not None:
    print(f"ad: {cari.ad}, qiymet: {cari.qiymet}")
    son = cari  
    cari = cari.next

print("\ndala qayitdiqda")
cari = son
while cari is not None:
    print(f"ad: {cari.ad}, qiymet: {cari.qiymet}")
    cari = cari.prev