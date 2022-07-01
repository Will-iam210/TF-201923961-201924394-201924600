## **1. Resumen Ejecutivo**

El objetivo del presente trabajo es elaborar un grafo para representar a una ciudad en específico. En nuestro caso decidimos optar por la ciudad de La Plata, provincia de Buenos Aires ubicada en Argentina, ya que cuenta con un peculiar diseño en cuadrícula, hecho que nos facilita el identificar las intersecciones entre las diversas calles que componen a esta ciudad. Por otro lado, la generación del grafo será con el lenguaje Python, mediante el cúal se podrá leer la información sobre los nodos y aristas, generados previamente en un archivo de texto, para después representar a la ciudad en formato de lista de adyacencia con nombre **“adjacency_list.txt”**.

## **2. Imagen estática de la ciudad o porción de ciudad elegida**

![Ciudad de La Plata](https://i.imgur.com/SVEbT79.png "Ciudad de La Plata")

_Ciudad de La Plata (Imagen de Google Maps)_

## **3. Descripción de los datos consignados por calle**
En relación a los datos consignados por calle, se decidió crear un archivo de texto por separado en el cual acompañamos el nombre de todas las calles de La Plata con un identificador único o id.

* id: identificador numérico de la calle
* nombre: nombre de calle

**Ejemplo:**

|   id  |   nombre  |
|-------|-----------|
|   7   |Avenida 25 |
|   8   |Avenida 31 |
|   9   |Avenida 32 |
		
**Nota:** El archivo que contiene la información de las calles es **“streets.txt”**

## **4. Descripción de la información consignada por intersección**
Las intersecciones o vértices se generaron a partir de los id de las calles que conforman una intersección, teniendo en cuenta que en algunos casos una intersección podría estar conformada hasta por 4 calles. Asimismo, se consideraron sus coordenadas geográficas obtenidas con Google Maps.

* id: identificador numérico de la intersección
* Latitud: Coordenada geográfica en el eje Y
* Longitud: Coordenada geográfica en el eje X
* N’s: identificadores de las calles que conforman la intersección
  
**Ejemplo:**

|   id  |     Latitud      |    Longitud    |  N1  |  N2  |
|-------|------------------|----------------|------|------|
|   7   |   -34.93315482   |   -57.97989967 |  8   |  11  |
|   8   |   -34.93404178   |   -57.97880845 |  8   |  120 |
|   9   |   -34.93480676   |   -57.97774634 |  8   |  121 |

Donde el nodo 0 tiene por latitud -34.93315482, longitud -57.97989967 y está conformado por las calles con id 8 y 11.

**Nota:**

* El número de calles que conforman una intersección puede ser mayor o igual que 2.
* El archivo que contiene la información de los nodos es **“nodes.txt”**

## **5. Explicación de cómo se elaboró el grafo, qué representan las aristas y los vértices**
El grafo fue elaborado en base a los datos recopilados por cada integrante, para esto se tuvieron que identificar todas las intersecciones existentes en el área de La Plata e incluso los alrededores. Además, se llegó a un consenso de representar a los vértices como la intersección entre dos o más calles y una arista como la conexión entre dos intersecciones, tomando en cuenta la dirección que había entre ellas.

**Representación de aristas:**

* node i: nodo de origen del cual parte una arista
* node j: nodo destino de la arista
  
**Ejemplo:**

| node i| node j|
|-------|-------|
|   504 |   505 |
|   864 |   876 |
|   1002|   892 |

La tabla indica que hay camino del _“node i”_ hacia el _“node j”_.

**Nota:** El archivo que contiene la información de las aristas es **“edges.txt”**.

Luego de este proceso, se construyó la lista de adyacencia, donde, para cada nodo _(nodo i)_, se creará una lista que contiene todos los identificadores de los nodos de llegada _(nodo j)_.

**Ejemplo:**

| nodo i|  Lista nodos j   |
|-------|------------------|
|   1510|[1509, 1511]      |
|   1511|[1510, 1512, 1499]|
|   1512|[1511, 1513, 1500]|

Donde el nodo 1510, por ejemplo, se dirige en el grafo hacia los nodos 1509 y 1511.

**Nota:** El archivo que contiene la información de la lista de adyacencia es **“adjacency_list.txt”**. Este archivo también será generado con el código usando los archivos anteriores.

## **6. Conclusiones**

El objetivo principal del trabajo fue el de construir un sistema que nos permita buscar la ruta más corta entre dos puntos de una ciudad representada por un grafo, para el cual se emplearon algunos de los algoritmos aprendidos en clase. Además, se tuvo que hacer uso de recursos adicionales como Google Maps y Overpass turbo que nos facilitaron en parte la construcción de nuestra lista de adyacencia. Por último, las reuniones constantes con los miembros del equipo fueron de suma importancia para organizarnos mejor, generar ideas de solución y distribuirnos el desarrollo del trabajo con la finalidad de cumplir a tiempo con lo solicitado para cada hito.

## **7. Anexos**

Obtención de la lista de calles en una zona especificada usando OverPass:

![Anexo 1](https://i.imgur.com/Czep97D.png "Anexo 1")

Lista de las calles obtenidas según el área seleccionada:

![Anexo 2](https://i.imgur.com/7vyFGZT.png "Anexo 2")

Prueba de la búsqueda de caminos con la hora con menos tráfico

![Anexo 3](https://i.imgur.com/rlmRfnE.png "Anexo 3")

Prueba de la búsqueda de caminos con la hora con más tráfico

![Anexo 4](https://i.imgur.com/GJtWxfZ.png "Anexo 4")

## **8. Recursos**

* Google Maps. (s. f.). La Plata. Recuperado 26 de mayo de 2022, de https://www.google.com/maps/place/La+Plata,+Provincia+de+Buenos+Aires,+Argentina/@-34.9179402,-57.9603284,13z/data=!4m5!3m4!1s0x95a2e62b1f0085a1:0xbcfc44f0547312e3!8m2!3d-34.9204948!4d-57.9535657 
* Overpass turbo. (s. f.). Overpass Turbo. Recuperado 28 de abril de 2022, de https://overpass-turbo.eu/ 
