names=["H","C","N","O","P","S"]
masses=[1.00794,12.0107,14.00674,15.9994,30.973761,32.066]
Dict2={}
for i in range(len(names)):
    Dict2[names[i]]=names[i]
print(Dict2)

def molemass(x):
    totalmass=0
    for i in x:
        if i=="H":
            totalmass+=masses[0]
        elif i=="C":
            totalmass+=masses[1]
        elif i=="N":
            totalmass+=masses[2]
        elif i=="O":
            totalmass+=masses[3]
        elif i=="P":
            totalmass+=masses[4]
        elif i=="S":
            totalmass+=masses[5]
    return totalmass
x= "HCNOPS"
value=molemass(x)
print(value)