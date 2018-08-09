#This file is used to update the DB with the chitty information

import sqlite3
from readJson import *


def dbCheck():
#Check if the DB exist or not
  try:
    conn = sqlite3.connect('file:chittyData.db?mode=rw',uri=True)
  except sqlite3.OperationalError:
    cIn = sqlite3.connect('chittyData.db')
    cInCur = cIn.cursor()
    cInCur.execute('''CREATE TABLE CHITTYDATA(ID INTEGER PRIMARY KEY AUTOINCREMENT,CHITTYNO INTEGER,CHITTYDATE DATE ,REGNUM INTEGER,SALA INTEGER,INSTALLMENT TEXT,STATUS TEXT,AMOUNT INTEGER) ''')
    cInCur.execute('''CREATE TABLE CHITTYMONTH(ID INTEGER PRIMARY KEY AUTOINCREMENT,MONTH TEXT,COUNT INTEGER)''')
    cIn.commit()
    cIn.close()


def dbUpdate():
#Update the table with the chitty information
  cIn=sqlite3.connect('chittyData.db')
  cInCur = cIn.cursor()
#  try:
#  To retrieve chitty information
#    for d in range(len(chittyDateData)):
#      chittyData =[(None,chittyNoData[d],
#                 chittyDateData[d],
#                 regNoData[d],
#                 salaData[d],
#                 instData[d],
#                 aucpriData[d],
#                 payAmtData[d])]
#      dbCheckIfPresent(chittyNoData[d],chittyDateData[d],regNoData[d],salaData[d],instData[d],aucpriData[d],payAmtData[d])
#  except:
#    cInCur.executemany('INSERT INTO CHITTYDATA VALUES(?,?,?,?,?,?,?,?)',chittyData)
#  cIn.commit()
   
#Update the table with chitty monthly information  
  for chittyCount in itertools.islice(chittyMonthlyCount,0,len(chittyMonthlyCount)-1):
    cCnt = [(None,chittyCount,chittyMonthlyCount[chittyCount])] 
    if not (dbCheckIfPresent(chittyCount,chittyMonthlyCount[chittyCount],cInCur)):
      cInCur.executemany('INSERT INTO CHITTYMONTH VALUES(?,?,?)',cCnt)
  cIn.commit()
  cIn.close()




def dbCheckIfPresent(*args):
#To update the chitty monthly data  
  if len(args) == 3:
    args[2].execute("SELECT COUNT(*) FROM CHITTYMONTH WHERE MONTH = ? and COUNT = ? ",(args[0],args[1]))
    chRes = args[2].fetchone()[0]
    if chRes :
      return 1
    else:
      return 0
#  elif len(args) == 7:
#    print("The function called from chittydata")
#    return 1



def dbDisplay():
#Function used to print and debuging process
  cIn=sqlite3.connect('chittyData.db')
  cInCur = cIn.cursor()
  for row in cInCur.execute('SELECT * FROM CHITTYDATA'):
    print (row)

  for row in cInCur.execute('SELECT * FROM CHITTYMONTH'):
    print(row)

  cIn.close()


def dbUpdateCheck():
  
  dbCheck()
  dbUpdate()
  dbDisplay()
