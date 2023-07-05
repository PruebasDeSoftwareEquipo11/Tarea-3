inventario = [
    ["Call Of Duty Modern Warfare 3", "Acción", "Xbox 360/Playstation 3/PC", 5, 5000, 4000],
    ["Call Of Duty Modern Warfare 2", "Acción", "Xbox 360/Playstation 3/PC", 5, 4000, 3500],
    ["Call Of Duty Modern Warfare", "Acción", "Xbox 360/Playstation 3/PC", 5, 100, 80],
    ["Resident Evil 2 Remake", "Survival Horror", "Xbox One/Playstation 4/PC", 20, 15000, 10000],
    ["Resident Evil 4 Remake", "Survival Horror", "Xbox One/Playstation 4/PC", 50, 30000, 25000],
    ["Silent Hill 2 Remake", "Survival Horror", "Playstation 5/PC", 2, 60000, 50000],
    ["juego","genero","plataforma",2,10,8]
]
compras = []
importaciones = []

def login_system():
    option = input(
        "Ingrese tipo de usuario:\n1.- Administrador\n2.- Cliente\n3.- Salir\nIngrese el número de opción: "
    )
    option = option.strip()
    if option == "2" or option == "3":
        return option
    elif option == "1":
        password = input("Ingrese contraseña de administrador: ")
        if password.strip() == "1234":
            return option
        else:
            return "INVALID"
    else:
        return "INVALID"

def mostrar_catalogo():
    for name, genere, platform, amount, price, _ in inventario:
        print("Nombre:", name)
        print("Género:", genere)
        print("Plataforma:", platform)
        print("Cantidad en tienda:", amount)
        print("Precio:", str(price) + " CLP\n")
    print("\n")

def comprar_juego():
    print("Menú de Compra\n")
    tittle = input("Ingrese el título que desea comprar: ")
    if tittle == "":
        print("ERROR")
        return "ERROR"
    amount = input("Ingrese la cantidad que desea comprar: ")
    if amount == "":
        print("ERROR")
        return "ERROR"
    tittle = tittle.strip()
    amount = int(amount.strip())
    if amount <= 0:
        print("ERROR")
        return "ERROR"
    finded = False
    for i in range(len(inventario)):
        inventory_tittle, _, _, inventory_amount, inventory_price, _ = inventario[i]
        if tittle.lower() == inventory_tittle.lower():
            finded = True
            if inventory_amount >= amount:
                inventario[i][3] -= amount
                print("Total a pagar:", amount * inventory_price)
                print("Gracias por su compra estimado cliente.\n")
                compras.append((inventory_tittle, amount, amount * inventory_price))
            else:
                print("Faltan copias físicas para realizar la compra!\n")
    if not finded:
        print("No se encontró dicho juego en la tienda.\n")

def vender_juego():
    print("Bienvenido al menú para vender.\n\n")
    tittle = input("Ingrese el título: ")
    if tittle == "":
        print("ERROR")
        return "ERROR"
    amount = input("Ingrese la cantidad: ")
    if amount == "":
        print("ERROR")
        return "ERROR"
    amount = int(amount)
    if amount <= 0:
        print("ERROR")
        return "ERROR"
    finded = False
    for i in range(len(inventario)):
        if tittle.lower() == inventario[i][0].lower():
            finded = True
            inventario[i][3] += amount
            importaciones.append([tittle, amount, inventario[i][-1]])

    if not finded:
        genere = input("Ingrese un género: ")
        if genere == "":
            print("ERROR")
            return "ERROR"
        platform = input("Ingrese una plataforma (si es más de una seguir este formato: xbox/pc/etc): ")
        if platform == "":
            print("ERROR")
            return "ERROR"
        costo = int(input("Ingrese el valor que costó el juego: "))
        if costo <= 0:
            print("Valor Invalido")
            return "ERROR"
        inventario.append([tittle, genere, platform, amount, int(costo * 1.2), costo])
        importaciones.append([tittle, amount, costo*amount])

def mostrar_inventario():
    print("Inventario:\n")
    for name, genere, platform, amount, price, cost in inventario:
        print("Título:", name)
        print("Género:", genere)
        print("Plataforma:", platform)
        print("Cantidad disponible:", amount)
        print("Precio:", price)
        print("Costo del juego:", cost)
        print("\n")
    print("\n")
    sum_ventas = 0
    sum_compras = 0
    ganancias = 0
    perdidas = 0
    for i in compras:
        sum_compras += i[1]
        ganancias += i[2]
        
    for i in importaciones:
        sum_ventas += i[1]
        perdidas += i[2]
    print(importaciones)
    print("Estadísticas de la tienda:\n")
    print("Cantidad de juegos vendidos:", sum_compras)
    print("Cantidad de juegos adquiridos:", sum_ventas)
    print("Ganancias:", ganancias)
    print("Pérdidas:", perdidas)
    print("Desempeño:", ganancias - perdidas)

def menu(option):
    print("\n¡Bienvenido al menú principal de la Tienda!\nIngrese una opción nuevamente:")
    while True:
        print("1.- Ver catálogo de juegos.")
        if option == "2":
            print("2.- Comprar.")
        elif option == "1":
            print("2.- Comprar.")
            print("3.- Vender.")
            print("4.- Ver inventario.")
        print("\nPara salir del menú, simplemente presione la tecla Enter.")
        menu_option = input("\nIngrese una opción válida, por favor: ")
        menu_option = menu_option.strip()
        if menu_option == "1":
            mostrar_catalogo()
        elif menu_option == "":
            print("Usted ha salido del menú de la tienda.\n")
            break
        elif option == "2" and menu_option == "2":
            comprar_juego()
        elif option == "1":
            if menu_option == "2":
                comprar_juego()
            elif menu_option == "3":
                vender_juego()
            elif menu_option == "4":
                mostrar_inventario()

def main():
    option = login_system()
    if option == "INVALID":
        print("Contraseña inválida.")
    elif option == "1" or option == "2":
        menu(option)
    else:
        print("Gracias por su visita.")

if __name__ == "__main__":
    main()