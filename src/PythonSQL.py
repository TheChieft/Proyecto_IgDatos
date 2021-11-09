
# -*- coding: utf-8 -*-


import psycopg2
from PythonConnect import Connection

con = Connection()
con.openConnection()

try:
    sql1 = """select *
         from PUBLIC.departamento;"""
    sql2 = """select *
         from PUBLIC.municipio;"""
    sql3 = """select *
         from PUBLIC.tipo_arma;"""
    sql4 = """select *
         from PUBLIC.genero_victimario;"""
    sql5 = """select *
         from PUBLIC.grupo_etario;"""
    sql6 = """select *
         from PUBLIC.tipo_homicidio;"""
    sql7 = """select *
         from PUBLIC.homicidios_colombia;"""
    

#Se ejecuta la sentencia para mostrar los nombres de los países
    
        
    cursor = psycopg2.connect.cursor()
    cursor.execute(sql1)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("Codigo_Dane_Departamento ", row[0])
            print("Nombre_Departamento ", row[1])
            print("\n")
    
    
    cursor = con.cursor()   #no se si este sobre
    cursor.execute(sql2)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("Codigo_Municipio_Dane ", row[0])
            print("Nombre_Muncipio ", row[1])
            print("Codigo_Dane_Departamento: ", row[2])
            print("\n")
            
    cursor = con.cursor()   #no se si este sobre
    cursor.execute(sql3)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("ID_tipo_arma ", row[0])
            print("Nombre_arma ", row[1])
            print("\n")
    
    cursor = con.cursor()   #no se si este sobre
    cursor.execute(sql4)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("ID_genero_victimario ", row[0])
            print("Nombre_genero ", row[1])
            print("\n")
            
    cursor = con.cursor()   #no se si este sobre
    cursor.execute(sql5)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("ID_grupo_etario ", row[0])
            print("Nombre_grupo_etario ", row[1])
            print("\n")
            
    cursor = con.cursor()   #no se si este sobre
    cursor.execute(sql6)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("ID_tipo_homicidio ", row[0])
            print("Nombre_tipo_homicidio ", row[1])
            print("\n")
            
    cursor = con.cursor()   #no se si este sobre
    cursor.execute(sql7)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
            print("ID_caso ", row[0])
            print("Fecha_homicidio ", row[1])
            print("Numero_Victimas ", row[2])
            print("ID_tipo_homicidio ", row[3])
            print("ID_tipo_arma ", row[4])
            print("ID_genero_victimario ", row[5])
            print("ID_grupo_etario_victimario ", row[6])
            print("Codigo_Dane_municipio ", row[7])  #no puse foreign key
            print("\n")
    
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)



con.closeConnection()
