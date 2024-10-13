
import requests
import zipfile

def CapturarImagen():
    url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)

    # wb -> escritura en binario 
    with open('perro.jpg', 'wb') as f:
        f.write(response.content)
        pass

    # ZIP
    zip='archivo.zip'
    with zipfile.ZipFile(zip, 'w') as zipf:
        zipf.write('perro.jpg')

    #Descomprimir Zip
    salida = 'descomprimido'
    with zipfile.ZipFile(zip, 'r') as zipf:
        zipf.extractall(salida)


if __name__ == "__main__":
    CapturarImagen()