#/////Nestor Emmanuel Briones Ramirez\\\\
#-1220100321 
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

mins = mins + dura

hour = hour + mins // 60

print(hour % 24, ":", mins % 60, sep="")
