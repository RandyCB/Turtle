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


    
def FigInscritaCirculo(opcion2, radio):
    if(opcion2 == 2):
        lado = math.sqrt(2*(radio**2))
        return lado
    elif(opcion2 == 3):
        lado = radio*math.sqrt(3)
        return lado
    elif(opcion2 == 5):
        lado = radio
        return lado
    elif(opcion2 == 6):
        rad = ((72/2)*math.pi) / 180
        lado = 2*radio*(math.sin(rad))
        return lado
    else:
        pass
        

lapiz = turtle.Turtle()

Circulo(centimetros,lapiz)
radio = centimetros

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

