SELECT schema_name
FROM information_schema.schemata;

SELECT datname FROM pg_database WHERE datistemplate = false;

CREATE table utec.usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    fecha_registro DATE DEFAULT CURRENT_DATE
);


SET search_path TO utec;


CREATE TABLE autores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    nacionalidad VARCHAR(50)
);

CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    anio_publicacion INT,
    genero VARCHAR(50),
    stock INT DEFAULT 1
);

CREATE TABLE libro_autor (
    libro_id INT REFERENCES libros(id),
    autor_id INT REFERENCES autores(id),
    PRIMARY KEY (libro_id, autor_id)
);

CREATE TABLE prestamos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id),
    libro_id INT REFERENCES libros(id),
    fecha_prestamo DATE DEFAULT CURRENT_DATE,
    fecha_devolucion DATE
);

CREATE TABLE comentarios (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id),
    libro_id INT REFERENCES libros(id),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    detalle JSONB
);

INSERT INTO autores VALUES (1, 'Mario Vargas Llosa', 'Peruana');
INSERT INTO autores VALUES (2, 'Haruki Murakami', 'Japonesa');
INSERT INTO autores VALUES (3, 'Jane Austen', 'Británica');
INSERT INTO autores VALUES (4, 'Stephen King', 'Estadounidense');
INSERT INTO autores VALUES (5, 'Julio Cortázar', 'Argentina');
INSERT INTO autores VALUES (6, 'Gabriel García Márquez', 'Colombiana');
INSERT INTO autores VALUES (7, 'Isabel Allende', 'Chilena');
INSERT INTO autores VALUES (8, 'J.K. Rowling', 'Británica');
INSERT INTO autores VALUES (9, 'Mario Vargas Llosa', 'Peruana');
INSERT INTO autores VALUES (10, 'Haruki Murakami', 'Japonesa');
INSERT INTO autores VALUES (11, 'Jane Austen', 'Británica');
INSERT INTO autores VALUES (12, 'Stephen King', 'Estadounidense');
INSERT INTO autores VALUES (13, 'Julio Cortázar', 'Argentina');
INSERT INTO autores VALUES (14, 'Margaret Atwood', 'Canadiense');
INSERT INTO autores VALUES (15, 'Umberto Eco', 'Italiana');

