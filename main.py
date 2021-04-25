import turtle
import math

""" DUDAS
1. Las medidas para figura 1 y 2 son las mismas
2. se puede seleccionar dos veces la misma figura
3. Medidas de PPI
"""

#1366x768 resolutin
#30.5cm x 17 cm size
#44.88px = 1cm


#MANEJAR EXCEPCIONES DESDE LE MENU
menu = """----------------------Menu----------------------\n             
1. Circulo \n
2. Cuadrado \n
3. Triángulo equilátero \n
4. Rombo \n
5. Pentágono regular \n
6. Hexágono regular \n

------------------------------------------------
"""
#print(menu)
#option1 = int(input("Seleccione el número de la figura a dibujar: "))
#option2 = int(input("Selecione el número de la figura a ser inscrita: "))
#medidas = int(input("Introduzca la medida en cm para las figuras elegidas: "))
medidas = 3
centimetros = medidas * 44.88

colorCirculo = "#ffff1a"
colorCuadrado = "#ff0080"
colorTriangulo = "#53ff1a"
colorRombo = "#2576C3"
colorPentagono = "#808080"
colorHexagono = "#cd853f"

def Circulo(radio,lapiz):
    circulo = lapiz
    circulo.color("black")
    circulo.circle(radio)   

    
def Cuadrado(lado,lapiz):
    cuadrado = lapiz  
    cuadrado.color("black")
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)


def Triangulo(lado,lapiz):
    triangle = lapiz
    triangle.color("black")
    triangle.forward(lado)
    triangle.left(120)
    triangle.forward(lado)
    triangle.left(120)
    triangle.forward(lado)
    triangle.left(120)

    
def Rombo(lado,lapiz):
    Rombo = lapiz
    Rombo.color("black")
    Rombo.left(60)
    Rombo.forward(lado)
    Rombo.right(120)
    Rombo.forward(lado)
    Rombo.right(60)
    Rombo.forward(lado)    
    Rombo.right(120)
    Rombo.forward(lado)
    Rombo.right(120)


def Pentagono(lado,lapiz):
    Penta = lapiz
    Penta.color("black")
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


def Hexagono(lado,lapiz):
    Hexa = lapiz
    Hexa.color("black")
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
        
                   
lapiz = turtle.Turtle()

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
        lapiz.forward(centimetros*2)
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
        lapiz.forward(centimetros)
        lapiz.left(90)
        lapiz.forward(centimetros)
        lapiz.left(120)
        lapiz.forward(centimetros)
        lapiz.right(300)
        lapiz.pendown()
        Hexagono(lado,lapiz)

    else:
        pass
        
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

#PoligonoInscritoEnCirculo(6,centimetros,lapiz)
#CirculoInscritoEnPoligono(5,centimetros,lapiz)

#Circulo(centimetros,lapiz)
#radio = centimetros

#para cuadrado
"""
lado = math.sqrt(2*(radio**2))
lapiz.left(90)
lapiz.penup()
lapiz.forward(centimetros)
lapiz.left(90)
lapiz.forward(lado/2)
lapiz.left(90)
lapiz.forward(lado/2)
lapiz.left(90)
lapiz.pendown()
Cuadrado(lado,lapiz)
"""

#para triangulo

"""lado = radio*math.sqrt(3)
lapiz.left(90)
lapiz.penup()
lapiz.forward(centimetros*2)
lapiz.right(210)
lapiz.forward(lado)
lapiz.left(120)
lapiz.pendown()
Triangulo(lado,lapiz)
"""

#para el hexagono
"""lado = centimetros
lapiz.left(90)
lapiz.penup()
lapiz.forward(centimetros)
lapiz.left(90)
lapiz.forward(centimetros)
lapiz.left(120)
lapiz.forward(centimetros)
lapiz.right(300)
lapiz.pendown()
Hexagono(lado,lapiz)
"""

#para el pentagono
"""rad = ((72/2)*math.pi) / 180
lado = 2*radio*(math.sin(rad))

lapiz.penup()
lapiz.left(90)
lapiz.forward(centimetros*2)
lapiz.left(126)
lapiz.forward(lado)

lapiz.left(72)
lapiz.forward(lado)
lapiz.left(72)
lapiz.pendown()
Pentagono(lado,lapiz)
"""
#-----------------------------------
#cuadrado con circulo inscrito
"""
Cuadrado(centimetros, lapiz)
lapiz.penup()
lapiz.forward(centimetros/2)
lapiz.pendown()
Circulo(centimetros/2,lapiz)
"""

#triangulo con circulo inscrito

"""Triangulo(centimetros, lapiz)
lapiz.penup()
lapiz.forward(centimetros/2)
lapiz.pendown()

rad = rad = (30*math.pi) / 180
radio = math.tan(rad) * (centimetros/2)
Circulo(radio, lapiz)
"""

"""Pentagono(centimetros, lapiz)
lapiz.penup()
lapiz.forward(centimetros/2)
lapiz.pendown()

rad = rad = (54*math.pi) / 180
radio = math.tan(rad) * (centimetros/2)
Circulo(radio, lapiz)
"""
"""
Hexagono(centimetros, lapiz)
lapiz.penup()
lapiz.forward(centimetros/2)
lapiz.pendown()

rad = rad = (60*math.pi) / 180
radio = math.tan(rad) * (centimetros/2)
Circulo(radio, lapiz)
"""

"""rad = rad = (30*math.pi) / 180
radio = math.sin(rad)*math.cos(rad)*centimetros

Rombo(centimetros, lapiz)
lapiz.penup()
lapiz.forward(centimetros/2)
lapiz.right(90)
lapiz.forward(radio)
lapiz.left(90)
lapiz.pendown()
Circulo(radio, lapiz)
"""
