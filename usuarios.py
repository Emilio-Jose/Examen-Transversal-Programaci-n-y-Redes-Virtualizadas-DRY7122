import sqlite3
import hashlib
from flask import Flask

# Crear aplicación web
app = Flask(__name__)

# Crear base de datos
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nombre TEXT,
    clave_hash TEXT
)
""")

# Usuarios del grupo
usuario1 = "Emilio"
clave1 = "1234"

usuario2 = "Patricio"
clave2 = "abcd"

usuario3 = "Alejandro"
clave3 = "pass"

# Crear hash de contraseñas
hash1 = hashlib.sha256(clave1.encode()).hexdigest()
hash2 = hashlib.sha256(clave2.encode()).hexdigest()
hash3 = hashlib.sha256(clave3.encode()).hexdigest()

# Insertar datos
cursor.execute("INSERT INTO usuarios VALUES (?,?)", (usuario1, hash1))
cursor.execute("INSERT INTO usuarios VALUES (?,?)", (usuario2, hash2))
cursor.execute("INSERT INTO usuarios VALUES (?,?)", (usuario3, hash3))

conexion.commit()
conexion.close()

# Página web
@app.route("/")
def inicio():
    return "Servidor web activo - Item 3 DRY7122"

# Ejecutar servidor en puerto 5800
app.run(host="0.0.0.0", port=5800)
