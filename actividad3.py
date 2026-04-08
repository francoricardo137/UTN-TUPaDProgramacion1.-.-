#actvidad 1 
nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras (sin espacios).")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad_str = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("Error: debe ingresar un número entero positivo mayor a cero.")
    cantidad_str = input("Ingrese la cantidad de productos a comprar: ")
cantidad = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
    print(f"\nProducto {i}")
    
    precio_str = input("Precio: ")
    while not precio_str.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio_str = input("Precio: ")
    precio = int(precio_str)
    
    descuento = input("¿Tiene descuento? (S/N): ")
    while descuento not in ('S', 's', 'N', 'n'):
        print("Error: responda con 'S' o 'N'.")
        descuento = input("¿Tiene descuento? (S/N): ")
    
    if descuento == 'S' or descuento == 's':
        precio_con_descuento = precio * 0.9
    else:
        precio_con_descuento = precio
    
    total_sin_descuento += precio
    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n" + "="*30)
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
#actividad 2
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

while intentos < 3 and not acceso:
    intentos += 1
    print(f"Intentó {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada")
else:
    opcion = 0
    while opcion != 4:
        print("\n1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")
        opcion_str = input("Opción: ")
        if not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            continue
        opcion = int(opcion_str)
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue
        
        if opcion == 1:
            print("Inscrito")
        elif opcion == 2:
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirmar nueva clave: ")
                if nueva == confirmacion:
                    clave_correcta = nueva
                    print("Clave cambiada exitosamente.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("¡Sigue adelante, tú puedes!")
    print("Saliendo del sistema...")

#actividad 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")
while not operador.isalpha():
    print("Error: solo letras.")
    operador = input("Ingrese nombre del operador: ")

opcion = 0
while opcion != 5:
    print("\n--- Menú Agenda ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opc_str = input("Opción: ")
    if not opc_str.isdigit():
        print("Error: ingrese un número.")
        continue
    opcion = int(opc_str)
    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    if opcion == 1:
        print("Días: 1 = Lunes, 2 = Martes")
        dia_str = input("Elija día: ")
        if not dia_str.isdigit():
            print("Error: debe ser número.")
            continue
        dia = int(dia_str)
        if dia not in (1, 2):
            print("Error: día inválido.")
            continue

        nombre_pac = input("Nombre del paciente (solo letras): ")
        while not nombre_pac.isalpha():
            print("Error: solo letras.")
            nombre_pac = input("Nombre del paciente: ")

        if dia == 1:
            if nombre_pac in (lunes1, lunes2, lunes3, lunes4):
                print("Error: el paciente ya tiene turno el lunes.")
                continue
            if lunes1 == "":
                lunes1 = nombre_pac
                print("Turno reservado (Lunes, Turno 1).")
            elif lunes2 == "":
                lunes2 = nombre_pac
                print("Turno reservado (Lunes, Turno 2).")
            elif lunes3 == "":
                lunes3 = nombre_pac
                print("Turno reservado (Lunes, Turno 3).")
            elif lunes4 == "":
                lunes4 = nombre_pac
                print("Turno reservado (Lunes, Turno 4).")
            else:
                print("No hay cupos disponibles para el lunes.")
        else:
            if nombre_pac in (martes1, martes2, martes3):
                print("Error: el paciente ya tiene turno el martes.")
                continue
            if martes1 == "":
                martes1 = nombre_pac
                print("Turno reservado (Martes, Turno 1).")
            elif martes2 == "":
                martes2 = nombre_pac
                print("Turno reservado (Martes, Turno 2).")
            elif martes3 == "":
                martes3 = nombre_pac
                print("Turno reservado (Martes, Turno 3).")
            else:
                print("No hay cupos disponibles para el martes.")

    elif opcion == 2:
        print("Días: 1 = Lunes, 2 = Martes")
        dia_str = input("Elija día: ")
        if not dia_str.isdigit():
            print("Error: debe ser número.")
            continue
        dia = int(dia_str)
        if dia not in (1, 2):
            print("Error: día inválido.")
            continue

        nombre_pac = input("Nombre del paciente a cancelar: ")
        while not nombre_pac.isalpha():
            print("Error: solo letras.")
            nombre_pac = input("Nombre del paciente: ")

        if dia == 1:
            if lunes1 == nombre_pac:
                lunes1 = ""
                print("Turno cancelado (Lunes, Turno 1).")
            elif lunes2 == nombre_pac:
                lunes2 = ""
                print("Turno cancelado (Lunes, Turno 2).")
            elif lunes3 == nombre_pac:
                lunes3 = ""
                print("Turno cancelado (Lunes, Turno 3).")
            elif lunes4 == nombre_pac:
                lunes4 = ""
                print("Turno cancelado (Lunes, Turno 4).")
            else:
                print("No se encontró un turno con ese nombre el lunes.")
        else:
            if martes1 == nombre_pac:
                martes1 = ""
                print("Turno cancelado (Martes, Turno 1).")
            elif martes2 == nombre_pac:
                martes2 = ""
                print("Turno cancelado (Martes, Turno 2).")
            elif martes3 == nombre_pac:
                martes3 = ""
                print("Turno cancelado (Martes, Turno 3).")
            else:
                print("No se encontró un turno con ese nombre el martes.")

    elif opcion == 3:
        print("Días: 1 = Lunes, 2 = Martes")
        dia_str = input("Elija día: ")
        if not dia_str.isdigit():
            print("Error: debe ser número.")
            continue
        dia = int(dia_str)
        if dia == 1:
            print("\n--- Agenda Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 else '(libre)'}")
        elif dia == 2:
            print("\n--- Agenda Martes ---")
            print(f"Turno 1: {martes1 if martes1 else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 else '(libre)'}")
        else:
            print("Día inválido.")

    elif opcion == 4:
        ocup_lun = 0
        if lunes1 != "": ocup_lun += 1
        if lunes2 != "": ocup_lun += 1
        if lunes3 != "": ocup_lun += 1
        if lunes4 != "": ocup_lun += 1
        libres_lun = 4 - ocup_lun

        ocup_mar = 0
        if martes1 != "": ocup_mar += 1
        if martes2 != "": ocup_mar += 1
        if martes3 != "": ocup_mar += 1
        libres_mar = 3 - ocup_mar

        print("\n--- Resumen General ---")
        print(f"Lunes: {ocup_lun} ocupados, {libres_lun} libres")
        print(f"Martes: {ocup_mar} ocupados, {libres_mar} libres")

        if ocup_lun > ocup_mar:
            print("Día con más turnos: Lunes")
        elif ocup_mar > ocup_lun:
            print("Día con más turnos: Martes")
        else:
            print("Empate: ambos días tienen la misma cantidad de turnos.")

print("Sistema cerrado.")
#actividad 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

nombre = input("Ingrese nombre del agente: ")
while not nombre.isalpha():
    print("Error: solo letras.")
    nombre = input("Ingrese nombre del agente: ")

print(f"\nBienvenido, agente {nombre}. Debes abrir 3 cerraduras antes de quedarte sin energía o tiempo.")
print("¡Cuidado con la alarma!\n")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n=== Estado ===")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}")
    if alarma:
        print("*** ALARMA ACTIVADA ***")
    print("=" * 30)

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    opcion_str = input("Elige una opción (1-3): ")

    if not opcion_str.isdigit():
        print("Error: debe ingresar un número.")
        continue
    opcion = int(opcion_str)
    if opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango (1-3).")
        continue

    if opcion == 1:
        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            alarma = True
            print("\n¡Has forzado tres veces seguidas! La cerradura se trabó y la alarma se activó.")
            print("No se abrió ninguna cerradura.")
            forzar_seguidas = 0
        else:
            energia_antes = energia + 20
            if energia_antes < 40:
                print("\n¡Advertencia! La energía está baja. Intentar forzar podría activar la alarma.")
                num_str = input("Ingresa un número entre 1 y 3 para intentar desactivar el sensor: ")
                while not num_str.isdigit():
                    print("Error: debe ser un número.")
                    num_str = input("Ingresa un número entre 1 y 3: ")
                num = int(num_str)
                while num < 1 or num > 3:
                    print("Error: número fuera de rango (1-3).")
                    num_str = input("Ingresa un número entre 1 y 3: ")
                    while not num_str.isdigit():
                        print("Error: debe ser un número.")
                        num_str = input("Ingresa un número entre 1 y 3: ")
                    num = int(num_str)
                if num == 3:
                    alarma = True
                    print("¡Has elegido 3! La alarma se activa.")
                else:
                    cerraduras_abiertas += 1
                    print("¡Has forzado la cerradura con éxito! Una cerradura abierta.")
            else:
                cerraduras_abiertas += 1
                print("¡Has forzado la cerradura! Una cerradura abierta.")

        print(f"Has perdido 20 de energía y 2 de tiempo.")

    elif opcion == 2:
        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo del panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}: código parcial = {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡El código alcanzó 8 caracteres! Se ha abierto una cerradura automáticamente.")
        else:
            print("El hackeo no logró abrir una cerradura esta vez.")
        print(f"Has perdido 10 de energía y 3 de tiempo.")

    elif opcion == 3:
        forzar_seguidas = 0

        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma está activada, pierdes 10 de energía adicional.")
        print(f"Has recuperado energía. Nueva energía: {energia}. Tiempo restante: {tiempo}.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n*** BLOQUEO POR ALARMA ***")
        print("La seguridad del sistema se ha activado y te ha bloqueado. Misión fallida.")
        break

if cerraduras_abiertas == 3:
    print("\n" + "="*40)
    print(f"¡VICTORIA! Agente {nombre}, has abierto las 3 cerraduras.")
    print("La bóveda está abierta. ¡Misión cumplida!")
elif energia <= 0:
    print("\nTe has quedado sin energía. Misión fallida.")
elif tiempo <= 0:
    print("\nSe acabó el tiempo. Misión fallida.")
elif alarma and tiempo <= 3:
    print("\nMisión fallida por bloqueo de alarma.")
else:
    print("\nEl juego ha terminado inesperadamente.")

# Ejercicio 5 — “Escape Room: La Arena del Gladiador”

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo_base = 12
turno_jugador = True

print(f"=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0 and turno_jugador:
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion_str = input("Opción: ")
    while not opcion_str.isdigit():
        print("Error: Ingrese un número válido.")
        opcion_str = input("Opción: ")
    opcion = int(opcion_str)
    while opcion < 1 or opcion > 3:
        print("Error: Opción fuera de rango (1-3).")
        opcion_str = input("Opción: ")
        while not opcion_str.isdigit():
            print("Error: Ingrese un número válido.")
            opcion_str = input("Opción: ")
        opcion = int(opcion_str)

    if opcion == 1:
        daño = ataque_pesado_base
        if vida_enemigo < 20:
            daño = daño * 1.5
        vida_enemigo -= daño
        if daño == int(daño):
            print(f"¡Atacaste al enemigo por {int(daño)} puntos de daño!")
        else:
            print(f"¡Atacaste al enemigo por {daño:.1f} puntos de daño!")

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(f"> Golpe conectado por 5 de daño")
        print(">> Ráfaga completada.")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Usaste una poción. Recuperaste 30 HP. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    if vida_enemigo <= 0:
        break

    print(f"¡El enemigo te atacó por {ataque_enemigo_base} puntos de daño!")
    vida_jugador -= ataque_enemigo_base

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")