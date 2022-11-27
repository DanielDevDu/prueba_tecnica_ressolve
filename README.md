# Solución Prueba Tecnica Ressolve

## Parte 1

#### Problema 1:

- Resuelto con "list comprenhension", iteradores y condicionales

#### Problema 2:

- Resuelto con la biblioteca "re" para expresiones regulares

#### Problema 3:

- Resuleto con iteradores

<br/>

## Parte 2

Plantee tres posibles soluciones al resolver el problema, las expongo brevemente con sus ventajas y desventajas:

- Primero unas generalidades que comparten las tres soluciones: - Hay dos clases en cada solución {nombre_solución}ManageData and {nombre_solución}Executer en las que está toda la lógica del programa.
  - En la primera, ManageData mediando los módulos pandas y pickle se leen los archivos, se convierten a Dataframes y se guardan en un archivo con codificación binaria, de donde con un método mismo de esta clase, se puede leer el DataFrame.
  - En la segunda se implementan posibles usos de la primera clase: write(Para leer los archivos y guardar en un archivo), y read(solo para obtener el DataFrame de vuelta).

<br/>

### Soluciones

#### Simple Solution:

- Aquí sólo se usa los conceptos de la programación orientada a objetos. - En caso de haber un archivo .csv o .json que no tengan una estructura correcta, el programa fallará y dentendrá su ejecución.

#### Thread Solution:

- Se hace uso de la clase Thread de la cual hereda ManageData y mediante la customización del método run se implemente la lectura(de los .csv y .json) y escritura de los datos.
- En Executer se hace uso del método start para ejecutar un hilo por cada archivo
- En caso de haber un archivo .csv o .json que no tenga la estructura correcta, el programa no fallará, continuará su ejecución, y completará el proceso, pero los errores deben ser manejados

#### Thread Pool Solution:

- Se hace uso de los conceptos de OOP igual que en simple solution
- Se implementa ThreadPoolExecuter para ejecutar un hilo por cada archivo igual que en Thread Solution
- En caso de error en los archivos, el programa no fallará y completará el proceso, además, maneja los errores internamente.
- Se abstrae mediante los método map y submit la ejecución de procesos, no como en el caso de thread_solution que debemos usar iteradores.

#### Tiempo de ejecución:

| Solución      | Seconds    | Seconds(With Error) |
| ------------- | ---------- | ------------------- |
| `Simple`      | **0.1554** | **Falla**           |
| `Thread`      | **0.1733** | **0.1839**          |
| `Thread Pool` | **0.1554** | **0.1523**          |

### Anotaciones:

- Se podrían intentar otras soluciones como asyncronismo o Paralelismo
- No se manejan todos los errores
- Al momento de probar cada solución, elimine el archivo dataframe.pkl
- Como prueba de error hay un archivo en la carpeta pruebas 00000.csv que está vacío, simple_solution fallará, thread_solution mostrará el error por consola, thread_pool_solution no mostrará error.
- La clase ConfigFile lee el archivo config_file.json y también lo actualiza el número de "jobs" port archivo.

### Author

- Daniel Duarte
