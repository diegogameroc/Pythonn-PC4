from pyfiglet import Figlet
import random
Figlet=Figlet()


while True:
    try:
        opcion=int(input("Ingrese una opcion: "))
        if(opcion==1):
            fuente=input("Ingrese una fuente porfavor: ")
            Figlet.setFont(font=fuente)
            texto=input("Ingrese un texto porfavor :")
            print(Figlet.renderText(texto))
            break
        if(opcion==2):
            # Fuente aleatoria...
            Figlet.setFont(font=random.choice(Figlet.getFonts()))
            texto=input("Ingrese un texto porfavor :")
            print(Figlet.renderText(texto))
            break
    except ValueError:
        print("Ingrese un valor válido")

