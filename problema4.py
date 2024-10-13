
def Temp():
    path='/workspaces/Pythonn-PC4/temperaturas.txt'

    with open(path,mode='r') as File:
        lineas=File.readlines()

        temperaturas=[]

        for linea in lineas:
            _, temperatura=linea.strip().split(',')
            temperaturax1=float(temperatura)
            temperaturas.append(temperaturax1)

        print(temperaturas)

        temperatura_max=max(temperaturas)
        temperatura_min=min(temperaturas)
        temperatura_prom= sum(temperaturas)/len(temperaturas)
        print(f'Temperatura maxima: {temperatura_max}')
        print(f'Temperatura minima: {temperatura_min}')
        print(f'Temperatura promedio: {temperatura_prom}')

        with open('/workspaces/Pythonn-PC4/resumen_temperaturas.txt',mode='w') as file:
            file.write(f'Temperatura maxima: {temperatura_max}\n')
            file.write(f'Temperatura minima: {temperatura_min}\n')
            file.write(f'Temperatura promedio: {temperatura_prom:.2f}\n')
            print('Se copiaron los datos exitosamente')

if __name__ == "__main__":
    Temp()