from pymongo import MongoClient
import requests
import time

def obtener_tipo_cambio():

    datos_anuales = []
    
    for mes in range(1, 13):
        url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2023"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
           
            datos_anuales.append(data)
            print(f"Datos obtenidos para el mes {mes}")
       
        time.sleep(5)  
    
    return datos_anuales

def guardar_en_mongodb(data):
    cadena_conexion_mongo = "mongodb+srv://diegoagameroc:HBdzxwNaivNFFFqb@clustermongodb.wdr7m.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDb"
    client = MongoClient(cadena_conexion_mongo)
    db = client['bdSunat']  
    collection = db['sunat_info']  

    # Insertar o actualizar datos
    for item in data:
        collection.update_one(
            {"fecha": item['fecha']}, 
            {"$set": {"compra": item['compra'], "venta": item['venta'], "origen": item['origen'], "moneda": item['moneda']}}, 
            upsert=True
        )
    print("Datos guardados en MongoDB.")

def mostrar_datos_mongodb():
    cadena_conexion_mongo = "mongodb+srv://diegoagameroc:HBdzxwNaivNFFFqb@clustermongodb.wdr7m.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDb"
    client = MongoClient(cadena_conexion_mongo)
    db = client['bdSunat']
    print(db.list_collection_names())

if __name__ == "__main__":
    datos = obtener_tipo_cambio() 
    guardar_en_mongodb(datos)
    mostrar_datos_mongodb()

