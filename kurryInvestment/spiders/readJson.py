# lineno: Can be numeric value or date format stuff
# chittyDate: Can be date format or Alpha numeric stuff[eg:NKL 18]
# chittyNo: Can be alpha numeric stuff[eg:NKL 18] or numeric value[18/15]
# regNo	:Can be numeric value[18/19] or amount format[eg:5,00,000/-]
# Sala:Can be amount format[eg:1,00,000] or numeric value[35/40]
# Inst:Can be numeric value[eg:35/40] or String[Auction/Prize]]
# Auction/Prize: Can be a string or numeric value[5,708]
# Amount pay: Can be numeric value or null

import json
import re

#Pattern setup
regNoPattern = r'\d+/\d+'
lineNoPattern= r'(\d+)|( \d+)'
chittyDatePattern= r'(\d{1,2}[/]\d{2}[/]\d{2,4}[(]\d{1,2}[/]\d{1,2}[)]|\d{1,2}[/]\d{2}[/]\d{2,4})'
chittyNoPattern= r'(NKL\d+|NKL \d+)'
salaPattern=   r'\d+,\d+,\d+-*'
instPattern= r'\d+/\d+'
apPattern= r'(Auction|Prize)'
payamtPattern=r'\d+,\d+'
tempChittyNoPattern = r'NKL'
tempNoPattern = r' \d+'
tempDatePattern= r'[/]\d{2}[/]\d{2,4}'

#Compile regular expression
lineNo= re.compile(lineNoPattern)
chittyDate= re.compile(chittyDatePattern)
chittyNo= re.compile(chittyNoPattern)
regNo= re.compile(regNoPattern)
sala= re.compile(salaPattern)
inst= re.compile(instPattern)
aucpri= re.compile(apPattern)
payamt= re.compile(payamtPattern)
tempChitty= re.compile(tempChittyNoPattern)
tempNo= re.compile(tempNoPattern)
tempDate= re.compile(tempDatePattern)


#Storage of data 
lineNoData=[]
chittyDateData=[]
chittyNoData=[]
regNoData=[]
salaData=[]
instData=[]
aucpriData=[]
payAmtData=[]

def lineNoFilter(data):
#Loop through the line no of chitty data
  for d in range (int(len(data[1]["noOfChitty"]))):
#Check if the data is of line no format or not,if yes add to the linen o list
    if(lineNo.fullmatch(data[1]["noOfChitty"][d])):
      lineNoData.append(data[1]["noOfChitty"][d])
#Check if the data is matching the date format,if yes add to the chitty date list
    elif(chittyDate.fullmatch(data[1]["noOfChitty"][d])):
      chittyDateData.append(data[1]["noOfChitty"][d])

def chittyDateFilter(data):
#Loop through the line no of chitty date data
  for d in range (int(len(data[1]["monthInfo"]))):
#Check if the data is of date format or not,if yes add to the date list
    if(chittyDate.fullmatch(data[1]["monthInfo"][d])):
      chittyDateData.append(data[1]["monthInfo"][d])
#Code to handle the special case of Date format not proper,the date field was split    
    elif(lineNo.fullmatch(data[1]["monthInfo"][d]) and tempDate.fullmatch(data[1]["monthInfo"][d+1])):
      chittyDateData.append(data[1]["monthInfo"][d] +data[1]["monthInfo"][d+1])
#Check if the data is matching the chitty number  format,if yes add to the chitty number list
    elif(chittyNo.fullmatch(data[1]["monthInfo"][d])):
      chittyNoData.append(data[1]["monthInfo"][d])
#Code to handle the special case of chitty no,chity no and description are in different line
    elif( tempChitty.fullmatch(data[1]["monthInfo"][d]) and lineNo.fullmatch(data[1]["monthInfo"][d+1])):
      chittyNoData.append(data[1]["monthInfo"][d]+data[1]["monthInfo"][d+1])

