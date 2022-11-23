import mysql.connector

conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='baza_danych')
cursor = conn.cursor()

query = "SHOW TABLES LIKE 'staze'"
cursor.execute(query)
result = cursor.fetchall()

if result:
    query = "DROP TABLE staze"
    cursor.execute(query)
    conn.commit()

    query = "CREATE TABLE staze (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, tytul varchar(500) NOT NULL, organizator varchar(100) NOT NULL, rodzaj varchar(50) NOT NULL, zasieg varchar(50) NOT NULL, grupa_docelowa varchar(100) NOT NULL, branza varchar(50) NOT NULL, link varchar(1000) NOT NULL)"
    cursor.execute(query)
    conn.commit()
    def appendStaze(tytul: str, organizator: str, rodzaj: str, zasieg: str, grupa:str, branza: str, link: str):
        try:
            query = "INSERT INTO staze (tytul, organizator, rodzaj, zasieg, grupa_docelowa, branza, link) values(%s, %s, %s, %s, %s, %s, %s)"
            values = (tytul, organizator, rodzaj, zasieg, grupa, branza, link)
            cursor.execute(query, values)
            conn.commit()
        except:
            print("Błąd")
else:
    query = "CREATE TABLE staze (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, tytul varchar(500) NOT NULL, organizator varchar(100) NOT NULL, rodzaj varchar(50) NOT NULL, zasieg varchar(50) NOT NULL, grupa_docelowa varchar(100) NOT NULL, branza varchar(50) NOT NULL, link varchar(1000) NOT NULL)"
    cursor.execute(query)
    conn.commit()
    def appendStaze(tytul: str, organizator: str, rodzaj: str, zasieg: str, grupa:str, branza: str, link: str):
        try:
            query = "INSERT INTO stypendia (tytul, organizator, rodzaj, zasieg, grupa_docelowa, branza, link) values(%s, %s, %s, %s, %s, %s, %s)"
            values = (tytul, organizator, rodzaj, zasieg, grupa, branza, link)
            cursor.execute(query, values)
            conn.commit()
        except:
            print("Błąd")