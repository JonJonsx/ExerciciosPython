import psutil

def dados():
    print("Retorna os tempos de CPU: {valor}".format(valor = psutil.cpu_times()))
    print("\n----------------------------------------------------------------------\n")
    print("psutil.cpu_percent(interval=1) Retorna: {valor}".format(valor =  psutil.cpu_percent(interval=1)))
