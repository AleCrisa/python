mass = float(input("Inserisci il tuo peso in kg: "))
heigth = float(input("Inserisci la tua altezza in m: "))
bmi = mass / (heigth **2)
print(f'Il tuo indice di massa corporea è: {bmi}')

if bmi <18.5:
    print('Sei sottopeso')
elif bmi >=18.5 and bmi<25:
    print('Sei normopeso')
elif bmi >=25 and bmi<30:
    print('Sei sovrappeso')
else:
    print('Sei obeso')