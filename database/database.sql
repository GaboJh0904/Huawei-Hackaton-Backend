create schema EfficientConnect_db;

-- tables
-- Table: Asignacion
CREATE TABLE Asignacion (
    id int  NOT NULL AUTO_INCREMENT,
    fecha_asignacion int  NOT NULL,
    Usuario_id int  NOT NULL,
    Tarea_id int  NOT NULL,
    CONSTRAINT Asignacion_pk PRIMARY KEY (id)
);

-- Table: Categoria
CREATE TABLE Categoria (
    id int  NOT NULL AUTO_INCREMENT,
    categoria varchar(100)  NOT NULL,
    CONSTRAINT Categoria_pk PRIMARY KEY (id)
);

-- Table: Chat
CREATE TABLE Chat (
    id int  NOT NULL AUTO_INCREMENT,
    Familia_empresa_id int  NOT NULL,
    Miembros_id int  NOT NULL,
    nombre varchar(100)  NOT NULL,
    fecha_creacion date  NOT NULL,
    CONSTRAINT Chat_pk PRIMARY KEY (id)
);

-- Table: Comentarios
CREATE TABLE Comentarios (
    id int  NOT NULL AUTO_INCREMENT,
    comentario varchar(250)  NOT NULL,
    fecha_creacion date  NOT NULL,
    Usuario_id int  NOT NULL,
    Tarea_id int  NOT NULL,
    CONSTRAINT Comentarios_pk PRIMARY KEY (id)
);

-- Table: Familia_empresa
CREATE TABLE Familia_empresa (
    id int  NOT NULL AUTO_INCREMENT,
    nombre varchar(100)  NOT NULL,
    detalle varchar(250)  NOT NULL,
    fecha_creacion date  NOT NULL,
    CONSTRAINT Familia_empresa_pk PRIMARY KEY (id)
);

-- Table: Mensaje
CREATE TABLE Mensaje (
    id int  NOT NULL AUTO_INCREMENT,
    mensaje text  NOT NULL,
    Chat_id int  NOT NULL,
    fecha datetime  NOT NULL,
    CONSTRAINT Mensaje_pk PRIMARY KEY (id)
);

-- Table: Miembros
CREATE TABLE Miembros (
    id int  NOT NULL AUTO_INCREMENT,
    Usuario_id int  NOT NULL,
    Familia_empresa_id int  NOT NULL,
    rol ENUM('admin', 'miembro')  NOT NULL,
    CONSTRAINT Miembros_pk PRIMARY KEY (id)
);

-- Table: Persona
CREATE TABLE Persona (
    id int  NOT NULL AUTO_INCREMENT,
    nombre varchar(200)  NOT NULL,
    email varchar(100)  NOT NULL,
    telefono varchar(20)  NOT NULL,
    fecha_nacimiento date  NOT NULL,
    CONSTRAINT Persona_pk PRIMARY KEY (id)
);

-- Table: Tablero
CREATE TABLE Tablero (
    id int  NOT NULL AUTO_INCREMENT,
    nombre varchar(100)  NOT NULL,
    descripcion varchar(250)  NOT NULL,
    fecha_creacion date  NOT NULL,
    Familia_empresa_id int  NOT NULL,
    CONSTRAINT Tablero_pk PRIMARY KEY (id)
);

-- Table: Tarea
CREATE TABLE Tarea (
    id int  NOT NULL AUTO_INCREMENT,
    nombre varchar(100)  NOT NULL,
    descripcion varchar(250)  NOT NULL,
    estado ENUM('pendiente', 'en_progreso', 'completada')  NOT NULL,
    prioridad ENUM('alta', 'media', 'baja')  NOT NULL,
    fecha_creacion date  NOT NULL,
    fecha_fin date  NOT NULL,
    Tablero_id int  NOT NULL,
    Categoria_id int  NOT NULL,
    CONSTRAINT Tarea_pk PRIMARY KEY (id)
);

-- Table: Usuario
CREATE TABLE Usuario (
    id int  NOT NULL AUTO_INCREMENT,
    username varchar(75)  NOT NULL,
    password varchar(55)  NOT NULL,
    Persona_id int  NOT NULL,
    CONSTRAINT Usuario_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: Asignacion_Tarea (table: Asignacion)
ALTER TABLE Asignacion ADD CONSTRAINT Asignacion_Tarea FOREIGN KEY Asignacion_Tarea (Tarea_id)
    REFERENCES Tarea (id);

-- Reference: Asignacion_Usuario (table: Asignacion)
ALTER TABLE Asignacion ADD CONSTRAINT Asignacion_Usuario FOREIGN KEY Asignacion_Usuario (Usuario_id)
    REFERENCES Usuario (id);

-- Reference: Chat_Familia_empresa (table: Chat)
ALTER TABLE Chat ADD CONSTRAINT Chat_Familia_empresa FOREIGN KEY Chat_Familia_empresa (Familia_empresa_id)
    REFERENCES Familia_empresa (id);

-- Reference: Chat_Miembros (table: Chat)
ALTER TABLE Chat ADD CONSTRAINT Chat_Miembros FOREIGN KEY Chat_Miembros (Miembros_id)
    REFERENCES Miembros (id);

-- Reference: Comentarios_Tarea (table: Comentarios)
ALTER TABLE Comentarios ADD CONSTRAINT Comentarios_Tarea FOREIGN KEY Comentarios_Tarea (Tarea_id)
    REFERENCES Tarea (id);

-- Reference: Comentarios_Usuario (table: Comentarios)
ALTER TABLE Comentarios ADD CONSTRAINT Comentarios_Usuario FOREIGN KEY Comentarios_Usuario (Usuario_id)
    REFERENCES Usuario (id);

-- Reference: Mensaje_Chat (table: Mensaje)
ALTER TABLE Mensaje ADD CONSTRAINT Mensaje_Chat FOREIGN KEY Mensaje_Chat (Chat_id)
    REFERENCES Chat (id);

-- Reference: Miembros_Familia_empresa (table: Miembros)
ALTER TABLE Miembros ADD CONSTRAINT Miembros_Familia_empresa FOREIGN KEY Miembros_Familia_empresa (Familia_empresa_id)
    REFERENCES Familia_empresa (id);

-- Reference: Miembros_Usuario (table: Miembros)
ALTER TABLE Miembros ADD CONSTRAINT Miembros_Usuario FOREIGN KEY Miembros_Usuario (Usuario_id)
    REFERENCES Usuario (id);

-- Reference: Tablero_Familia_empresa (table: Tablero)
ALTER TABLE Tablero ADD CONSTRAINT Tablero_Familia_empresa FOREIGN KEY Tablero_Familia_empresa (Familia_empresa_id)
    REFERENCES Familia_empresa (id);

-- Reference: Tarea_Categoria (table: Tarea)
ALTER TABLE Tarea ADD CONSTRAINT Tarea_Categoria FOREIGN KEY Tarea_Categoria (Categoria_id)
    REFERENCES Categoria (id);

-- Reference: Tarea_Tablero (table: Tarea)
ALTER TABLE Tarea ADD CONSTRAINT Tarea_Tablero FOREIGN KEY Tarea_Tablero (Tablero_id)
    REFERENCES Tablero (id);

-- Reference: Usuario_Persona (table: Usuario)
ALTER TABLE Usuario ADD CONSTRAINT Usuario_Persona FOREIGN KEY Usuario_Persona (Persona_id)
    REFERENCES Persona (id);

-- End of file.

