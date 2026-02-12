import random
import time
print("AVENTURA")
nombre = input("Ingresa tu nombre: ")
print("\nElige tu clase:")
print("1. Guerrero (Más vida)")
print("2. Mago (Más ataque)")
print("3. Explorador (Balanceado)")
opcion = input("Selecciona (1-3): ")
if opcion == "1":
    clase = "Guerrero"
    vida = 120
    ataque = 15
elif opcion == "2":
    clase = "Mago"
    vida = 80
    ataque = 25
elif opcion == "3":
    clase = "Explorador"
    vida = 100
    ataque = 18
else:
    clase = "Aventurero"
    vida = 100
    ataque = 15
vida_max = vida
inventario = []
tipos_objetos = []
contador_turnos = 0
print(f"\nBienvenido {nombre} el {clase}")
print(f"Vida: {vida} | Ataque: {ataque}")
inicio = time.time()
def combate():
    global vida
    enemigo_vida = random.randint(40, 100)
    enemigo_ataque = random.randint(8, 18)
    print("\n⚔ ¡Un enemigo aparece!")
    print(f"Vida del enemigo: {enemigo_vida}")
    while enemigo_vida > 0 and vida > 0:
        print("\n1. Atacar")
        accion = input("Elige acción: ")
        if accion == "1":
            daño = random.randint(ataque - 5, ataque + 5)
            enemigo_vida -= daño
            print(f"Le haces {daño} de daño.")
            if enemigo_vida > 0:
                daño_enemigo = random.randint(enemigo_ataque - 3, enemigo_ataque + 3)
                vida -= daño_enemigo
                print(f"El enemigo te hace {daño_enemigo} de daño.")
                print(f"Tu vida actual: {vida}")
        else:
            print("Solo puedes atacar.")
    if vida <= 0:
        print("\n Has sido derrotado...")
        return False
    else:
        print("\n Enemigo derrotado!")
        return True
while vida > 0:
    print("\n------ MENÚ ------")
    print("1. Buscar objeto")
    print("2. Ver inventario")
    print("3. Salir del juego")
    decision = input("Elige opción: ")
    if decision == "1":
        contador_turnos += 1
        evento = random.randint(1, 100)
        if evento <= 40:
            resultado = combate()
            if not resultado:
                break
        numero = random.randint(1, 100)
        if numero < 30:
            tipo = "Común"
        elif 30 <= numero <= 70:
            tipo = "Raro"
        else:
            tipo = "Legendario"
        inventario.append(numero)
        tipos_objetos.append(tipo)
        print(f"\n Encontraste un objeto {tipo} (valor {numero})")
    elif decision == "2":
        print("\n INVENTARIO:")
        if len(inventario) == 0:
            print("Vacío.")
        else:
            for i in range(len(inventario)):
                print(f"{i+1}. {tipos_objetos[i]} - {inventario[i]}")
    elif decision == "3":
        print("\nHas decidido salir del juego.")
        break
    else:
        print("Opción inválida.")
fin = time.time()
tiempo_total = round(fin - inicio, 2)
print("\n RESUMEN FINAL ")
print(f"Jugador: {nombre}")
print(f"Clase: {clase}")
print(f"Vida final: {vida}")
print(f"Objetos recolectados: {len(inventario)}")
print(f"Turnos jugados: {contador_turnos}")
print(f"Tiempo jugado: {tiempo_total} segundos")
print("\nTipos de objetos obtenidos:")
for i in range(len(tipos_objetos)):
    print(f"- {tipos_objetos[i]} ({inventario[i]})")
print("\nGracias por jugar")
