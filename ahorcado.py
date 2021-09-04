from pantalla import*
from pyconio import*
from os import system
import random

pantalla = Pantalla()


class Ahorcado:
	def __init__(self):
		self.erroneas = []
		self.acertadas = []
		self.ListaPalabras = []
		self.cargarLista()
	
	def menuJuego(self):
		salir = False
		while(salir == False):
			system("cls")
			pantalla.dibujarMarco()
			gotoxy(19, 13)
			print("1 - PALABRA RANDOM")
			gotoxy(19, 14)
			print("2 - INGRESAR PALABRA")
			gotoxy(19, 15)
			print("3 - VOLVER")
			gotoxy(15, 17)
			print("Elija opcion:")
			gotoxy(30, 17)
			opcion = getchar()
			if opcion == "1":
				system("cls")
				self.erroneas.clear()
				self.acertadas.clear()
				palabraEnJuego = self.palabraRandom()
								
				while(self.terminoElJuego(pantalla, palabraEnJuego)):
					self.procesoJuego(palabraEnJuego)
					
				self.mensajeFinal(palabraEnJuego)
				palabraEnJuego = None
				getchar()

			elif opcion == "2":
				palabraQueSeIngreso = self.ingresarPalabra()
				if (palabraQueSeIngreso in self.ListaPalabras) == False:#cambiar x lista
					self.guardarPalabraEnArchivo(palabraQueSeIngreso)
					gotoxy(10, 18)
					print("Se agrego la palabra a la base de datos")# bajarlo 2 a la derecha 5 masomenos
				self.ListaPalabras.clear()
				self.cargarLista()
				#print(self.ListaPalabras)
				getchar()
				system("cls")
				self.erroneas.clear()
				self.acertadas.clear()
												
				while(self.terminoElJuego(pantalla, palabraQueSeIngreso)):
					self.procesoJuego(palabraQueSeIngreso)
					
				self.mensajeFinal(palabraQueSeIngreso)
				palabraQueSeIngreso = None
				getchar()
			
			elif opcion == "3":
				salir = True 

	
	def mensajeFinal(self, unaPalabra):
		getchar()
		system("cls")
		pantalla.dibujarMarco()
		gotoxy(20, 14)
		if len(self.erroneas) == 6:
			print("!!!PERDISTE¡¡¡")
		elif not self.fueDescubierta(pantalla, unaPalabra):
			print("!!!GANASTE¡¡¡")
	
	def procesoJuego(self, unaPalabra):
		pantalla.dibujarPantallaJuego(unaPalabra, self.erroneas, self.acertadas)
		gotoxy(10, 25)
		print("Ingrese una letra:")
		gotoxy(29, 25)
		letra = input().upper()
		esValida = self.letraEsValida(letra)
		if esValida == True:
			self.catalogarLetra(unaPalabra, letra)
		system("cls")	
		pantalla.dibujarPantallaJuego(unaPalabra, self.erroneas, self.acertadas)

	def terminoElJuego(self, unaPantalla, unaPalabra):
		termino = True
		if len(self.erroneas) == 6:
			termino = False
		elif not self.fueDescubierta(unaPantalla, unaPalabra):
			termino = False
		return termino

	
	def fueDescubierta(self, unaPantalla, unaPalabra):
		cantidadSecreta = unaPantalla.palabraADescubrir(unaPalabra, self.acertadas)
		guiones = []
		for i in cantidadSecreta:
			if i == "-":
				guiones.append(i)
		
		return len(guiones) != 0#TRUE

	def catalogarLetra(self, unaPalabra, unaLetra):#Todo en mayuscula
		if unaLetra in unaPalabra:
			#print("acertadas")
			self.acertadas.append(unaLetra)
		else:
			#print("erronea")
			self.erroneas.append(unaLetra)

	def palabraRandom(self):
		palabraParaJugar = random.choice(self.ListaPalabras)
		#system("cls")
		#print(palabraParaJugar)
		getchar()
		return palabraParaJugar

###OPCION 2

	def guardarPalabraEnArchivo(self, unaPalabra):
		archivo = open("estasPalabras.txt", "a")
		archivo.write(unaPalabra)
		archivo.write('\n')
		archivo.close() 

	def ingresarPalabra(self):
		verificada = False
		system("cls")
		while(verificada == False):
			pantalla.dibujarMarco()
			gotoxy(19, 14)
			print("Ingrese palabra:")
			gotoxy(19, 16)
			palabraIngresada = input().upper()
			verificada = self.verificarPalabra(palabraIngresada)
		getchar()
		return palabraIngresada

	def verificarPalabra(self, palabra):
		if not palabra.isalpha():
			system("cls")
			pantalla.dibujarMarco()
			gotoxy(14, 14)
			print("La palabra ingresada contiene")
			gotoxy(15, 15)
			print("elementos que no son letras")
			getchar()
			return False
		elif len(palabra) < 4:
			system("cls")
			pantalla.dibujarMarco()
			gotoxy(14, 14)
			print("La palabra ingresada contiene")
			gotoxy(16, 15)
			print("menos de cuatro letras")
			getchar()
			return False
		else: 
			return True

	def letraEsValida(self, letra):
		esValida = True
		if len(letra) > 1:
			gotoxy(25, 26)
			print("ingresaste mas de un caracter")
			esValida = False
			getchar()

		elif letra.isalpha() == False:
			gotoxy(25, 26)
			print("Lo ingresado no es una letra")
			esValida = False
			getchar()
		
		elif letra in self.erroneas or letra in self.acertadas: 
			gotoxy(25, 26)
			print("Ya ingresaste esta letra")
			esValida = False
			getchar()

		return esValida

	def cargarLista(self):
		archivo = open("estasPalabras.txt", 'r')
		linea = archivo.readline()
		while linea != "":
			self.ListaPalabras.append(linea.rstrip("\n"))
			linea = archivo.readline()
		archivo.close()