def chittyNoFilter(data):
#Loop through the line no of chitty no  data
  for d in range (int(len(data[1]["chittyNo"]))):
    print("\nThe value under consideration is for chitty no",data[1]["chittyNo"][d])
#Check if the data is of chitty no,if yes add to the chity no list
    if(chittyNo.fullmatch(data[1]["chittyNo"][d])):
      chittyNoData.append(data[1]["chittyNo"][d])
#Check if the data is matching the chitty regno,if yes add to the reg  number list
    elif(regNo.fullmatch(data[1]["chittyNo"][d])):
      regNoData.append(data[1]["chittyNo"][d])


def chittyRegNoFilter(data):
#Loop through the line no of chitty data
  for d in range (int(len(data[1]["regNo"]))):
#Check if the data is of chitty reg no,if yes add to the chitty reg  no list
    if(regNo.fullmatch(data[1]["regNo"][d])):
      regNoData.append(data[1]["regNo"][d])
#Check if the data is matching the chitty sala no,if yes add to the sala  list
    elif(sala.fullmatch(data[1]["regNo"][d])):
      salaData.append(data[1]["regNo"][d])

def chittySalaFilter(data):
#Loop through chitty sala data
  for d in range (int(len(data[1]["sala"]))):
#Check if the data is of chitty sala,if yes add to the chitty sala list
    if(sala.fullmatch(data[1]["sala"][d])):
      salaData.append(data[1]["sala"][d])
#Check if the data is matching the chitty inst,if yes add to the chitty inst
    elif(inst.fullmatch(data[1]["sala"][d])):
      instData.append(data[1]["sala"][d])



def chittyInstFilter(data):
#Loop through chitty inst data
  for d in range (int(len(data[1]["inst"]))):
#Check if the data is of chitty inst,if yes add to the chitty inst list
    if(inst.fullmatch(data[1]["inst"][d])):
      instData.append(data[1]["inst"][d])
#Check if the data is matching the chitty payment status,if yes add to the chitty status
    elif(aucpri.fullmatch(data[1]["inst"][d])):
      aucpriData.append(data[1]["inst"][d])

def chittyPayFilter(data):
#Loop through chitty payment status data
  for d in range (int(len(data[1]["chittyStatus"]))):
#Check if the data is of chitty payment statust,if yes add to the chitty payment status list
    if(aucpri.fullmatch(data[1]["chittyStatus"][d])):
      aucpriData.append(data[1]["chittyStatus"][d])
#Check if the data is matching the chitty payment amount,if yes add to the chitty payment amount list
    elif(payamt.fullmatch(data[1]["chittyStatus"][d])):
      payAmtData.append(data[1]["chittyStatus"][d])




def chittyPayAmtFilter(data):
#Loop through chitty payment amount  data
  for d in range (int(len(data[1]["chittyAmount"]))):
#Check if the data is matching the chitty payment amount,if yes add to the chitty payment amount list
    if(payamt.fullmatch(data[1]["chittyAmount"][d])):
      payAmtData.append(data[1]["chittyAmount"][d])


with open('quotes.json') as D:
  data = json.load(D)
  chittyPayAmtFilter(data)
  chittyPayFilter(data)
  chittyInstFilter(data)
  chittySalaFilter(data)
  chittyRegNoFilter(data)
  chittyNoFilter(data)
  chittyDateFilter(data)
  lineNoFilter(data)
for i in range(int(len(chittyNoData))):
  print("The value is",chittyNoData[i])

print("\nThe value of chitty payAmount is",len(payAmtData),payAmtData[20])
print("The value of chitty Chitty status is",len(aucpriData),aucpriData[20])
print("\nThe value of chitty install is",len(instData),instData[20])
print("\nThe value of chitty sala is",len(salaData),salaData[20])
print("\nThe value of chitty regno is",len(regNoData),regNoData[20])
print("\nThe value of chitty no is",len(chittyNoData),chittyNoData[20])
print("\nThe value of chitty Date is",len(chittyDateData),chittyDateData[20])


