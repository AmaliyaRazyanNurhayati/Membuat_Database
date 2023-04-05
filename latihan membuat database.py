#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect('d3_ti_2023')

print ("Opened database successfully")


# In[14]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# preparing cursor
cursorObject = dataBase.cursor()

# drop table if it exists
cursorObject.execute("DROP TABLE IF EXISTS Mahasiswa")

# creating table
studentRecord = """CREATE TABLE Mahasiswa (
                  NIM VARCHAR(10) NOT NULL,
                  NAMA VARCHAR(30),
                  ALAMAT VARCHAR(255),
                  MATA_KULIAH VARCHAR(10),
                  KELAS VARCHAR(10),
                  DOSEN_PEMBIMBING VARCHAR(30),
                  TAHUN_MASUK INT
                  )"""

# table created
cursorObject.execute(studentRecord)

# disconnect
dataBase.close()


# In[18]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# preparing cursor
cursorObject = dataBase.cursor()

# drop table if it exists
cursorObject.execute("DROP TABLE IF EXISTS Dosen")

# creating table
studentRecord = """CREATE TABLE Dosen (
                  NIP VARCHAR (20) NOT NULL,
                  NAMA_DOSEN VARCHAR (50),
                  MATA_KULIAH_YANG_DIAJAR VARCHAR (50),
                  TAHUN_MENGAJAR INT,
                  BANYAK_KELAS_YANG_DIAJAR INT,
                  TAHUN_PENSIUN INT,
                  ALAMAT VARCHAR (50)
                  )"""

# table created
cursorObject.execute(studentRecord)

# disconnect
dataBase.close()


# In[20]:


# preparing cursor
cursorObject = dataBase.cursor()

# drop existing table
cursorObject.execute("DROP TABLE IF EXISTS Mata_Kuliah")

# creating table
studentRecord = """CREATE TABLE Mata_Kuliah (
                  KODE_MATKUL VARCHAR (10),
                  NAMA_MATKUL VARCHAR (50),
                  WAKTU DATE,
                  RUANGAN VARCHAR (10),
                  DOSEN_PENGAMPU VARCHAR (50),
                  SKS INT
                  )"""

# table created
cursorObject.execute(studentRecord)

# disconnect
dataBase.close()


# In[31]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, NAMA_DOSEN, MATA_KULIAH_YANG_DIAJAR, TAHUN_MENGAJAR, BANYAK_KELAS_YANG_DIAJAR, TAHUN_PENSIUN, ALAMAT) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [("236795430", "Yusuf Fadillah", "Phyton", "2019", "2", "2057", "Madiun"),
       ("236795432", "Darmawan", "Kewirausahaan", "2016", "2", "2050", "Karanganyar"),
       ("236795433", "Fendi Aji", "Mikrokontroller", "2012", "2", "2045", "Solo"),
       ("987643289", "Masbahah", "Basis Data", "2015", "2", "2048", "Jiwan"),
       ("236795434", "Trisna Ari", "Statistika", "2020", "2", "2050", "Jogja")
      ]

cursorObject.executemany(sql, val) # execute many instead of execute
dataBase.commit()

# disconnect
dataBase.close()


# In[33]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# preparing cursor
cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_Kuliah (KODE_MATKUL, NAMA_MATKUL, WAKTU, RUANGAN, DOSEN_PENGAMPU, SKS)VALUES (%s, %s, %s, %s, %s, %s)"
val = [("12345678", "Phyton", "2023-4-7", "L2R3", "Yusuf Fadilla", "2"),
       ("11223344", "Kewirausahaan", "2023-4-8", "L2R2", "Darmawan", "2"),
       ("55667788", "Mikrokontroller", "2023-4-9", "Lab.Mikro", "Fendi Aji", "2"),
       ("12233445", "Basis Data", "2023-4-10", "2015", "Masbahah", "2"),
       ("13151718", "Statistika", "2023-4-11", "2020", "Trisna Ari", "2")
      ]

cursorObject.executemany(sql, val) # execute many instead of execute
dataBase.commit()

# disconnect
dataBase.close()


# In[35]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# preparing cursor
cursorObject = dataBase.cursor()

query = "SELECT NAMA_MATKUL, DOSEN_PENGAMPU FROM Mata_Kuliah"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

dataBase.commit()
dataBase.close()


# In[ ]:




