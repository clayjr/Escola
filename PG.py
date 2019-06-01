n = int(input("Informe quantos elementos ira somar na PG: "))
r = float(input("Informe a razao entre os elementos: "))
primeiroelemento = float(input("Informe o primeiro elemento: "))

total = 0
pg = 1
print("Os termos da progressao sao: ")
print(primeiroelemento)
for i in range(1, n):
    pg = pg * r
    print(pg) 
    total = total + pg

print("O total da PG e: ", total+primeiroelemento)
