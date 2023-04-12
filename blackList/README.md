## Microservicio _Gestión de blackLists_

Este microservicio se encarga de la gestión de blackLists (rutas). Dentro de sus funcionalidades se encuentran las siguientes:

- **Creación de blackLists**: Permite a un usuario autenticado, crear blackLists.
- **Búsqueda de blackLists**: Permite buscar blackLists mediante el código del aeropuerto de origen o destino o la fecha del envío. 
- **Consulta de un blackList**: Permite a un usuario autenticado, obtener la información de un blackList.
- **Consulta la salud del microservicio**: Permite verificar si el componente se está ejecutando.

Para mayor información consultar el siguiente enlace de la documentación.

[Documentación de blackLists](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/entrega-1-proyecto-202311/wiki/Gesti%C3%B3n-de-blackLists)


## Estructura
````
├── blackList # Archivos y directorios de la aplicación blackList
|   ├── authentication # Directorio con archivos de autenticación
|   ├── config # Directorio con variables de entorno
|   ├── controllers # Directorio del controlador de la aplicación
|   ├── helpers # Directorio de inicialización de BD
|   ├── models # Directorio del modelo de la aplicación
|   ├── services # Directorio de los metodos de las funcionalidades de la app
|   ├── tests # Directorio de pruebas
|   ├── app.py # Archivo de inicialización de la aplicación
|   ├── database.py # Creación de la base de datos
|   ├── Dockerfile # Archivo de configuración de la imagen del componente
|   ├── Pipfile # Dependencias de la aplicación
|   ├── Pipfile.lock # Archivo lock de dependencias
|   ├── README.md # Archivo con información útil de la aplicación
|   ├── requirements.txt # Archivo de dependencias de la aplicación
|   ├── run_service.sh # Archivo para la ejecución del servicio
````

**Pruebas Unitarias**
---
1) Ejecutar pruebas
```bash
coverage run -m pytest -s tests
```

2) Ejecutar pruebas desde docker compose
```bash
docker-compose exec blackList-microservice coverage run -m pytest -s tests
```

3) Obtener cobertura de pruebas
```bash
coverage report -m
```

4) Obtener cobertura de pruebas desde docker compose
```bash
docker-compose exec blackList-microservice coverage report -m
```