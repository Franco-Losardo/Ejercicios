# print(number for number in a if number in b and number not in c)
# print([number for number in list if number < userNumber])
while True:
    user1 = input("¿Cual es tu nombre? ")
    user2 = input("¿Cual es tu nombre? ")

    user1_option = input("%s, ¿qué elegis: piedra, papel o tijera? " % user1)
    user2_option = input("%s, ¿qué elegis: piedra, papel o tijera? " % user2)

    def compare(u1, u2):
        if user1_option == user2_option:
            return("Es un empate")

        elif user1_option == "piedra":
            if user2_option == "papel":
                return(user2, "ganó")
            else:
                return(user1, "ganó")

        elif user1_option == "papel":
            if user2_option == "tijera":
                return(user2, "ganó")
            else:
                return(user1, "ganó")

        elif user1_option == "tijera":
            if user2_option == "piedra":
                return(user2, "ganó")
            else:
                return(user1, "ganó")
        else:
            print("La opción ingresada es incorrecta")

    print(compare(user1_option, user2_option))

    repetir = input("Ingresa ""si"" para jugar otra vez, presiona cualquier tecla para salir ")
    if repetir == "si":
        continue
    else:
        break
