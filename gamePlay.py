from pyconio import *
from pantalla import*
from ahorcado import*
from os import system

bucleJuego = True
pantalla = Pantalla()
ahorcado = Ahorcado()

while(bucleJuego == True):
	system("cls")
	pantalla.pantallaInicio()
	print("Elija opcion:")
	gotoxy(18,26)
	opcion = getchar()

	if opcion == "1":
		system("cls")
		ahorcado.menuJuego()
		#system("PAUSE")
		
	elif opcion == "2":
		bucleJuego = False




