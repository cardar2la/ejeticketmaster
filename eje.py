nombre = input ("Escribe tu nombre por favor: ")
print ("Bienvenid@ ",nombre, " estás en la página de ticket master, para la compra de los boletos para el concierto de Billie Eilish, en las fechas 28, 29 y 30 de marzo del 2025.")
ejecutar = True 
def price ( zona, cantidad):
    global precio
    precio = zona*cantidad
while ejecutar:
    numero = int(input("Presiona 1 si deseas comprar boleto (s), o presiona 2 si deseas cancelar boleto (s)"))

    if numero == 1:
        ejecutar = True
        while ejecutar:
            boletos = int(input("¿Cuántos boletos deseas adquirir?"))
            if boletos <= 0 or boletos > 4: 
                boletos = int(input("El límite de boletos es de 4, elige entre 1 y 4 boletos, no más, no menos: "))
                ejecutar = True
            elif boletos == 1:
                print("Perfecto, procesando tu compra")
                ejecutar = False
            elif boletos == 2:
                print("Perfecto, procesando tu compra")
                ejecutar = False 
            elif boletos == 3:
                print("Perfecto, procesando tu compra")
                ejecutar = False
            elif boletos == 4:
                print("Perfecto, procesando tu compra")
                ejecutar = False 
            else:
                print("opción no válida")
                ejecutar = True

        print("El lugar de tus asientos determina el costo de tus boletos por lo que tendrás que elegir un lugar")
        print("Las áreas son: \n General A con un costo de $3,000 mx \n General B con un costo de $2,500 mx \n Gradas C con un costo de $1,200 mx \n Gradas D con un costo de $800 mx")
        print("Deberas elegir un número dependiendo que lugar prefieres: \n 1 para general A \n 2 para general B \n 3 para gradas C \n 4 para gradas D")

        ejecutar = True
        while ejecutar: 
            lugares = int(input("Presiona un número"))
            if lugares == 1:
                print("Escogiste general A con un costo de $3,000 mx")
                price(3000, boletos)
                print("Tus boletos más el lugar te da un total de: ", precio)
                ejecutar = False
            elif lugares == 2:
                print("Escogiste general B con un costo de $2,500 mx")
                price(2500, boletos)
                print("Tus boletos más el lugar te da un total de: ", precio)
                ejecutar = False
            elif lugares == 3:
                print("Escogiste gradas C con un costo de $1,200 mx")
                price(1200, boletos)
                print("Tus boletos más el lugar te da un total de: ", precio)
                ejecutar = False
            elif lugares == 4:
                print("Escogiste gradas D con un costo de $800 mx")
                price(800, boletos)
                print("Tus boletos más el lugar te da un total de: ", precio)
                ejecutar = False
            else:
                print("Opción no válida")
                ejecutar = True
            
            precio = precio
            print(precio)
        
            dia = input("Coloca la fecha que deseas tu evento: ")
            if  dia == "28" or dia == "29" or dia == "30":
             print("Perfecto")
            elif dia != "28" or dia != "29" or dia != "30":
                print(input("Opción no válida, elige solo las opciones prudentes"))


            descuento = input("¿Tienes algun cupón de descuento?")
            if descuento == "si":
                print("Está bien")
                codigo = input("Inserta tu código")

                while codigo != "39724924":
                    codigo = input("El código es incorrecto intenta de nuevo: ")

                desc = precio - (precio * 0.20)
                print(desc)
                print("Tu resumen de compra es de ", boletos, " boletos, en el lugar ", lugares, " (revisa arriva tus lugares), con un total de: ", precio, " y con descuento de ", desc, " en el día: ", dia)
                
            if descuento == "no":
                print("Está bien")
                print("Tu resumen de compra es de ", boletos, " boletos, en el lugar ", lugares, " (revisa arriva tus lugares), con un total de: ", precio, "en el día: ", dia)

            fin = input("¿Deseas realizar alguna otra actividad?")
            if fin == "si":
                print("Regresaras al menú principal")
                ejecutar = True
            elif fin == "no":
                print("Muchas gracias por tu compra, esperamos y la disfrutes.")
                ejecutar = False

    if numero == 2:
        cancel = int(input("¿Cuantos boletos deseas cancelar?"))
        print("Perfecto, la mentablemente no existen rembolosos ni devoluciones, gracias por cancelar.")
        fin = input("¿Deseas realizar alguna otra actividad?")
    if fin == "si":
        print("Regresaras al menú principal")
        ejecutar = True
    elif fin == "no":
        print("Muchas gracias por tu cooperación.")
        ejecutar = False