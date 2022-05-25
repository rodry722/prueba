import datetime
from django.http import HttpResponse

def saludo(self):
    
    documento = """
        <html1>
        <body>
        <h1>
        Hola alumnos
        <h1>
        <body>
        <html>"""
    

    return HttpResponse(documento)

def despedida(self):

    return HttpResponse("Adios alumnos")

def dameFecha(self):
    fechaActual = datetime.datetime.now()

    documento = f"""
    <html1>
    <body>
    <h2>
    Fecha y hora actuales {fechaActual}
    <h2>
    <body>
    <html>"""

    return HttpResponse(documento)

def calculaEdad(self,edad,year):
    
    
    periodo = year - 2022
    edadFutura = edad + periodo
    documento = f"""
    <html1>
    <body>
    <h2>
    En el anio {year} tendras {edadFutura}
    <h2>
    <body>
    <html>"""

    return HttpResponse(documento)
