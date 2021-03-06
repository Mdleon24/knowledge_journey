
def validar(tablero):
	for i in range(len(tablero)): #valida si se gana en fila
		if(tablero[i][0]==tablero[i][1] and tablero[i][1]==tablero[i][2]):
			if(tablero[i][0]=='x'): #se verifica quien puede ganar
				return +10           #+10 si gana la I.A
			elif(tablero[i][0]=='o'):
				return -10			 #-10 si gana el humano

	for i in range(len(tablero)): #valida si se gana en columna
		if(tablero[0][i]==tablero[1][i] and tablero[1][i]==tablero[2][i]):
			if(tablero[0][i]=='x'):
				return +10
			elif(tablero[0][i]=='o'):
				return -10

	if(tablero[0][0]==tablero[1][1] and tablero[1][1]==tablero[2][2]): #valida si se gana en diagonal
		if(tablero[0][0]=='x'):
			return +10
		elif(tablero[0][0]=='o'):
			return -10

	if(tablero[0][2]==tablero[1][1] and tablero[1][1]==tablero[2][0]): #valida si se gana en diagonal
		if(tablero[0][2]=='x'):
			return +10
		elif(tablero[0][2]=='o'):
			return -10
	return 0			#0 si la jugada es un empate


##Para validar si es empate##
def tableroLleno(tablero):
	for i in range(len(tablero)):
		for j in range(len(tablero)):
			if tablero[i][j]==' ':
				return True
	return False

def determinarMejorMovimiento(tablero):
	mejor= -1000
	#x,y = -1,-1
	profundidad = celdasVacias(tablero)
	for i in range(len(tablero)):
		for j in range(len(tablero)):
			if tablero[i][j]==' ':
				tablero[i][j] = 'x'
				mov_valor = minimax(tablero,1,False)
				tablero[i][j] = ' '
				if(mov_valor>mejor):
					x,y = i,j
					mejor = mov_valor
	#print("El mejor mov es", mejor,x,y)
	return x,y

def minimax(tablero,profundidad,bandera):
	#print("Nivel",profundidad)
	maquina = 'x'
	jugador = 'o'
	valor = validar(tablero)
	#print(valor)
	x = -1000
	y = -1000
	if valor == +10:
		return 10-profundidad
	if valor == -10:
		return -10 + profundidad

	if tableroLleno(tablero) == False:
		return 0

	if bandera: #si es maximizador
		#colocar la 'x' en las posiciones disponibles
		mov = -1000
		for i in range(len(tablero)):
			for j in range(len(tablero)):
				if tablero[i][j] == ' ':
					tablero[i][j] = maquina
					#print("x,y,score",i,j,valor)
					#imprimirTablero(tablero)
					mov = max(mov,minimax(tablero,profundidad+1,not bandera))
					tablero[i][j] = ' '
		return mov
	else: #si es minimizador
		#colocar la 'o' en las posiciones disponibles
		mov = +1000
		for i in range(len(tablero)):
			for j in range(len(tablero)):
				if tablero[i][j] == ' ':
					tablero[i][j] = jugador
					#print("x,y score",i,j,valor)
					#imprimirTablero(tablero)
					mov = min(mov,minimax(tablero,profundidad+1,not bandera))
					tablero[i][j] = ' '
		return mov

def celdasVacias(tablero):
	celdas = []
	for i in range(len(tablero)):
		for j in range(len(tablero)):
			if tablero[i][j] == ' ':
				celdas.append([i, j])
	return len(celdas)

def jugadorIA(tablero,):
	i,j = determinarMejorMovimiento(tablero)
	tablero[i][j] = 'x'
	imprimirTablero(tablero)

def jugadorHumano(tablero):
	coordenada = ''
	bandera = False
	validos = [0,1,2]
	while not bandera:
		print("Ingrese las coordenadas:")
		coordenada = input()
		try:
			coordenada = coordenada.split(',')
			i = int(coordenada[0])
			j = int(coordenada[1])
			if tablero[i][j] != ' ':
				print("Casilla ocupada")
			elif(i not in validos or j not in validos):
				print("Ingresar coordenada válida")
			else:
				tablero[i][j] = 'o'
				bandera = True
				imprimirTablero(tablero)
		except:
			print("Ingrese valor válido")
		



def main():
	tablero=[[" " , " " , " "],
		 	 [" " , " " , " "],
		 	 [" " , " " , " "]]

	
	#imprimirTablero(tablero)
	jugador = "o"
	maquina ="x" 
	print("--------")
	print("x - I.A")
	print("o - Humano")
	print("--------")
	print()
	jugando = True
	#mejor_movimiento = determinarMejorMovimiento(tablero)
	#while(jugando):
		#if(validar(tablero) == +10):
		#	print("Perdiste!")
		#elif(validar(tablero) == -10):
		#	print("Ganaste!")
		#else:

	imprimirTablero(tablero)
	primero_iniciar = ''
	while primero_iniciar != 'Y' and primero_iniciar != 'N':
		try:
			primero_iniciar = input('Quiere iniciar el juego?[y/n]: ').upper()
		except (KeyError, ValueError):
			print('Error')

	##Ciclo del juego##
	while celdasVacias(tablero) > 0 and not validar(tablero) == +10 and not validar(tablero) == -10:
		if primero_iniciar == 'N':
			jugadorIA(tablero)
			primero_iniciar = ''
		jugadorHumano(tablero)
		if(celdasVacias(tablero) > 0):
			jugadorIA(tablero)

	##Mensajes##
	if (validar(tablero) == +10):
		print("Perdiste!")
	elif(validar(tablero) == -10):
		print("Ganaste!")
	else:
		print("Empate!")

	exit()


def imprimirTablero(tablero):
	print("      0    1    2")
	print("0    " +  tablero[0][0] +  "  |  " + tablero[0][1]  + "  |  " + tablero[0][2])
	print("     -------------")
	print("1    " +  tablero[1][0] +  "  |  " + tablero[1][1]  + "  |  " + tablero[1][2])
	print("     -------------")
	print("2    " +  tablero[2][0] +  "  |  " + tablero[2][1]  + "  |  " + tablero[2][2])
	print()



main()