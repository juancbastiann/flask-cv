import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.date.today()
    edad = fecha_actual.year - fecha_nacimiento.year

    if fecha_actual.month < fecha_nacimiento.month:
        edad -= 1
    elif fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day:
        edad -= 1

    return edad

fecha_nacimiento = datetime.date(2003, 4, 7)
edad_actual = calcular_edad(fecha_nacimiento)

def convertir_fecha(fecha):
    meses = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
        7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    
    año, mes, día = fecha
    
    fecha_letras = f"{día} de {meses[mes]} de {año}"
    
    return fecha_letras


fecha_numeros = (2003, 4, 7)
fecha_letras = convertir_fecha(fecha_numeros)
