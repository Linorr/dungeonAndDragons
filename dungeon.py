# Juego Dungeons & Dragons en Python (juego de preguntas simples).
print("__________________________________Dragones y Mazmorras_______________________________")
print("=====================================================================================")
print("=============================By Lino  # Copyright: © 2.021===========================")
print("#####################################################################################")

print("Erase una vez un hace muchos años, un reino que luchaba contra bestias imposibles....")
input()
print("Era un pueblo valiente donde sus hombres servian en las fuerzas de del Lord Mariscal ")
print('______________________Prepárate tienes que elegir____________________________________')
seleccion = input('Ingrese ejercito Posibilidad arquero, arcabucero ò piquero: ')
print("###########################   PULSA ENTER  ##########################################")
input()
if seleccion == 'arquero':
    print(" Arquero !!!!!Ve al campo de entrenamiento y destroza los sacos con tus flechazos")
elif seleccion == 'arcabucero':
    print('Arcabucero !!!! Ve a por tus armas y municiónate eres la élite del ejercito......')
elif seleccion == 'piquero':
    print("Píquero !!! Te necesitamos debes defender la retaguardia, busca tus armas........")
print("###########################   PULSA ENTER  ##########################################")
input()
print("Ya tenemos a nuestro soldado enrolado en su grupo, ahora hay que entrenar y valor....")
print("###########################   PULSA ENTER  ##########################################")
input()
print("Suena el cuerno de guerra en las almenas !!!soldados a las armas, viene Lord Mariscal")
input()
print("Mis titanes, hoy es un día grande la historia nos llama para la gloria a luchar......")
print("###########################   PULSA ENTER  ##########################################")
input()
accion = input('Ingrese accion ir a las: almenas, puertas ó huir ')
if accion == 'almenas':
    if seleccion == 'arquero':
        print("Eres de gran utilidad ya que eres un arquero infalible. bien!!!!!............")
    elif seleccion == 'piquero':
        print("soldado que haces aquí solo puedes estorbar Lárgate de aquí o te fusilo......")
    elif seleccion == 'arcabucero':
        print("Eres bien recibido destruye al enemigo con tus armas,defiende a los arqueros.")
elif accion == 'puertas':
    if seleccion == 'arquero':
        print("Arquero vete a las almenas ¿quieres morir joven? corred corred...............")
    elif seleccion == 'piquero':
        print("Soldado manten la posición se que eres valiente, vende cara tu piel..........")
    elif seleccion == 'arcabucero':
        print("Arcabuces !!! defended a los piqueros y a los arqueros esas mechas encendidas")
if accion == 'huir':
    if seleccion == 'arquero':
        print("eres un cobarte muere como tal...............................................")
    elif seleccion == 'piquero':
        print("eres un cobarte muere como tal...............................................")
    elif seleccion == 'arcabucero':
        print("eres un cobarte muere como tal...............................................")
print("_____________________________________________________________________________________")
print("_____________________________________________________________________________________")
input()
print("Aparece La bestia surcando los cielos, con su aliento de fuego, viene de frente......")
input()
print("Pulverizando con fuego una división entera de soldados en la puerta, quemados vivos..")
print(" A las armas mis arqueros, ensartarlo con vuestra furia, ahoraaaa!!!!................")
seleccion = input('Ingrese ejercito Posibilidad arquero, arcabucero ò piquero: ')
print("###########################   PULSA ENTER  ##########################################")
input()
if seleccion == 'arquero':
    print(" Disparas todas tus flechas mientras viene a por vosotros, buscas más............")
elif seleccion == 'piquero':
    print("Sales corriendo con tu regimiento para defender a tus compañeros y recoger heridos")
elif seleccion == 'arcabucero':
    print("Disparas todo tu plomo, el calor del arma no es nada con lo que ves venir........")
print("El Dragón ha resultado herido, cae en picado destrozando la torre del castillo.......")
input()
print("Lord Mariscal ha sido herido, pero se levanta con tu ayuda, te asciende a teniente...")
print("---------------------------------------FIN DEL JUEGO---------------------------------")