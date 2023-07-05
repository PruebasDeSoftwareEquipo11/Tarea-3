# Tarea-3
## Instalación y librerias
- **Python 3.10** para la creación del programa, instalada desde el sitio oficial de Python.
- **pytest** para el testing unitario. Para el uso de pytest, es necesario instalarlo usando ```pip install pytest```
- **pytest-cov** para determinar la cobertura del código. Para el uso de pytest-cov, es necesario instalarlo usando ```pip install pytest-cov```

Para hacer el testing con cobertura usando "pytest" y "pytest-cov", se tiene que escribir en consola ```pytest --cov=tienda --cov-fail-under=70```, donde hacemos la verificación de que la cobertura sea sobre 70%.
## Como correr el código:
### Para iniciar la tienda:
- ```python tienda.py``` |  ```python3 tienda.py```
### Para iniciar los test:
- ```pytest -v```
## Tienda:
- Para ingresar como administrador, se debe colocar la opción "1" cuando uno ingrese y una clave "1234".
## Supuestos:
- Se considera que **Vender** se refiere a comprar más stock de juegos en el inventario.
- Se considero que al obtener nuevas copias de juegos no existentes en la tienda, los costos para comprar el juego equivale al costo de obtenerlo más un 20% de ese precio.
- Hay solamente un tipo de administrador con clave: "1234"

## Link de video:
