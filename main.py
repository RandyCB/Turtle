import turtle
import math

"""
El modulo turltle utiliza pixeles como parametro de distancia
para usar cm se debe realizar una conversion considerando los pixeles
por centimetro de la pantalla respectiva
para el presente caso se cuenta con una pantalla de:

resolucion1366x768 
tamañño 30.5cm x 17 cm 
por lo cual al calcular y dividir la diagonal de pixeles entre la de cm
se obtiene la relacion de 44.88px = 1cm
"""


"""
Los colores para las figuras geometricas definidos en hexadecimal 
"""
colorCirculo = "#ffff1a"
colorCuadrado = "#ff0080"
colorTriangulo = "#53ff1a"
colorRombo = "#2576C3"
colorPentagono = "#808080"
colorHexagono = "#9e4ae4"


"""
Para cada figura se define una funcion en donde se pasa como parametro una medida en cm y un objeto de
tipo turlte para controlar el cursor
Se utiliza el color negro para el borde en todas las figuras y se define un color diferente para el interior de la figura.
"""
def Circulo(radio,lapiz):
    circulo = lapiz
    circulo.color("black", colorCirculo)
    circulo.begin_fill()
    circulo.circle(radio)
    circulo.end_fill()

    
def Cuadrado(lado,lapiz):
    cuadrado = lapiz  
    cuadrado.color("black", colorCuadrado)
    cuadrado.begin_fill()
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.end_fill()


def Triangulo(lado,lapiz):
    triangle = lapiz
    triangle.color("black",colorTriangulo)
    triangle.begin_fill()
    triangle.forward(lado)
    triangle.left(120)
    triangle.forward(lado)
    triangle.left(120)
    triangle.forward(lado)
    triangle.left(120)
    triangle.end_fill()
    
    
def Rombo(lado,lapiz):
    Rombo = lapiz
    Rombo.color("black", colorRombo)
    Rombo.begin_fill()
    Rombo.left(60)
    Rombo.forward(lado)
    Rombo.right(120)
    Rombo.forward(lado)
    Rombo.right(60)
    Rombo.forward(lado)    
    Rombo.right(120)
    Rombo.forward(lado)
    Rombo.right(120)
    Rombo.end_fill()


def Pentagono(lado,lapiz):
    Penta = lapiz
    Penta.color("black", colorPentagono)
    Penta.begin_fill()
    Penta.forward(lado)
    Penta.left(72)
    Penta.forward(lado)
    Penta.left(72)
    Penta.forward(lado)
    Penta.left(72)
    Penta.forward(lado)
    Penta.left(72)
    Penta.forward(lado)
    Penta.left(72)
    Penta.end_fill()


def Hexagono(lado,lapiz):
    Hexa = lapiz
    Hexa.color("black", colorHexagono)
    Hexa.begin_fill()
    Hexa.forward(lado) 
    Hexa.right(300)
    Hexa.forward(lado)
    Hexa.right(300)
    Hexa.forward(lado)
    Hexa.right(300)
    Hexa.forward(lado)
    Hexa.right(300)
    Hexa.forward(lado)
    Hexa.right(300)
    Hexa.forward(lado)
    Hexa.right(300)
    Hexa.end_fill()


"""
La funcion recibe cual figura se ha seleccionado y el valor del radio y
caclula la relacion que tiene el lado del poligono con respecto al valor del
radio que ha seleccionado el usuario segun cada figura y devuelve este valor
"""
def LadoPoligonoInscrito(opcion2, radio):
    if(opcion2 == 2):
        lado = math.sqrt(2*(radio**2))
        return lado
    elif(opcion2 == 3):
        lado = radio*math.sqrt(3)
        return lado
    elif(opcion2 == 5):
        rad = ((72/2)*math.pi) / 180
        lado = 2*radio*(math.sin(rad))    
        return lado
    elif(opcion2 == 6):
        lado = radio
        return lado
    else:
        pass

"""
La funcion recibe cual figura se ha seleccionado y el valor del lado de la misma y
caclula la relacion que tiene el radio del circulo a inscribirse con respecto al valor del
lado del poligono que ha seleccionado el usuario y devuelve ese valor
"""
def RadioCirculoInscrito(opcion1, lado):
    if(opcion1 == 2):
        radio = lado/2
        return radio
    elif(opcion1 == 3):
        rad = rad = (30*math.pi) / 180
        radio = math.tan(rad) * (lado/2)
        return radio
    elif(opcion1 == 4):
        rad = rad = (30*math.pi) / 180
        radio = math.sin(rad)*math.cos(rad)*lado
        return radio
    elif(opcion1 == 5):
        rad = rad = (54*math.pi) / 180
        radio = math.tan(rad) * (lado/2)
        return radio
    elif(opcion1 == 6):
        rad = rad = (60*math.pi) / 180
        radio = math.tan(rad) * (lado/2)
    else:
        pass            

