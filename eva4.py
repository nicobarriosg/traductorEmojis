#LISTAS
def emojis():
    lista = [["<<3", "amor"],[":*>", "preocupado"],[">:-", "molesto"],[":<>", "gracioso"],["0_0", "miedo"],["=]]", "feliz"],["=[]", "emocionado"],["=_=", "extraño"],["~.~", "incomodo"],["#_#", "confundido"]]
    return lista
def censura():
    lista = [["###", "tonto"],["#@#", "estupido"],["#!&", "bobo"],["!$*", "recorcholis"],["#!%", "caspitas"]]
    return lista

listaEmojis = emojis()
listaCensura = censura()

#AGREGAR
def agregar():
    while True:
        print("")
        print("====================")
        print("MENU PARA AGREGAR")
        print("")
        print("Ingrese la opcion que desea")
        print("")
        print("1. Agregar emoji")
        print("2. Agregar emoji censura")
        print("3. Volver")
        print("")
        try:
            opcion =  int(input("→ "))
            print("")
            if opcion == 1:
                print("====================")
                print("Ingrese el emoji que desea crear (UNICAMENTE DE 3 CARACTERES)")
                emoji =  input("→ ")
                if len(emoji) == 3:
                    print("Ingrese su significado")
                    significado = input("→ ")
                    for i in range(len(listaEmojis)):
                        if emoji in listaEmojis[i][0]:
                            print("")
                            print("Este emoji ya existe")
                            return agregar()
                        elif significado in listaEmojis[i][1]:
                            print("")
                            print("Ya existe un emoji con este significado")
                            return agregar()
                        else:
                            listaEmojis.append([emoji, significado])
                            print("")
                            print("Emoji {} agregado con éxito".format(emoji))
                else:
                    print("")
                    print("No cumple con los 3 caracteres")
            elif opcion == 2:
                print("Ingrese el emoji censura que desea crear")
                emoji =  input("→ ")
                if len(emoji) == 3:
                    print("Ingrese su significado")
                    significado = input("→ ")
                    for i in range(len(listaCensura)):
                        if emoji in listaCensura[i][0]:
                            print("")
                            print("Este emoji ya existe")
                            return agregar()
                        elif significado in listaCensura[i][0]:
                            print("")
                            print("Ya existe un emoji con este significado")
                            return agregar()
                        else:
                            listaCensura.append([emoji, significado])
                            print("")
                            print("Emoji {} agregado con éxito".format(emoji))
                else:
                    print("")
                    print("No cumple con los 3 caracteres")
            elif opcion == 3:
                break
            else:
                print("Ingrese un numero valido")
        except ValueError:
            print("")
            print("No es un numero entero")

#MOSTRAR
def menuMostrar():
    while True:
        print("")
        print("====================")
        print("MENU PARA MOSTRAR")
        print("")
        print("Ingrese la opcion que desea")
        print("")
        print("1. Emojis")
        print("2. Emojis censura")
        print("3. Volver")
        print("")
        try:
            ver = int(input("→ "))
            print("")
            if ver == 1:
                lista = listaEmojis
                mostrar(lista)
            elif ver == 2:
                lista = listaCensura
                mostrar(lista)
            elif ver == 3:
                break
            else:
                print("Ingrese un numero valido")
        except ValueError:
            print("")
            print("No es un numero entero")
def mostrar(lista):
    for emoji in lista:
        print(emoji[0], "-", emoji[1])
    print("")

#ACTUALIZAR
def actualizar():
    while True:
        print("")
        print("====================")
        print("MENU PARA ACTUALIZAR")
        print("")
        print("Ingrese la opcion que desea")
        print("")
        print("1. Actualizar emojis")
        print("2. Actualizar emojis censura")
        print("3. Volver")
        print("")
        try:
            ver = int(input("→ "))
            print("")
            if ver == 1:
                print("====================")
                print("Ingrese el emoji que desea actualizar")
                emojiAntiguo = input("→ ")
                print("Ingrese el nuevo emoji que desa (UNICAMENTE DE 3 CARACTERES)")
                emojiNuevo = input("→ ")
                if len(emojiNuevo) == 3:
                    print("ingrese el significado para el nuevo emoji")
                    significadoNuevo = input("→ ")
                    for i in range(len(listaEmojis)):
                        if emojiNuevo in listaEmojis[i][0]:
                            print("")
                            print("Este emoji ya existe")
                            return actualizar()
                        elif significadoNuevo in listaEmojis[i][1]:
                            print("")
                            print("Ya existe un emoji con este significado")
                            return actualizar()
                        else:
                            if listaEmojis[i][0] == emojiAntiguo:
                                listaEmojis[i][0] = emojiNuevo 
                                listaEmojis[i][1] = significadoNuevo
                                print("")
                                print("El emoji {} fue actualizado a {} con exito".format(emojiAntiguo, emojiNuevo))
                else:
                    print("")
                    print("No cumple con los 3 caracteres")    
            elif ver == 2:
                print("")
            elif ver == 3:
                break
            else:
                print("Ingrese un numero valido")

        except ValueError:
            print("")
            print("No es un numero entero")

