from tarfile import PAX_NAME_FIELDS


file = open('alumnos.txt', 'w')
lista_alumnos = []
hay_mas = 'si'
while hay_mas == 'si':
    alumno = input('ingrese el nombre del alumno: ')
    lista_alumnos.append(alumno)
    hay_mas = input('hay mas alumnos?: ')

for alumno in lista_alumnos:
    file.write(alumno +',')

file.close() 

