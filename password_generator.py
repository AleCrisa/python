import random
import string

characters = ''

lenght = int(input("Inserisci la lunghezza della password: "))
upper = bool(int(input("Premi 1 se vuoi lettere maiuscole, altrimenti premi 0: ")))
if upper:
    characters += string.ascii_uppercase 
lower = bool(int(input("Premi 1 se vuoi lettere minuscole, altrimenti peremi 0: ")))
if lower:
    characters += string.ascii_lowercase
special = bool(int(input("Premi 1 se vuoi caratteri speciali, altrimenti premi 0: ")))
if special:
    characters += string.punctuation
password = ''.join(random.choice(list(characters))for i in range (lenght))

print(f'La tua password è: {password}')