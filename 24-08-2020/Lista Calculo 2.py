from math import floor

def ex2():
    horas1 = (8.5*3)*4
    horas2 = (9*2)*4
    tempo = horas1+horas2
    horaTrabalho = 5468/ tempo
    print(floor(horaTrabalho))

def ex3():
    altura_Bruno = 1.75
    peso_Bruno = 85
    IMC_Bruno = (peso_Bruno / (pow(altura_Bruno,2)))
    teto_imc = floor(IMC_Bruno)
    print(teto_imc)

def ex4():
    a = 4/6
    b = 3/2
    c = (a*b)+1
    d = pow(3,2/3)
    e = pow(d,c)
    f = 1.4 + e
    print(round(f,3))
    
def ex5():
    a1 = (-4)**(-5) == pow(-4,-5)
    a2 = -10**0 == pow(-10,0)
    a3 = (4)*(3) == pow(4,3)
    a4 = -4**1/2 == -pow(4,0.5)
    a5 = ((2)**(3))**4 == pow(pow(2,3),4)
    print([n1,n2,n3,n4,n5])
    
def ex6():
    a = 4/6
    a1 = 3/2
    a = (a* a1) + 1
    b = pow(a,3)
    a1 = pow(3,b)
    print(a1)

def ex7():
    print(round(((45/8)**(2+1.5))/(1-(5/7 + 6)/4) + 600))

def ex8():
    a = 4
    b = 2
    c = a/b
    print(type(c))

def ex9():
    a = 4
    b = 2
    c = a + b
    print(type(c))

def ex10():
    a = 4
    b = 2
    c = a + b
    print('type(c)')
    
    
