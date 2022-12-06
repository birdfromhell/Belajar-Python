teman = open('teman.txt', 'w')
tanya = input("Nama : ")
teman.write(tanya)
a = int(input("Lagi ? "))

i = 1
while a == i:
    teman.write("\n")
    tanya = input("Nama : ")
    teman.write(tanya)
    a = int(input("Lagi ? "))

