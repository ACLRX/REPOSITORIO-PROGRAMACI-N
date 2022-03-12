def mcd (a,b):
    resto=0
    while (b>0):
        resto=b
        b=a%b
        a= resto
    return a

def fracc (a,b):    
    n1= int(a/mcd(a,b))
    n2= int (b/mcd(a,b))
    if n2==1:
        return (n1)
    
    return str(n1)+ "/"+str(n2)

def sumafracciones(n1,n2,n3,n4):
    x = n1*n4
    z = n2*n3
    y = n2*n4
    s = x+z
    return str (s)+ "/"+ str(y)

def restafracciones (n1,n2,n3,n4):
    x = n1*n4
    z = n2*n3
    y = n2*n4
    s = x-z
    return  str (s)+ "/"+ str(y)

def multiplicacionfracciones (n1,n2,n3,n4):
    x = n1*n3
    z = n2*n4
    return str (x)+ "/"+ str(z)

def divisionfracciones (n1,d1,n2,d2):
    x = n1*d2
    z = n2*d1
    if d1== 0:
        return ("ERROR")
    if d2== 0:
        return ("ERROR")
    
    return str (x)+ "/"+ str(z)   
    