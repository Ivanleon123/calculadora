# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b == 0:
        return "Error: No es pot dividir per zero."
    return a / b

def convertir_base(num, base):
    if base == 'bin':
        return bin(int(num))
    elif base == 'oct':
        return oct(int(num))
    elif base == 'hex':
        return hex(int(num))
    elif base == 'dec':
        return str(num)
    else:
        return "Base no vàlida."

def calculadora():
    print("Benvingut a la calculadora!")
    print("Operacions disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Conversió de bases")

    while True:
        try:
            operacio = input("Tria l'operació (1/2/3/4/5) o 'q' per sortir: ")

            if operacio == 'q':
                print("Sortint de la calculadora. Adéu!")
                break

            if operacio in ['1', '2', '3', '4']:
                num1 = float(input("Introdueix el primer número: "))
                num2 = float(input("Introdueix el segon número: "))

                if operacio == '1':
                    print(f"Resultat: {suma(num1, num2)}")
                elif operacio == '2':
                    print(f"Resultat: {resta(num1, num2)}")
                elif operacio == '3':
                    print(f"Resultat: {multiplicacio(num1, num2)}")
                elif operacio == '4':
                    print(f"Resultat: {divisio(num1, num2)}")
            elif operacio == '5':
                num = float(input("Introdueix un número: "))
                base = input("Introdueix la base (bin, oct, hex, dec): ").strip().lower()
                resultat = convertir_base(num, base)
                print(f"Resultat: {resultat}")
            else:
                print("Operació no vàlida. Torna a provar.")
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")

if __name__ == "__main__":
    calculadora()
