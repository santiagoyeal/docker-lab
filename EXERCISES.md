# Ejercicios básicos para el lab

Este documento describe una serie de ejercicios sencillos que puedes realizar utilizando la base de datos PostgreSQL que levanta el laboratorio y el pequeño módulo Python incluido. Puedes adaptarlos a tus necesidades y añadir más.

## Conexión
1. Arrancar los contenedores:
   ```sh
   cd /Users/santiago/Documents/Dev/dev-labs/docker-lab
   docker compose up --build
   ```
2. Alternativamente, conéctate desde el host a la base de datos con cualquier cliente SQL:
   ```sh
   psql "postgresql://labuser:labpassword@localhost:5432/labdb"
   ```

## Ejercicios SQL (desde psql u otro cliente)

1. **Crear tablas adicionales**
   - Crear una tabla `categories` con campos `id SERIAL PRIMARY KEY` y `name TEXT UNIQUE NOT NULL`.
   - Añadir una columna `category_id` en la tabla `items` que referencie a `categories(id)`.
   - Insertar varias categorías y actualizar los ítems existentes para asociarlos.

2. **Consultas básicas**
   - Seleccionar todos los `items` junto con el nombre de su categoría usando `JOIN`.
   - Contar cuántos `items` hay por categoría.
   - Encontrar el ítem con mayor `quantity`.

3. **Operaciones de agrupación y agregación**
   - Calcular la suma total de `quantity` de todos los ítems.
   - Promedio de `quantity` por categoría.

4. **Transacciones y bloqueo**
   - Iniciar una transacción, actualizar la cantidad de un ítem y hacer rollback.
   - Simular un bloqueo compartido/escrito en dos sesiones diferentes.

5. **Funciones y triggers**
   - Crear una función PL/pgSQL que loguee en otra tabla cada vez que se inserte un `item` nuevo.
   - Añadir un trigger `AFTER INSERT` que invoque la función.

## Ejercicios Python (modificando `app/main.py` o creando nuevos módulos)

1. **CRUD completo desde Python**
   - Usar la clase `Database` para implementar una función `find_item(name)` que retorne un ítem concreto.
   - Añadir un método `delete_all()` y probarlo.

2. **Inserción masiva**
   - Crear un script que lea datos desde un CSV y los inserte en la tabla `items` usando `executemany` o un `COPY`.

3. **Consultas dinámicas**
   - Implementar un método que acepte criterios opcionales (por ejemplo, `min_quantity`) y construya la consulta en función de ellos.

4. **Manejo de errores y reconexión**
   - Probar qué ocurre cuando la conexión se corta (detener el contenedor `db` manualmente) y manejar la excepción para intentar reconectar.

5. **Migraciones simples**
   - Añadir un pequeño sistema de versiones de esquema: una tabla `migrations` que almacene qué scripts ya han sido ejecutados. Escribe un par de scripts SQL en `migrations/` y un método Python que aplica solo los pendientes.

6. **API web (opcional)**
   - Usar Flask o FastAPI en el contenedor `app` para exponer endpoints que realicen operaciones sobre la tabla `items`.
   - Documentar en el README cómo construir la imagen, exponer puertos y probar la API usando `curl` o `httpie`.

## Ejercicios adicionales de Python puro

Además de las interacciones con la base de datos, puedes aprovechar el contenedor `app` para practicar algoritmos y ejercicios de programación en Python. Edita `app/main.py` o crea nuevos scripts dentro de `app/`.

1. **Fibonacci**
   - Implementa una función que calcule los primeros `n` términos de la serie de Fibonacci de forma iterativa y otra de forma recursiva.
   - Haz que el programa imprima la lista de términos o el `n`-ésimo término.

2. **Números primos**
   - Escribe una función que determine si un número dado es primo.
   - Genera todos los primos menores que un cierto límite usando el método de la "criba de Eratóstenes".

3. **Factorial y combinaciones**
   - Implementa una función para calcular el factorial de un número.
   - Usando el factorial, crea otra función que calcule combinaciones `C(n, k)`.

4. **Ordenamiento**
   - Crea implementaciones simples de los algoritmos de ordenamiento: burbuja, inserción y selección.
   - Genera una lista aleatoria y ordénala con cada uno, mostrando el tiempo tomado.

5. **Uso de la base de datos para almacenar resultados**
   - Combina estos ejercicios con la base de datos: por ejemplo, guarda en la tabla `items` los resultados de la serie de Fibonacci (nombre "fib_{n}" y cantidad igual al valor).
   - Otro ejercicio: crea una tabla `calculations` que registre el tipo de cálculo y el resultado, e inserta allí cada vez que ejecutes una función matemática.

6. **Pequeño juego o script de texto**
   - Implementa un menú en la línea de comandos que permita al usuario elegir qué ejercicio ejecutar (Fibonacci, primo, factorial, etc.) y muestre el resultado.

Estos ejercicios proporcionan práctica con la lógica de programación y pueden integrarse al contenedor para ejecutarse dentro del lab.

## Extensiones

- Añadir un contenedor extra al `docker-compose.yml` con un cliente administrable como pgAdmin o Adminer.
- Implementar un contenedor que ejecute un job periódico (cron) para archivar datos antiguos.

Puedes usar estos ejercicios como punto de partida y ampliar con tus propios retos.
