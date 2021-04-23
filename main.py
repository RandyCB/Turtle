import turtle

""" DUDAS
1. Las medidas para figura 1 y 2 son las mismas
2. se puede seleccionar dos veces la misma figura
3. 
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
medidas = int(input("Introduzca la medida en cm para las figuras elegidas: "))

centimetros = medidas * 44.88

colorCirculo = "#ffff1a"
colorCuadrado = "#ff0080"
colorTriangulo = "#53ff1a"
colorRombo = "#2576C3"

def Circulo(radio):
    circulo = turtle.Turtle()
    circulo.color("black", colorCirculo)
    circulo.begin_fill()
    circulo.circle(radio)
    circulo.end_fill()

def Cuadrado(lado):
    cuadrado = turtle.Turtle()
    cuadrado.color("black", colorCuadrado)
    cuadrado.begin_fill()
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.left(90)
    cuadrado.forward(lado)
    cuadrado.end_fill()

def Triangulo(lados):
    triangle = turtle.Turtle()
    triangle.color("black", colorTriangulo)
    triangle.begin_fill()
    triangle.forward(lados)
    triangle.left(120)
    triangle.forward(lados)
    triangle.left(120)
    triangle.forward(lados)
    triangle.end_fill()

def Rombo(lados):
    Rombo = turtle.Turtle()
    Rombo.color("black", colorRombo)
    Rombo.begin_fill()

    Rombo.left(60)
    Rombo.forward(lados)
    Rombo.right(120)
    Rombo.forward(lados)
    Rombo.right(60)
    Rombo.forward(lados)    
    Rombo.right(120)
    Rombo.forward(lados)
    Rombo.end_fill()


#Circulo(centimetros)
#Cuadrado(centimetros)
#Rombo(centimetos)
