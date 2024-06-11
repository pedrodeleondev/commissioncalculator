nombre=input("¿Cuál es tu nombre?: ")
ventas=int(input("¿Cuál es el número total de tus ventas?: "))

comisiones_ganadas=round(ventas*0.13,2)

print(f"Hola {nombre}, lo que vas a ganar este mes es ${comisiones_ganadas}.")