import requests

def ConseguirDataBitcoin():
    url="https://api.coindesk.com/v1/bpi/currentprice.json"
    response=requests.get(url)

    data=response.json()

    precioDolar=data['bpi']['USD']['rate_float']
    return precioDolar

def Bitcoins():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))

        total = ConseguirDataBitcoin() * n
        print(f"El costo actual de {n} Bitcoins es: ${total:,.4f}")
    except requests.RequestException:
        print("Hubo un error al obtener los datos")
    except ValueError:
        print("Ingrese un valor válido")

if __name__ == "__main__":
    Bitcoins()