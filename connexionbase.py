import mysql.connector

con = mysql.connector.connect(host="localhost",database="minesoft",user = "root", password = "")
curos = con.cursor()
curos.execute("SELECT * FROM faculte ORDER BY nom_fac ASC")
result = curos.fetchall()

cur = con.cursor()
cur.execute("SELECT * FROM departement_fac ORDER BY nom_dep ASC")
depres = cur.fetchall()

camp = con.cursor()
camp.execute("SELECT * FROM campus")
showcampus = camp.fetchone()

institut = con.cursor()
institut.execute("SELECT * FROM option_institut")

showinstitut = institut.fetchall()



con.commit()
con.close()