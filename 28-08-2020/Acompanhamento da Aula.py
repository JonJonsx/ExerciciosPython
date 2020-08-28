def ex1():
    conjunto_processador = {'CPU','Registrador','Core'}
    print(conjunto_processador)
    
def ex2():
    conjunto_processador = set(['CPU','Registrador','Core'])
    print(conjunto_processador)

def ex3():
    lista_processador = {'CPU','Registrador','Core','CPU'}
    conjunto_processaor2 = set(lista_processador)
    print(conjunto_processaor2)
    
print("\n------------------------------")
print("Operação de união")
print("------------------------------\n")

def ex4():
    user_Thor = {'mysql','CPU','RAM','SSD1','Google'}
    user_Thanos = {'LoL','RAM','CPU','HD','Google'}
    user_CA = {'mysql','Lol','RAM','CPU','Firefox'}
    user_TS = {'mysql','CPU','RAM','SSD1','Google'}
    inventario1 = user_Thor | user_CA
    print(inventario1)

ex4()
