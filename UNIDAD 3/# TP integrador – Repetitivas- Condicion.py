#  TP integrador – Repetitivas- Condicionales y Secuenciales.
# GIARROSSOS_GIULIANO
# DNI:47.175.619

#--------------------------------------------------------------------

# Ejercicio 1 -- "Caja del Kiosco"
# Simula una compra con validaciones y calculo de total.

# --- Pedir nombre del cliente (solo letras, no vacio) ---
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: el nombre solo puede contener letras y no puede estar vacio.")
    nombre = input("Cliente: ")

# --- Pedir cantidad de productos (entero positivo) ---
cantidad_texto = input("Cantidad de productos: ")
while not cantidad_texto.isdigit() or int(cantidad_texto) <= 0:
    print("Error: ingrese un numero entero mayor a 0.")
    cantidad_texto = input("Cantidad de productos: ")
cantidad = int(cantidad_texto)

total_sin_descuento = 0
total_con_descuento = 0.0

# --- Por cada producto ---
for i in range(1, cantidad + 1):
    precio_texto = input(f"Producto {i} - Precio: ")
    while not precio_texto.isdigit():
        print("Error: ingrese un precio numerico valido.")
        precio_texto = input(f"Producto {i} - Precio: ")
    precio = int(precio_texto)

    descuento = input("Descuento (S/N): ")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: responda S o N.")
        descuento = input("Descuento (S/N): ")

    total_sin_descuento += precio

    if descuento.lower() == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print()
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#--------------------------------------------------------------------
# Ejercicio 2 -- "Acceso al Campus y Menu Seguro"
# Login con intentos + menu de acciones con validacion estricta.

USUARIO_CORRECTO = "alumno"
CLAVE_CORRECTA = "python123"

acceso_concedido = False
intento = 1

while intento <= 3 and not acceso_concedido:
    print(f"Intento {intento}/3 - Usuario: ", end="")
    usuario = input()
    clave = input("Clave: ")

    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales invalidas.")
        intento += 1

if not acceso_concedido:
    print("Cuenta bloqueada")
else:
    opcion = 0
    while opcion != 4:
        print()
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_texto = input("Opcion: ")

        while not opcion_texto.isdigit():
            print("Error: ingrese un numero valido.")
            opcion_texto = input("Opcion: ")

        opcion = int(opcion_texto)

        while opcion < 1 or opcion > 4:
            print("Error: opcion fuera de rango.")
            opcion_texto = input("Opcion: ")
            while not opcion_texto.isdigit():
                print("Error: ingrese un numero valido.")
                opcion_texto = input("Opcion: ")
            opcion = int(opcion_texto)

        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: minimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirme la nueva clave: ")
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirme la nueva clave: ")

            CLAVE_CORRECTA = nueva_clave
            print("Clave actualizada con exito.")
        elif opcion == 3:
            print("Cada dia es una nueva oportunidad para aprender algo nuevo.")
        elif opcion == 4:
            print("Hasta luego.")

#--------------------------------------------------------------------
# Ejercicio 3 -- "Agenda de Turnos con Nombres (sin listas)"
# No se permite usar listas, diccionarios, sets ni tuplas.
# Se usan variables individuales para cada turno.

# --- Cupos fijos ---
# Lunes: 4 turnos -> lunes1, lunes2, lunes3, lunes4
# Martes: 3 turnos -> martes1, martes2, martes3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

# --- Nombre del operador ---
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ")


def pedir_dia():
    dia_texto = input("Elegir dia (1=Lunes, 2=Martes): ")
    while not dia_texto.isdigit() or (dia_texto != "1" and dia_texto != "2"):
        print("Error: ingrese 1 o 2.")
        dia_texto = input("Elegir dia (1=Lunes, 2=Martes): ")
    return int(dia_texto)


def pedir_nombre_paciente():
    nombre = input("Nombre del paciente: ")
    while not nombre.isalpha():
        print("Error: solo se permiten letras.")
        nombre = input("Nombre del paciente: ")
    return nombre