"""
Se encarga de manejar el dibujo para todas las combinaciones que tienen un poligono inscrito
en un circulo, llamando a la funcion de circulo y despues acomodando el cursor en la posicion adecuada
antes de invocar a la funcion del poligono que el usuario ha seleccionado
"""
def PoligonoInscritoEnCirculo(opcion2, radio,lapiz):
    if(opcion2 == 2):
        Circulo(radio,lapiz)    
        lado = LadoPoligonoInscrito(opcion2,radio)
        lapiz.left(90)
        lapiz.penup()
        lapiz.forward(radio)
        lapiz.left(90)
        lapiz.forward(lado/2)
        lapiz.left(90)
        lapiz.forward(lado/2)
        lapiz.left(90)
        lapiz.pendown()
        Cuadrado(lado,lapiz)

    elif(opcion2 == 3):
        Circulo(radio,lapiz)
        lado = LadoPoligonoInscrito(opcion2,radio)
        lapiz.left(90)
        lapiz.penup()
        lapiz.forward(radio*2)
        lapiz.right(210)
        lapiz.forward(lado)
        lapiz.left(120)
        lapiz.pendown()
        Triangulo(lado,lapiz)

    elif(opcion2 == 5):
        Circulo(radio,lapiz)
        lado = LadoPoligonoInscrito(opcion2,radio)
        lapiz.penup()
        lapiz.left(90)
        lapiz.forward(radio*2)
        lapiz.left(126)
        lapiz.forward(lado)    
        lapiz.left(72)
        lapiz.forward(lado)
        lapiz.left(72)
        lapiz.pendown()
        Pentagono(lado,lapiz)

    elif(opcion2 == 6):
        Circulo(radio,lapiz)
        lado = LadoPoligonoInscrito(opcion2,radio)
        lapiz.left(90)
        lapiz.penup()
        lapiz.forward(radio)
        lapiz.left(90)
        lapiz.forward(radio)
        lapiz.left(120)
        lapiz.forward(radio)
        lapiz.right(300)
        lapiz.pendown()
        Hexagono(lado,lapiz)

    else:
        pass


"""
Se encarga de manejar el dibujo para todas las combinaciones que tienen un circulo inscrito
en un poligono, llamando a la funcion del poligono y despues acomodando el cursor en la posicion adecuada
antes de invocar a la funcion del circulo
"""        
def CirculoInscritoEnPoligono(opcion2,lado,lapiz):
    if(opcion2 == 2):
        Cuadrado(lado, lapiz)
        lapiz.penup()
        lapiz.forward(lado/2)
        lapiz.pendown()
        radio = RadioCirculoInscrito(opcion2, lado)
        Circulo(radio,lapiz)
        
    elif(opcion2 == 3):
        Triangulo(lado, lapiz)
        lapiz.penup()
        lapiz.forward(lado/2)
        lapiz.pendown()
        radio = RadioCirculoInscrito(opcion2, lado)
        Circulo(radio, lapiz)

    elif(opcion2 == 4):
        radio = RadioCirculoInscrito(opcion2, lado)
        Rombo(lado, lapiz)
        lapiz.penup()
        lapiz.forward(lado/2)
        lapiz.right(90)
        lapiz.forward(radio)
        lapiz.left(90)
        lapiz.pendown()
        Circulo(radio, lapiz)

    elif(opcion2 == 5):
        Pentagono(lado, lapiz)
        lapiz.penup()
        lapiz.forward(lado/2)
        lapiz.pendown()
        radio = RadioCirculoInscrito(opcion2, lado)
        Circulo(radio, lapiz)

    elif(opcion2 == 6):
        Hexagono(lado, lapiz)
        lapiz.penup()
        lapiz.forward(lado/2)
        lapiz.pendown()
        radio = RadioCirculoInscrito(opcion2, lado)
        Circulo(radio, lapiz)
        
    else:
        pass

 
"""
Contine una variable donde se define el formato del menu e imprime esta variable
en pantalla
"""
def Menu():
        menu = """----------------------Menu----------------------\n             
        1. Circulo \n
        2. Cuadrado \n
        3. Triángulo equilátero \n
        4. Rombo \n
        5. Pentágono regular \n
        6. Hexágono regular \n

        ------------------------------------------------
        """
        print(menu)


"""
punto de inicio del programa donde se despliega el menu y se interactua con el usuario
se condicionan las opciones de figuras que no pueden ser inscritas en una figura especifica (ej un rombo en un circulo)
y se llaman a las funciones que manejan cada caso segun sea un circulo inscrito en un poligono
o un poligono inscrito en un circulo
"""
def mainF():
 
    Menu()
    option1 = int(input("Seleccione el número de la figura a dibujar: "))

    if(option1 != 1):
        option2 = 1
    else:
        option2 = int(input("Selecione el número de la figura a ser inscrita: "))
        if(option2 == 4 or option2 == 1):
            print("\n El poligono seleccionado no puede ser inscrito en el circulo!! \n          **********Intente de nuevo**********\n")
            mainF()
            
         
    medidas = int(input("Introduzca la medida en cm para las figuras elegidas: "))
    centimetros = medidas * 44.88
    lapiz = turtle.Turtle()
    
    if(option1 == 1):
        PoligonoInscritoEnCirculo(option2,centimetros,lapiz)
    else:
        CirculoInscritoEnPoligono(option1,centimetros,lapiz)

mainF()
