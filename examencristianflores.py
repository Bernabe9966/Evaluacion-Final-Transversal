#Examen Transversal Final Cristian Flores

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
                           }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock[modelo][1]
    print(f"El stock total de {marca} es", total)

def busqueda_ram_precio(ram_min, ram_max, preciomin, preciomax):
    resultado = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if preciomin <= precio <= preciomax and cantidad > 0:
            marca = productos[modelo][0]
            resultado.append(f"{marca}----{modelo}")
        if ram_min <= precio <= ram_max and cantidad > 0:
            ram = productos[modelo][0]
            resultado.append(f"{ram}----{modelo}")
       
    if resultado:
        print("Los notebooks consultados entre el precio y la ram son:", sorted(resultado))
    else:
        print("No hay notebooks que mostrar.")
        

def eliminar_producto(modelo):
    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock [modelo]
        return True
    else:
        return False

while True:
    print("*** MENU PRINCIPAL ***")
    print("1.- Stock marca.")
    print("2.- Busqueda por RAM.")
    print("3.- Eliminar Producto.")
    print("4.- Salir.")
    try:
        opcion = input("Ingrese la opcion que desea elegir: ")
    except ValueError:
        print("Debe ingreser un valor entero, vuelva a intentarlo.")

    if opcion == '1':
        marca = input("Ingrese la marca que desea consultar: ")
        stock_marca(marca)
    elif opcion == '2':
        while True: 
            try:
                preciomin = int(input("Ingrese el precio minimo que desea buscar: "))
                preciomax = int(input("Ingrese el precio maximo que desea buscar: "))
                ram_min = int(input("Ingrese la cantidad de RAM minima que desea buscar: "))
                ram_max = int(input("Ingrese la cantidad de RAM maxima que desea buscar: "))
                break
            except ValueError:
                print("Ingrese valores enteros porfavor, vuelva a intentarlo.")
        busqueda_ram_precio(preciomin, preciomax, ram_min, ram_max)
    elif opcion == '3':
        while True:
            modelo = input("Ingrese el modelo que desea eliminar: ").upper()
            if eliminar_producto(modelo):
                print("¡Producto eliminado con exito!")
            else: 
                print("Lo siento, el modelo buscado no existe.")
            opcion2 = input("Desea eliminar otro producto (si/no): ").lower()
            if opcion2 != 'si':
                break

    elif opcion == '4':
        print("Programa finalizado.")
        break

    else:
        print("Seleccione una opcion valida.")
    