INSERT INTO libros VALUES (1, 'La ciudad y los perros', 1963, 'Novela', 2);
INSERT INTO libros VALUES (2, 'Tokio Blues', 1987, 'Novela', 3);
INSERT INTO libros VALUES (3, 'Orgullo y prejuicio', 1813, 'Romance', 2);
INSERT INTO libros VALUES (4, 'It', 1986, 'Terror', 1);
INSERT INTO libros VALUES (5, 'Rayuela', 1963, 'Novela', 2);
INSERT INTO libros VALUES (6, 'El resplandor', 1977, 'Terror', 2);
INSERT INTO libros VALUES (7, 'Kafka en la orilla', 2002, 'Fantasía', 1);
INSERT INTO libros VALUES (8, 'El amor en los tiempos del cólera', 1985, 'Novela', 2);
INSERT INTO libros VALUES (9, 'Cien años de soledad', 1967, 'Novela', 3);
INSERT INTO libros VALUES (10, 'El amor en los tiempos del cólera', 1985, 'Novela', 2);
INSERT INTO libros VALUES (11, 'La casa de los espíritus', 1982, 'Novela', 2);
INSERT INTO libros VALUES (12, 'Harry Potter y la piedra filosofal', 1997, 'Fantasía', 4);
INSERT INTO libros VALUES (13, 'Harry Potter y la cámara secreta', 1998, 'Fantasía', 4);
INSERT INTO libros VALUES (14, 'Harry Potter y el prisionero de Azkaban', 1999, 'Fantasía', 4);
INSERT INTO libros VALUES (15, 'La ciudad y los perros', 1963, 'Novela', 2);
INSERT INTO libros VALUES (16, 'Conversación en La Catedral', 1969, 'Novela', 2);
INSERT INTO libros VALUES (17, 'Tokio Blues', 1987, 'Novela', 3);
INSERT INTO libros VALUES (18, 'Kafka en la orilla', 2002, 'Fantasía', 1);
INSERT INTO libros VALUES (19, 'Orgullo y prejuicio', 1813, 'Romance', 2);
INSERT INTO libros VALUES (20, 'Emma', 1815, 'Romance', 2);
INSERT INTO libros VALUES (21, 'It', 1986, 'Terror', 1);
INSERT INTO libros VALUES (22, 'El resplandor', 1977, 'Terror', 2);
INSERT INTO libros VALUES (23, 'Rayuela', 1963, 'Novela', 2);
INSERT INTO libros VALUES (24, 'Bestiario', 1951, 'Cuento', 1);
INSERT INTO libros VALUES (25, 'El cuento de la criada', 1985, 'Distopía', 2);
INSERT INTO libros VALUES (26, 'Alias Grace', 1996, 'Histórica', 1);
INSERT INTO libros VALUES (27, 'El nombre de la rosa', 1980, 'Misterio', 2);
INSERT INTO libros VALUES (28, 'Baudolino', 2000, 'Histórica', 1);
INSERT INTO libros VALUES (29, 'El otoño del patriarca', 1975, 'Novela', 2);
INSERT INTO libros VALUES (30, 'De amor y de sombra', 1984, 'Novela', 1);
INSERT INTO libros VALUES (31, 'Harry Potter y el cáliz de fuego', 2000, 'Fantasía', 4);
INSERT INTO libros VALUES (32, 'Harry Potter y la Orden del Fénix', 2003, 'Fantasía', 4);
INSERT INTO libros VALUES (33, 'Harry Potter y el misterio del príncipe', 2005, 'Fantasía', 4);
INSERT INTO libros VALUES (34, 'Harry Potter y las reliquias de la muerte', 2007, 'Fantasía', 4);
INSERT INTO libros VALUES (35, 'Los perros del paraíso', 1983, 'Novela', 1);
INSERT INTO libros VALUES (36, 'El fin del mundo y un despiadado país de las maravillas', 1985, 'Fantasía', 1);
INSERT INTO libros VALUES (37, '1Q84', 2009, 'Fantasía', 2);
INSERT INTO libros VALUES (38, 'Crónica de una muerte anunciada', 1981, 'Novela', 2);
INSERT INTO libros VALUES (39, 'La increíble y triste historia de la cándida Eréndira', 1972, 'Novela', 1);
INSERT INTO libros VALUES (40, 'La suma de los días', 2007, 'Memorias', 1);
INSERT INTO libros VALUES (41, 'El palacio de la luna', 1989, 'Novela', 1);
INSERT INTO libros VALUES (42, 'Carrie', 1974, 'Terror', 1);
INSERT INTO libros VALUES (43, 'Misery', 1987, 'Terror', 1);
INSERT INTO libros VALUES (44, 'Cuentos de Eva Luna', 1989, 'Cuento', 1);
INSERT INTO libros VALUES (45, 'Ensayo sobre la ceguera', 1995, 'Novela', 2);
INSERT INTO libros VALUES (46, 'El Aleph', 1949, 'Cuento', 1);
INSERT INTO libros VALUES (47, 'La tía Julia y el escribidor', 1977, 'Novela', 1);
INSERT INTO libros VALUES (48, 'Travesuras de la niña mala', 2006, 'Novela', 1);
INSERT INTO libros VALUES (49, 'El túnel', 1948, 'Novela', 1);
INSERT INTO libros VALUES (50, 'La balada del café triste', 1951, 'Cuento', 1);
INSERT INTO libros VALUES (51, 'El psicoanalista', 2002, 'Thriller', 1);
INSERT INTO libros VALUES (52, 'El hombre duplicado', 2002, 'Novela', 1);
INSERT INTO libros VALUES (53, 'El cementerio de Praga', 2010, 'Misterio', 1);
INSERT INTO libros VALUES (54, 'La isla del día de antes', 1994, 'Aventura', 1);
INSERT INTO libros VALUES (55, 'El libro de arena', 1975, 'Cuento', 1);
INSERT INTO libros VALUES (56, 'El perseguidor', 1959, 'Cuento', 1);
INSERT INTO libros VALUES (57, 'La sombra del viento', 2001, 'Misterio', 2);

