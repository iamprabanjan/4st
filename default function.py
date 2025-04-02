userinput1=int(input("Enter some numbers :"))
userinput2=int(input("Enter some numbers:"))
userinput3=int(input("Enter some numbers:"))
def dataanalyzer(x,y,z):
    numberList=[]
    #to store a input value to use min(),max(),sorted(),default functions
numberList.append(x)
numberList.append(y)
numberList.apend(z)
average=round(((x+y+z)/3),2)
aboveAverage=0
if(x>average):
    aboveAverage+=1
elif(y>average):
    aboveAverage+=1
elif(z>average):
    aboveAverage+=1
    total=x+y+zip
minnimum=min(numberList)
maximum=max(numberList)
sort=sorted(numberList)
numericDict= { "sum":total,
                "min":minimum,
                "max":maximum,
                 "average":average,
                 "above average":
aboveAverage,
               
                "sorted":sort}
print(numericDict)
                
                     
