import os
#clasificacion de estudiantes de acuerdo a puntaje
ls_categoria1 = [] #puntaje (30-50) y edad (15-20)
ls_categoria2 = [] #puntaje (51-80) y edad (21-30)
ls_categoria3 = [] #puntaje (81-100) y edad (31-50)
sw = True
def fnt_limpiar():
    os.system('cls')
    print('\nBienvenido al sistema de calificación de estudiantes')
    print('Autor: Valentina Arias')
    print('Institución: Universidad Católica Luis Amigó')
    print('Categoria I:' , ls_categoria1)
    print('Categoria II:' , ls_categoria2)
    print('Categoria III:' , ls_categoria3)

def fnt_registrar(id, nombre, edad, puntaje):
    if id == '' or puntaje == '' or edad == '' or nombre == '':
        enter = input('Debe ingresar todos los datos <ENTER>')
    else: 
        if id in ls_categoria1: #or ls_categoria2 or ls_categoria3:  #si ese id se encuentra ya registrado
                enter = input('\nEsta persona ya se encuentra categorizada <ENTER>')
        else:
            auxP = int(puntaje) #convierte el dato en entero
            auxE = int(edad) #convierte el dato en entero
            if (auxP >= 30 and auxP <= 50) and (auxE  >= 15 and auxE  <= 20):
                ls_categoria1.append([id,nombre,edad,puntaje])
            elif (auxP >=51 and auxP<= 80) and (auxE >=21 and auxE  <= 30):
                ls_categoria2.append([id, nombre, edad, puntaje])
            elif (auxP >=81 and auxP<= 100) and (auxE  >= 31 and auxE <= 50):
                ls_categoria3.append([id, nombre, edad, puntaje])
                enter = input(f'\nEstudiante {nombre} registrado con éxito')
                
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
        idStr =  input('\nID:  ')
        nombreStr = input('Nombres completos:  ')
        edadInt = input('Edad:   ')
        puntajeInt = input('Puntaje: ')
        fnt_registrar(idStr,nombreStr, edadInt, puntajeInt)
        
        
while sw == True:   
    fnt_limpiar()
    opcionesStr = input('\n\n<<<<<MENÚ PRINCIPAL>>>>>\n\n1. REGISTRAR\n2. CONSULTAR\n\n--> ')
    fnt_selector(opcionesStr)
    