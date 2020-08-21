ex1 = pow(2,3)
ex2 = pow(-2,3)
ex3 = pow(1,0)
ex4 = pow(-1,0)
ex5 = pow(2,0)
ex6 = pow((2/5),3)
ex7 = pow(3,-2)
ex8 = pow((1/2),-3)
a = pow((-1),3)
ex9 = pow(a,4)
ex10 = pow(0.5,3)
ex11 = pow(0.25,4)
ex12 = pow(0,4)
ex13 = 1+ pow(0.41,2)
ex14 = 1/4 + pow(5,2) - (pow(2,-4))
ex15 = pow(2,-3) + pow(-4,-5)
ex16 = pow((4/5 - 1/2 + 1),-2) + (1 / (1+pow(3,2) - pow(4-5,-2)))

exs = [ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11,ex12,ex13,ex14,ex15,ex16]

i = 0
while i <= 16:
    print( "O resultado do Exercicio " + str(i+1) +" foi: "+ str(exs[i]))
    i += 1


        
