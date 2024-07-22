from PyQt6 import uic, QtWidgets
import PySide6.QtSql
import mysql.connector
import mysql

#codigo para cadastro de usuario
#conexao com banco de dado
banco =mysql.connector.connect(
    host =  "%",
    user ="localhost:3307",
    password ="Computacao",
    database ="berna"
)

cursor = banco.cursor(buffered=True) #cria um cursor

cursor.execute("select * from berna")

meuresultado = cursor.fetchall()




#funcao para conferir se o usuario esta ou nao cadastrado

#def funcao_principal():
    
     
