# MICROSERVICIO DE ENTRADAS

## Tecnologias

  * Python 3.7
  * Unittest
  * Flask
  * AWS Pipeline (Despliegue)
  * Circle CI (Chequeo tests)
 
## Estandar V1
  * GET
        
```
/api/v1/entrada

```
 * POST
 ```
/api/v1/entrada

```



## GET "/Api/v1/entrada/AAAA-MM-DD/AAAA-MM-DD" Response Body (200)
```
[
{
    vuelo: String
    fecha: String "AAAA-MM-DDTHH:MM:SS.000Z"
    retraso_horas: Number
    origen_ciudad: String
    internacional: True|False
    aerolinea:String
    pasajeros: Number
    avion: String
    escala: True|False
{,
...
]
```
## POST "/Api/v1/entrada" Request Body
```
{
    vuelo: String
    fecha: String "AAAA-MM-DDTHH:MM:SS.000Z"
    retraso_horas: Number
    origen_ciudad: String
    internacional: True|False
    aerolinea:String
    pasajeros: Number
    avion: String
    escala: True|False
{
```
## POST "/Api/v1/entrada" Response Status
    HTTP STATUS : 201 Created