#BORRAR
def menuBorrar():
    while True:
        print("")
        print("====================")
        print("MENU PARA BORRAR")
        print("")
        print("1. Borrar Emojis")
        print("2. Borrar emojis censura")
        print("3. Volver")
        print("")
        try:
            opcion= int(input("→ "))
            print("")
            if opcion == 1:
                eleccion = "emoji"
                lista = listaEmojis
                borrar(lista, eleccion)
            elif opcion == 2:
                eleccion = "emoji censura"
                lista = listaCensura
                borrar(lista, eleccion)
            elif opcion == 3:
                break
            else:
                print("Ingrese un numero valido")
        except ValueError:
            print("")
            print("No es un numero entero")            
def borrar(lista, eleccion):
    print("Ingrese el {} que desea borrar".format(eleccion))
    emoji = input("→ ")
    for i in range(len(lista)):
        if lista[i][0] == emoji:
            del lista[i]
            print("")
            print("Emoji {} borrado con éxito".format(emoji))
            break

#MENU PRINCIPAL
def menu():
    print("")
    print("====================")
    print("BIENVENIDO!!")
    print("")
    print("Ingrese la opcion que desea")
    print("")
    print("1. Traducir un mensaje")
    print("2. Mostrar Emojis")
    print("3. Agregar Emojis")
    print("4. Actualizar Emojis")
    print("5. Borrar Emojis")
    print("6. Salir")
    print("")
    opcion = int(input("→ "))
    try:
        return opcion
    except ValueError:
        print("")
        print("No es un numero entero")

#INGRESAR MENSAJE
def mensaje():
    texto = ""
    while True:
        print("Ingrese el texto")
        tex = input("→ ").strip()
        print("Ingrese el emoji")
        emo = input("→ ").strip()
        if emo == "":
            texto += tex + " "
        else:
            texto += tex + " %"+emo+"%"
            return texto, emo, tex

#MENSAJES CENSURADO        
def censura(emo):
    contadorCensura = 0
    for i in range(len(listaCensura)):
        if listaCensura[i][0] == emo:
            contadorCensura += 1
            if contadorCensura == 1:
                print("")
                print("El mensaje tiene un emoji indebido, fue censurado")
            elif contadorCensura == 2:
                print("")
                print("El mensaje tiene dos emoji indebidos, el mensaje no se envio")
                return menu()
            else:
                continue
    return contadorCensura

#CONFIRMACION CENSURA
def traduccion(texto, emo, tex):
    censuras = ("*** CENSURADO ***")
    censuraEmoji = censura(emo)
    print("Mensaje finalizado? (S/N)")
    opcion = input("→ ").upper()
    if opcion == "N":
        mensaje()
    elif opcion == "S":
        if censuraEmoji:
            print("")
            print("El mensaje contiene un emoji que fue censurado")
            print(tex, censuras + "\n")
            return menu()
        for i in range(len(listaEmojis)):
            if listaEmojis[i][0] == emo:
                for emoji in listaEmojis:
                    if emo == emoji[0]:
                        string = texto.split()
                        textoActualizado = string[1] = emoji[1]
                        print("")
                        print("Mensaje enviado:")
                        print(tex + "", textoActualizado + "\n")
                        return menu()
    else:
        print("Ingrese una opcion valida (S/N)")

#PP

menuPrincipal = menu()
while True:
    if menuPrincipal == 1:
        texto, emo, tex = mensaje()
        traduccion(texto, emo, tex)
    elif menuPrincipal == 2:
        menuMostrar()
    elif menuPrincipal == 3:
        agregar()
    elif menuPrincipal == 4:
        actualizar()
    elif menuPrincipal == 5:
        menuBorrar()
    else:
        break

