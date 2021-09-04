from pyconio import*
from os import system
import re
textcolor(Green)

class Pantalla:
	
	def pantallaInicio(self):
		self.dibujarMarco()
		self.titulo()
		self.horcaInicio()
		gotoxy(22,23)
		print(" 1 - JUGAR")
		gotoxy(22,24)
		print(" 2 - SALIR")
		gotoxy(3,26)
		
		
	def dibujarPantallaJuego(self, unaPalabra, erroneas, acertadas):
		system("cls")
		self.dibujarMarco()	
		self.tituloTablero()
		self.horcaVacia()
		self.muerto(erroneas)
		self.cajonFallidas(erroneas)
		queda = 54 - len(unaPalabra)
		espacios = queda / 2
		gotoxy(espacios, 23)
		print("".join(self.palabraADescubrir(unaPalabra, acertadas)))
		
	
################################################################	

	def dibujarMarco(self):
		self.dibujarLineaSuperior()
		self.dibujarLineasCentrales()
		self.dibujarLineaInferior()

	def dibujarLineaSuperior(self):
		print("╔", end="")
		for i in range(54):#linea superior
			print("=", end="")
		print("╗")

	def dibujarLineasCentrales(self):
		for i in range(26):#linea izquierda
			print("║                                                      ║")
		print("╚", end="")

	def dibujarLineaInferior(self):
		for i in range(54):#linea abajo
			print("=", end="")
		print("╝")

	def tituloTablero(self):
		gotoxy(24, 2)
		print("AHORCADO")
		gotoxy(2, 3)
		for i in range(54):
			print("▼", end="")

	def horcaVacia(self):
		gotoxy(22,15)
		for i in range(10):
			print("≡", end="")
		gotoxy(31,14)
		print("║")
		gotoxy(31,13)
		print("║")
		gotoxy(31,12)
		print("║")
		gotoxy(31,11)
		print("║")
		gotoxy(31,10)
		print("╗")
		gotoxy(26,10)
		print("=")
		gotoxy(27,10)
		print("=")
		gotoxy(28,10)
		print("=")
		gotoxy(29,10)
		print("=")
		gotoxy(30,10)
		print("=")
		gotoxy(25,10)
		print("╔")

	def cajonFallidas(self, erroneas):
		gotoxy(2, 18)
		for i in range(54):
			print("►", end="")
		gotoxy(2, 20)
		for i in range(54):
			print("◄", end="")
		gotoxy(20, 19)
		if(len(erroneas) > 0):
			j = 0
			for j in range (len(erroneas)):
				print(erroneas[j], end=" ")

	def muerto(self, erroneas):
		if len(erroneas) == 1:
			gotoxy(25,11)
			print("O")
		if len(erroneas) == 2:
			gotoxy(25,11)
			print("O")
			gotoxy(25,12)
			print("|")
		if len(erroneas) == 3:
			gotoxy(25,11)
			print("O")
			gotoxy(24,12)
			print("ʃ|")
		if len(erroneas) == 4:
			gotoxy(25,11)
			print("O")
			gotoxy(24,12)
			print("ʃ|ʅ")
		if len(erroneas) == 5:
			gotoxy(25,11)
			print("O")
			gotoxy(24,12)
			print("ʃ|ʅ")
			gotoxy(24, 13)
			print("ʃ")
		if len(erroneas) == 6:
			gotoxy(25,11)
			print("O")
			gotoxy(24,12)
			print("ʃ|ʅ")
			gotoxy(24, 13)
			print("ʃ ʅ")

	def palabraADescubrir(self, unaPalabra, acertadas):
		secreta = ["-"]*len(unaPalabra)
		if len(acertadas) > 0:
			for i in acertadas:
				#print(i)
				for c in re.finditer(i, unaPalabra, re.IGNORECASE):
     					secreta[c.start()] = c.group()
     					#print("".join(secreta))
		return secreta
	

	def horcaInicio(self):
		gotoxy(22,21)
		for i in range(10):
			print("≡", end="")
		gotoxy(31,20)
		print("║")
		gotoxy(31,19)
		print("║")
		gotoxy(31,18)
		print("║")
		gotoxy(31,17)
		print("║")
		gotoxy(31,16)
		print("╗")
		gotoxy(26,16)
		print("=")
		gotoxy(27,16)
		print("=")
		gotoxy(28,16)
		print("=")
		gotoxy(29,16)
		print("=")
		gotoxy(30,16)
		print("=")
		gotoxy(25,16)
		print("╔")
		
		gotoxy(25, 17)
		print("O")
		gotoxy(24, 18)
		print("ʃ|ʅ")
		gotoxy(24, 19)
		print("ʃ ʅ")

	def titulo(self):
		gotoxy(20, 6)
		print("███ █ █ ███ ██▄")
		gotoxy(20, 7)
		print("█ █ █ █ █ █ █ █")
		gotoxy(20, 8)
		print("███ ███ █ █ ██▄")
		gotoxy(20, 9)
		print("█ █ █ █ ███ █ █")

		gotoxy(20, 11)
		print("███ ███ ██▄ ███")
		gotoxy(20, 12)
		print("█   █ █ █ █ █ █")
		gotoxy(20, 13)
		print("█   ███ █ █ █ █")
		gotoxy(20, 14)
		print("███ █ █ ██▀ ███")