INSERT INTO usuarios VALUES (2, 'Ana Torres', 'ana@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (3, 'Luis Gómez', 'luis@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (4, 'María Pérez', 'maria@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (5, 'Carlos Ruiz', 'carlos@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (6, 'Elena Martínez', 'elena@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (7, 'Jorge Fernández', 'jorge@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (8, 'Lucía Sánchez', 'lucia@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (9, 'Pedro Ramírez', 'pedro@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (10, 'Sofía López', 'sofia@correo.com', '2025-05-22');
INSERT INTO usuarios VALUES (11, 'Miguel Castro', 'miguel@correo.com', '2025-05-22');

INSERT INTO comentarios VALUES (1, 2, 1, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["favorito", "realismo mágico"], "comentario": "Obra maestra"}');
INSERT INTO comentarios VALUES (2, 2, 2, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["amor", "latinoamericano"], "comentario": "Muy romántico"}');
INSERT INTO comentarios VALUES (3, 3, 3, '2025-05-22 12:42:09.382436', '{"puntaje": 3, "etiquetas": ["clásico"], "comentario": "Interesante pero denso"}');
INSERT INTO comentarios VALUES (4, 4, 4, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["fantasía"], "comentario": "Fascinante"}');
INSERT INTO comentarios VALUES (5, 5, 5, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["fantasía"], "comentario": "Entretenido"}');
INSERT INTO comentarios VALUES (6, 6, 6, '2025-05-22 12:42:09.382436', '{"puntaje": 2, "etiquetas": ["fantasía"], "comentario": "Esperaba más"}');
INSERT INTO comentarios VALUES (7, 7, 7, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["novela"], "comentario": "Excelente"}');
INSERT INTO comentarios VALUES (8, 8, 8, '2025-05-22 12:42:09.382436', '{"puntaje": 3, "etiquetas": ["novela"], "comentario": "Complicado de seguir"}');
INSERT INTO comentarios VALUES (9, 9, 9, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["japonés"], "comentario": "Murakami nunca decepciona"}');
INSERT INTO comentarios VALUES (10, 10, 10, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["fantasía"], "comentario": "Increíble"}');
INSERT INTO comentarios VALUES (11, 3, 11, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["romance"], "comentario": "Un clásico imperdible"}');
INSERT INTO comentarios VALUES (12, 2, 12, '2025-05-22 12:42:09.382436', '{"puntaje": 3, "etiquetas": ["romance"], "comentario": "No es mi estilo"}');
INSERT INTO comentarios VALUES (13, 3, 13, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["terror"], "comentario": "Terrorífico y atrapante"}');
INSERT INTO comentarios VALUES (14, 4, 14, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["terror"], "comentario": "Muy bueno"}');
INSERT INTO comentarios VALUES (15, 5, 15, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["experimental"], "comentario": "Cortázar es único"}');
INSERT INTO comentarios VALUES (16, 6, 16, '2025-05-22 12:42:09.382436', '{"puntaje": 3, "etiquetas": ["cuento"], "comentario": "Interesante"}');
INSERT INTO comentarios VALUES (17, 7, 17, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["distopía"], "comentario": "Distopía atrapante"}');
INSERT INTO comentarios VALUES (18, 8, 18, '2025-05-22 12:42:09.382436', '{"puntaje": 5, "etiquetas": ["histórica"], "comentario": "Muy recomendable"}');
INSERT INTO comentarios VALUES (19, 9, 19, '2025-05-22 12:42:09.382436', '{"puntaje": 4, "etiquetas": ["misterio"], "comentario": "Misterio bien logrado"}');
INSERT INTO comentarios VALUES (20, 10, 20, '2025-05-22 12:42:09.382436', '{"puntaje": 3, "etiquetas": ["histórica"], "comentario": "Un poco largo"}');
INSERT INTO comentarios VALUES (22, 5, 4, '2025-03-03 00:00:00', '{"puntaje": 5, "etiquetas": ["favorito", "realismo mágico"], "comentario": "Obra maestra"}');
INSERT INTO comentarios VALUES (21, 4, 4, '2025-01-20 00:00:00', '{"puntaje": 4, "etiquetas": ["favorito", "realismo mágico"], "comentario": "Obra maestra"}');

INSERT INTO libro_autor VALUES (1, 1);
INSERT INTO libro_autor VALUES (2, 1);
INSERT INTO libro_autor VALUES (21, 1);
INSERT INTO libro_autor VALUES (29, 1);
INSERT INTO libro_autor VALUES (30, 1);
INSERT INTO libro_autor VALUES (3, 2);
INSERT INTO libro_autor VALUES (22, 2);
INSERT INTO libro_autor VALUES (31, 2);
INSERT INTO libro_autor VALUES (35, 2);
INSERT INTO libro_autor VALUES (4, 3);
INSERT INTO libro_autor VALUES (5, 3);
INSERT INTO libro_autor VALUES (6, 3);
INSERT INTO libro_autor VALUES (23, 3);
INSERT INTO libro_autor VALUES (24, 3);
INSERT INTO libro_autor VALUES (25, 3);
INSERT INTO libro_autor VALUES (26, 3);
INSERT INTO libro_autor VALUES (7, 4);
INSERT INTO libro_autor VALUES (8, 4);
INSERT INTO libro_autor VALUES (38, 4);
INSERT INTO libro_autor VALUES (39, 4);
INSERT INTO libro_autor VALUES (9, 5);
INSERT INTO libro_autor VALUES (10, 5);
INSERT INTO libro_autor VALUES (28, 5);
INSERT INTO libro_autor VALUES (11, 6);
INSERT INTO libro_autor VALUES (12, 6);
INSERT INTO libro_autor VALUES (13, 7);
INSERT INTO libro_autor VALUES (14, 7);
INSERT INTO libro_autor VALUES (33, 7);
INSERT INTO libro_autor VALUES (34, 7);
INSERT INTO libro_autor VALUES (15, 8);
INSERT INTO libro_autor VALUES (16, 8);
INSERT INTO libro_autor VALUES (49, 8);
INSERT INTO libro_autor VALUES (17, 9);
INSERT INTO libro_autor VALUES (18, 9);
INSERT INTO libro_autor VALUES (36, 9);
INSERT INTO libro_autor VALUES (19, 10);
INSERT INTO libro_autor VALUES (20, 10);
INSERT INTO libro_autor VALUES (45, 10);
INSERT INTO libro_autor VALUES (46, 10);
INSERT INTO libro_autor VALUES (27, 5);
INSERT INTO libro_autor VALUES (32, 4);
INSERT INTO libro_autor VALUES (37, 8);
INSERT INTO libro_autor VALUES (40, 4);
INSERT INTO libro_autor VALUES (41, 8);
INSERT INTO libro_autor VALUES (42, 9);
INSERT INTO libro_autor VALUES (43, 9);
INSERT INTO libro_autor VALUES (44, 10);
INSERT INTO libro_autor VALUES (47, 10);
INSERT INTO libro_autor VALUES (48, 8);
INSERT INTO libro_autor VALUES (50, 10);

INSERT INTO prestamos VALUES (31, 2, 1, '2024-01-10', '2024-01-30');
INSERT INTO prestamos VALUES (32, 2, 2, '2024-01-15', NULL);
INSERT INTO prestamos VALUES (33, 3, 3, '2024-01-20', '2024-02-10');
INSERT INTO prestamos VALUES (34, 4, 4, '2024-02-01', NULL);
INSERT INTO prestamos VALUES (35, 5, 5, '2024-02-05', '2024-02-25');
INSERT INTO prestamos VALUES (36, 6, 6, '2024-02-10', NULL);
INSERT INTO prestamos VALUES (37, 7, 7, '2024-02-15', '2024-03-05');
INSERT INTO prestamos VALUES (38, 8, 8, '2024-02-20', NULL);
INSERT INTO prestamos VALUES (39, 9, 9, '2024-02-25', '2024-03-15');
INSERT INTO prestamos VALUES (40, 10, 10, '2024-03-01', NULL);
INSERT INTO prestamos VALUES (41, 3, 11, '2024-03-05', '2024-03-25');
INSERT INTO prestamos VALUES (42, 2, 12, '2024-03-10', NULL);
INSERT INTO prestamos VALUES (43, 3, 13, '2024-03-15', '2024-04-05');
INSERT INTO prestamos VALUES (44, 4, 14, '2024-03-20', NULL);
INSERT INTO prestamos VALUES (45, 5, 15, '2024-03-25', '2024-04-15');
INSERT INTO prestamos VALUES (46, 6, 16, '2024-04-01', NULL);
INSERT INTO prestamos VALUES (47, 7, 17, '2024-04-05', '2024-04-25');
INSERT INTO prestamos VALUES (48, 8, 18, '2024-04-10', NULL);
INSERT INTO prestamos VALUES (49, 9, 19, '2024-04-15', '2024-05-05');
INSERT INTO prestamos VALUES (50, 10, 20, '2024-04-20', NULL);
INSERT INTO prestamos VALUES (51, 5, 21, '2024-04-25', '2024-05-15');
INSERT INTO prestamos VALUES (52, 2, 22, '2024-05-01', NULL);
INSERT INTO prestamos VALUES (53, 3, 23, '2024-05-05', '2024-05-25');
INSERT INTO prestamos VALUES (54, 4, 24, '2024-05-10', NULL);
INSERT INTO prestamos VALUES (55, 5, 25, '2024-05-15', '2024-06-05');
INSERT INTO prestamos VALUES (56, 6, 26, '2024-05-20', NULL);
INSERT INTO prestamos VALUES (57, 7, 27, '2024-05-25', '2024-06-15');
INSERT INTO prestamos VALUES (58, 8, 28, '2024-06-01', NULL);
INSERT INTO prestamos VALUES (59, 9, 29, '2024-06-05', '2024-06-25');
INSERT INTO prestamos VALUES (60, 10, 30, '2024-06-10', NULL);
INSERT INTO prestamos VALUES (61, 8, 12, '2025-01-01', NULL);
INSERT INTO prestamos VALUES (64, 7, 15, '2024-12-01', NULL);
INSERT INTO prestamos VALUES (65, 6, 15, '2023-01-01', '2024-10-10');
INSERT INTO prestamos VALUES (66, 2, 12, '2025-03-10', NULL);


-- 1. Libros que nunca han sido prestados:
select *
from libros as l
where l.id not in (
				select p.libro_id  
				from  prestamos as p
				)

-- SOLUCION DE GPT				
SELECT *
FROM libros AS l
WHERE NOT EXISTS (
    SELECT 1
    FROM prestamos AS p
    WHERE p.libro_id = l.id
);

-- 2. Listar usuarios y la cantidad total de libros distintos que se han prestado
select  u.nombre, count (distinct (p.libro_id))
from prestamos p , usuarios u , libros l  
where p.usuario_id = u.id and p.libro_id = l.id
group by u.nombre

-- 3. Libros y total de préstamos históricos, listando solo los mas prestados (todos los libros con el maximo de prestamos)
select l.titulo, count (p.libro_id) as total_pestados
from libros l , prestamos p 
where l.id  = p.libro_id
group by l.titulo
order by total_pestados  desc
limit 1


-- 4. Ranking de usuarios por cantidad de préstamos:
select  u.nombre ,count(p.id) as cantidad
from usuarios u , prestamos p 
where u.id  = p.usuario_id
group by p.usuario_id, u.nombre
order by cantidad  desc

