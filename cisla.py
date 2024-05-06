import random

def vygeneruj_nahodnou_delku():
    delka = random.randint(1, 50)
    cisla = [random.randint(1, 50) for i in range(5)]
    return cisla
  
cisla = vygeneruj_nahodnou_delku()

print("-------------------------------------------------")
print("Vygenerovaná délka je : ", cisla)
print("-------------------------------------------------")