import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="your_password",
    database="webphotos"
)
cursor = conn.cursor()