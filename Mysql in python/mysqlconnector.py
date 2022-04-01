import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user ="root",
    password ="Piyush@113"
)



# creating the databse
cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE mysql_basic")