opcion = 0
while opcion != 5:
    print()
    print("1) Reservar turno  2) Cancelar turno  3) Ver agenda del dia  4) Resumen general  5) Cerrar sistema")
    opcion_texto = input("Opcion: ")
    while not opcion_texto.isdigit() or int(opcion_texto) < 1 or int(opcion_texto) > 5:
        print("Error: ingrese un numero entre 1 y 5.")
        opcion_texto = input("Opcion: ")
    opcion = int(opcion_texto)

    if opcion == 1:
        # --- Reservar ---
        dia = pedir_dia()
        paciente = pedir_nombre_paciente()

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: el paciente ya tiene turno ese dia.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado.")
            else:
                print("No hay turnos disponibles el Lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: el paciente ya tiene turno ese dia.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado.")
            else:
                print("No hay turnos disponibles el Martes.")

    elif opcion == 2:
        # --- Cancelar ---
        dia = pedir_dia()
        paciente = pedir_nombre_paciente()

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado.")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado.")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado.")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado.")
            else:
                print("No se encontro ese turno.")
        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado.")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado.")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado.")
            else:
                print("No se encontro ese turno.")

    elif opcion == 3:
        # --- Ver agenda del dia ---
        dia = pedir_dia()
        if dia == 1:
            print("Agenda del Lunes:")
            turno_actual = lunes1 if lunes1 != "" else "(libre)"
            print(f"Turno 1: {turno_actual}")
            turno_actual = lunes2 if lunes2 != "" else "(libre)"
            print(f"Turno 2: {turno_actual}")
            turno_actual = lunes3 if lunes3 != "" else "(libre)"
            print(f"Turno 3: {turno_actual}")
            turno_actual = lunes4 if lunes4 != "" else "(libre)"
            print(f"Turno 4: {turno_actual}")
        else:
            print("Agenda del Martes:")
            turno_actual = martes1 if martes1 != "" else "(libre)"
            print(f"Turno 1: {turno_actual}")
            turno_actual = martes2 if martes2 != "" else "(libre)"
            print(f"Turno 2: {turno_actual}")
            turno_actual = martes3 if martes3 != "" else "(libre)"
            print(f"Turno 3: {turno_actual}")

    elif opcion == 4:
        # --- Resumen general ---
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1
        disponibles_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1
        disponibles_martes = 3 - ocupados_martes

        print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles.")

        if ocupados_lunes > ocupados_martes:
            print("Dia con mas turnos: Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("Dia con mas turnos: Martes.")
        else:
            print("Empate entre Lunes y Martes.")

    elif opcion == 5:
        print("Cerrando sistema. Hasta luego.")

#-----------------------------------------------------------------------------------------------
# Ejercicio 4 -- "Escape Room: La Boveda"

# --- Nombre del agente ---
agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Error: solo se permiten letras.")
    agente = input("Nombre del agente: ")

# --- Variables iniciales (no se piden por teclado) ---
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0  # cuenta veces seguidas que se eligio "Forzar cerradura"

print(f"\nAgente {agente}, la mision comienza.")

bloqueado = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print()
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")
    opcion_texto = input("Opcion: ")
    while not opcion_texto.isdigit() or int(opcion_texto) < 1 or int(opcion_texto) > 3:
        print("Error: ingrese un numero entre 1 y 3.")
        opcion_texto = input("Opcion: ")
    opcion = int(opcion_texto)

    if opcion == 1:
        # --- Forzar cerradura ---
        racha_forzar += 1
        energia_antes = energia
        energia -= 20
        tiempo -= 2

        if racha_forzar >= 3:
            print("La cerradura se trabo por forzarla demasiadas veces seguidas.")
            alarma = True
        else:
            if energia_antes < 40:
                print("Riesgo de alarma. Elija con cuidado (1-3):")
                riesgo_texto = input("Numero (1-3): ")
                while not riesgo_texto.isdigit() or int(riesgo_texto) < 1 or int(riesgo_texto) > 3:
                    print("Error: ingrese un numero entre 1 y 3.")
                    riesgo_texto = input("Numero (1-3): ")
                riesgo = int(riesgo_texto)
                if riesgo == 3:
                    alarma = True
                    print("Se activo la alarma.")

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura forzada con exito.")

    elif opcion == 2:
        # --- Hackear panel ---
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Progreso hackeo: paso {paso}/4 -> codigo: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El hackeo abrio una cerradura automaticamente.")

    elif opcion == 3:
        # --- Descansar ---
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
        print("El agente descansa.")

    # --- Regla de bloqueo por alarma ---
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

# --- Condiciones de fin ---
if cerraduras_abiertas == 3:
    print("\nVICTORIA: la boveda fue abierta con exito.")
elif bloqueado:
    print("\nDERROTA (bloqueo): el sistema se bloqueo por la alarma.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA: se acabo la energia o el tiempo.")

#------------------------------------------------------------------------------------------------------------------
# Ejercicio 5 -- "Escape Room: La Arena del Gladiador"

print("--- BIENVENIDO A LA ARENA ---")

# --- Nombre del gladiador (String) ---
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# --- Estadisticas iniciales ---
vida_jugador = 100        # int
vida_enemigo = 100        # int
pociones = 3               # int
dano_ataque_pesado = 15    # int
dano_enemigo = 12          # int
turno_gladiador = True     # boolean

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion_texto = input("Opcion: ")
    while not opcion_texto.isdigit() or int(opcion_texto) < 1 or int(opcion_texto) > 3:
        print("Error: Ingrese un numero valido.")
        opcion_texto = input("Opcion: ")
    opcion = int(opcion_texto)

    if opcion == 1:
        # --- Ataque Pesado ---
        if vida_enemigo < 20:
            dano_final = dano_ataque_pesado * 1.5  # float, golpe critico
            print("!Golpe critico!")
        else:
            dano_final = float(dano_ataque_pesado)
        vida_enemigo -= dano_final
        print(f"!Atacaste al enemigo por {dano_final} puntos de dano!")

    elif opcion == 2:
        # --- Rafaga Veloz ---
        print(">> !Inicias una rafaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de dano")

    elif opcion == 3:
        # --- Curar ---
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Usaste una pocion. Recuperaste 30 puntos de vida.")
        else:
            print("!No quedan pociones!")

    # --- Turno del enemigo ---
    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f"!El enemigo te ataco por {dano_enemigo} puntos de dano!")

    print("=== NUEVO TURNO ===")

# --- Fin del juego ---
if vida_jugador > 0:
    print(f"!VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")