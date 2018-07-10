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
lineNoPattern= r'\d+'
chittyDatePattern= r'\d{1,2}[/]\d{2}[/]\d{2,4}'
chittyNoPattern= r'NKL \d+'
salaPattern=   r'\d+,\d+,\d+-*'
instPattern= r'\d+/\d+'
apPattern= r'\w+'
payamtPattern=r'\d+,\d+'


#Compile regular expression
lineNo= re.compile(lineNoPattern)
chittyDate= re.compile(chittyDatePattern)
chittyNo= re.compile(chittyNoPattern)
regNo= re.compile(regNoPattern)
sala= re.compile(salaPattern)
inst= re.compile(instPattern)
aucpri= re.compile(apPattern)
payamt= re.compile(payamtPattern)


#Storage of data 
lineNoData=[]
chittyDateData=[]
chittyNoData=[]
regNoData=[]
salaData=[]
aucpriData=[]
payAmtData=[]

#Read the scrapped file data
with open('quotes.json') as D:
  data = json.load(D)

#Loop through the line no of chitty data
  for d in range (int(len(data[1]["noOfChitty"]))):
#Check if the data is of line no format or not,if yes add to the linen o list
    if(lineNo.fullmatch(data[1]["noOfChitty"][d])):
      lineNoData.append(data[1]["noOfChitty"][d])
#Check if the data is matching the date format,if yes add to the chitty date list
    elif(chittyDate.fullmatch(data[1]["noOfChitty"][d])):
      chittyDateData.append(data[1]["noOfChitty"][d])

  for temp in range (int(len(lineNoData))):
    print("\nThe value of  line no is",lineNoData[temp])
  for temp in range(int(len(chittyDateData))):
    print("\n The value[ of chittyDate is",chittyDateData[temp])
