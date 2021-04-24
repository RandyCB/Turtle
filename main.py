import turtle

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

def Circulo(radio, order,lapiz):
    circulo = lapiz
    circulo.color("black")
    circulo.circle(radio)   

    if(order == 1):                                 #si opcion 1 es circulo se debe acomodar el cursor para tal caso
        circulo.left(90)                                
        circulo.penup()
        circulo.forward(radio/2)
        circulo.left(90)
        circulo.forward(radio/2)
        circulo.right(180)
        circulo.pendown()
    else:
        pass
    
def Cuadrado(lado, order,lapiz):
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

    if(order == 1):                                  #si la opcion 2 es circulo para cualquier otra figura el cursor se debe acomodar para tal caso
        cuadrado.penup()
        cuadrado.forward(lado/2)
        cuadrado.right(90)
        cuadrado.forward(lado/2)
        cuadrado.left(90)
        cuadrado.pendown()
    else:
        pass

def Triangulo(lado, order,lapiz):
    triangle = lapiz
    triangle.color("black")
    triangle.forward(lado)
    triangle.left(120)
    triangle.forward(lado)
    triangle.left(120)
    triangle.forward(lado)
    triangle.left(120)


    if(order == 1):                                
        triangle.penup()
        triangle.forward(lado/2)
        triangle.right(90)
        triangle.forward(lado/2)
        triangle.left(90)
        triangle.pendown()
    else:
        pass
    

def Rombo(lado, order,lapiz):
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

    if(order == 1):                                  
        Rombo.penup()
        Rombo.forward(lado/2)
        Rombo.right(90)
        Rombo.forward(lado/2)
        Rombo.left(90)
        Rombo.pendown()
    else:
        pass


def Pentagono(lado, order,lapiz):
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


    if(order == 1):                                  
        Penta.penup()
        Penta.forward(lado/2)
        Penta.right(90)
        Penta.forward(lado/2)
        Penta.left(90)
        Penta.pendown()
    else:
        pass

def Hexagono(lado, order,lapiz):
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

    if(order == 1):                                  
        Hexa.penup()
        Hexa.forward(lado/2)
        Hexa.right(90)
        Hexa.forward(lado/2)
        Hexa.left(90)
        Hexa.pendown()
    else:
        pass
    



#option1 = 1               #circulo x cuadraro
#option2 = 2

#option1 = 1                #circulo x triangulo     #AJUSTAR ALTURA PARA QUE TRIANGULO SE CENTRE EN CIRCULO
#option2 = 3    

option1 = 4                #circulo x rombo     
option2 = 1 





lapiz = turtle.Turtle()

if(option1 == 1):
    Circulo(centimetros,option1,lapiz)

elif(option1 == 2):
    Cuadrado(centimetros, option2,lapiz)

elif(option1 == 3):
    Triangulo(centimetros, option2,lapiz)

elif(option1 == 4):
    Rombo(centimetros, option2,lapiz)

elif(option1 == 5):
    Pentagono(centimetros, option2,lapiz)

elif(option1 == 6):
    Hexagono(centimetros, option2,lapiz)

else:
    pass


if(option2 == 1):
    Circulo(centimetros,0,lapiz)

elif(option2 == 2):
    Cuadrado(centimetros, 0,lapiz)

elif(option2 == 3):
    Triangulo(centimetros, 0,lapiz)

elif(option2 == 4):
    Rombo(centimetros, 0,lapiz)

elif(option2 == 5):
    Pentagono(centimetros, 0,lapiz)

elif(option2 == 6):
    Hexagono(centimetros, 0,lapiz)

else:
    pass




    


