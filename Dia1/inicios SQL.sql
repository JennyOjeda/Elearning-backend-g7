-- SQL > Structured Query Language (lenguaje de consultas estructuradas)
-- Registros > conjunto de datos
-- Dato > un valor que por si solo no da una buena referencia 
-- Las BD estan compuestas por una o varias tablas y cada tabla puede contener uno o varios registros
-- varios registros
-- en el lenguaje de baase de datos siempre tenemos que colocar ";2 asi se da cuenta que la instruccion se ha terminado

CREATE DATABASE prueba;
-- Sirve para indicar en que BD queremos trabajar
USE prueba;

CREATE TABLE producto(
	-- obligatoriamente para crear un tabla debemos crear al menos una columna
	-- Solamente se puede usar UNA VEZ el auto-incrementable por tabla 
	-- Primary Key > inidcamos que esta columna se comportara como la identificadora 
	-- de todo este registro
	-- Nombre | Tipo de dado| [configuracion adicional]
	id INT AUTO_INCREMENT PRIMARY KEY, 
	nombre VARCHAR(50),
	fecha_vencimiento DATE
);
-- DML Data Manipulation Language (Lenguaje de manipulacion de datos)
-- Con esto extraigo, inserto, actualizar y elimono la informacion de la base de data 
-- INSERT (INSETO NUEVA INFORMACION)
INSERT INTO producto(id, nombre, fecha_vencimiento) VALUES (DEFAULT, 'Aguaymanto', '2022-07-01');

INSERT INTO producto(id, nombre, fecha_vencimiento) VALUES (DEFAULT, 'Cebolla', '2022-07-10'),
														   (DEFAULT, 'Limon', '2022-06-30');

-- SELECT 
-- Al momento de insertar registros y si estamos manejando el autoincrementador y al momento de realizar 
-- un registro este fallece el incrementador incrementa
SELECT nombre, fecha_vencimiento, id FROM producto;

SELECT * FROM producto; 

SELECT nombre, fecha_vencimiento AS 'fecha de vencimiento', id FROM producto;

-- con la clausula de condicion WHERE indicaremos  un filtro para los resultados, esta es la mejor forma 
-- de poder hacer busquedas y es recomendable hacerlas a nivel de BD
SELECT * FROM producto WHERE nombre = 'cebolla';

-- AND > todas las condiciones tienen que ser Verdaderas
SELECT * FROM producto WHERE nombre = 'Cebolla' AND id = 1;

-- OR > cualquiera de las dos condiciones tiene que ser verdadera 
SELECT * FROM producto
WHERE nombre = 'Cebolla' OR id = 1 OR 
        (id = 7 AND
        nombre = 'Limon'); 

SELECT * FROM producto WHERE nombre LIKE '%a%'; 
SELECT * FROM producto WHERE nombre LIKE '___a%';

-- UPDATE > sirve para actualizar uno o varios registros dependiendo de su condicional
UPDATE producto SET nombre = 'Cebolla China' WHERE nombre = 'Cebolla';

-- Desactivar el modo seguro que lo que hace es que ahora podamos hacer actualizaciones sin 
-- necesidad de tener en la condicion a unacolumna UNIQUE o que sea una Key
-- No se recomienda desactivar porque podria llevar a  hacer modificaciones
-- masivas sin la posibilidad de deshacer esos cambios 

SET SQL_SAFE_UPDATES = false;



-- DDL Data Definition Language( Lenguaje de definicion de datos)
-- Definir la estructura que vamos a manejar en la base de datos(crear, modificar, y eliminar una tabla de BD)
