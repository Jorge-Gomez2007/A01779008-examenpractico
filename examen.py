"""
Sistema de Trueque 
------------------------------------------------------------
Objetivo: mostrar el diseño general del sistema, con funciones, validaciones y
la idea de "base de datos" en archivos; sin necesidad de que todo corra ahora.

En esta maqueta:
- Implementado por completo : registrar_usuario
- Implementadas validaciones básicas: texto no vacío, email simple, password mínimo
- TODO (diseño + comentarios): autenticación, productos, ofertas, chat, persistencia CSV

"""

# =========================
# 1) VALIDACIÓN Y UTILIDADES
# =========================



def validar_texto_no_vacio(texto: str, nombre_campo: str = "valor") -> tuple[bool, str | None]:
    
    #Verifica que un texto no esté vacío o con solo espacios.
    #Retorna (True, None) si es válido; si no, (False, "mensaje de error").
    
    if texto is None or str(texto).strip() == "":
        return False, f"El campo '{nombre_campo}' no puede estar vacío."
    return True, None



def validar_password(password: str, min_len: int = 6) -> tuple[bool, str | None]:
    
    #Verifica longitud mínima. Para principiantes, basta con esto.
    
    ok, err = validar_texto_no_vacio(password, "password")
    if not ok:
        return ok, err
    if len(password) < min_len:
        return False, f"El password debe tener al menos {min_len} caracteres."
    return True, None


# =========================
# 2) "BASE DE DATOS" (mock) Y ARCHIVOS
# =========================

# --- Simulación en memoria (para esta prueba) ---
# En un futuro, estos datos se cargarían/guardarían desde/ hacia archivos CSV.
USUARIOS_DB = []       # lista de dicts: {"user_id", "nombre", "email", "password_hash"}
PRODUCTOS_DB = []      # lista de dicts: {"producto_id", "user_id_propietario", "titulo", ...}
OFERTAS_DB = []        # lista de dicts: {"oferta_id", "producto_id", "user_id_ofertante", ...}
CHATS_DB = []          # lista de dicts: {"mensaje_id", "user_id_origen", "user_id_destino", ...}

# --- Generadores de ID ---
_next_user_id = 1
_next_producto_id = 1
_next_oferta_id = 1
_next_mensaje_id = 1

def generar_id_usuario() -> str:
    """Genera un ID de usuario incremental tipo 'USR_1', 'USR_2', ..."""
    global _next_user_id
    uid = f"USR_{_next_user_id}"
    _next_user_id += 1
    return uid

def generar_id_producto() -> str:
    """Genera un ID de producto incremental tipo 'PRD_1', 'PRD_2', ..."""
    global _next_producto_id
    pid = f"PRD_{_next_producto_id}"
    _next_producto_id += 1
    return pid

def generar_id_oferta() -> str:
    """Genera un ID de oferta incremental tipo 'OFR_1', 'OFR_2', ..."""
    global _next_oferta_id
    oid = f"OFR_{_next_oferta_id}"
    _next_oferta_id += 1
    return oid

def generar_id_mensaje() -> str:
    """Genera un ID de mensaje incremental tipo 'MSG_1', 'MSG_2', ..."""
    global _next_mensaje_id
    mid = f"MSG_{_next_mensaje_id}"
    _next_mensaje_id += 1
    return mid


# --- Firmas para manejo de archivos (CSV) (diseño) ---
def guardar_usuarios_en_csv(ruta_csv: str) -> None:
    """
    TODO (diseño): Guardar USUARIOS_DB en un archivo CSV con encabezados.
    - Abrir archivo en modo escritura.
    - Escribir cabeceras: user_id,nombre,email,password_hash
    - Recorrer USUARIOS_DB con un for y escribir cada fila.
    """
    pass

def cargar_usuarios_de_csv(ruta_csv: str) -> None:
    
    #TODO (diseño): Cargar usuarios desde CSV a USUARIOS_DB.
    #- Abrir archivo en modo lectura.
    #- Leer y construir diccionarios y agregarlos a USUARIOS_DB.
    pass

def guardar_productos_en_csv(ruta_csv: str) -> None:
    """TODO (diseño): Guardar PRODUCTOS_DB al CSV."""
    pass

def cargar_productos_de_csv(ruta_csv: str) -> None:
    """TODO (diseño): Cargar PRODUCTOS_DB desde CSV."""
    pass

def guardar_ofertas_en_csv(ruta_csv: str) -> None:
    """TODO (diseño): Guardar OFERTAS_DB al CSV."""
    pass

def cargar_ofertas_de_csv(ruta_csv: str) -> None:
    """TODO (diseño): Cargar OFERTAS_DB desde CSV."""
    pass

def guardar_chats_en_csv(ruta_csv: str) -> None:
    """TODO (diseño): Guardar CHATS_DB al CSV."""
    pass

def cargar_chats_de_csv(ruta_csv: str) -> None:
    """TODO (diseño): Cargar CHATS_DB desde CSV."""
    pass


# =========================
# 3) MÓDULO: USUARIOS
# =========================

def registrar_usuario(nombre: str, email: str, password: str) -> tuple[bool, str | None, dict | None]:
    """
    IMPLEMENTADA (sencilla, en memoria).

    Flujo:
    1) Validar nombre, email y password.
    2) Unicidad por email (recorrer la lista USUARIOS_DB con un for).
    3) Crear un dict y "guardarlo" en USUARIOS_DB.
    4) Retornar (True, None, usuario_dict) si todo va bien.

    Nota: password_hash aquí será el propio password (por simplicidad de principiantes).
    En una versión real, se debe hashear.
    """
    # Validaciones básicas
    ok, err = validar_texto_no_vacio(nombre, "nombre")
    if not ok:
        return False, err, None
   
    ok, err = validar_password(password)
    if not ok:
        return False, err, None

   

    # Crear registro y guardar en memoria
    usuario = {
        "user_id": generar_id_usuario(),
        "nombre": nombre.strip(),
        "email": email.strip().lower(),
        "password_hash": password,  # ← En real: usar hash. Aquí lo dejamos simple para la prueba.
    }
    USUARIOS_DB.append(usuario)
    return True, None, usuario


def autenticar_usuario(email: str, password: str) -> tuple[bool, str | None, dict | None]:
    """
    TODO (diseño): Autenticar buscando por email y comparando password_hash.
    - Recorrer USUARIOS_DB (for).
    - Si email coincide y password también → éxito.
    - Si no, retornar error.
    """
    return False, "No implementado aún.", None


def obtener_usuario_por_id(user_id: str) -> dict | None:
    """
    TODO (diseño): Buscar en USUARIOS_DB por user_id y retornar el dict o None.
    - Recorrer con for y comparar.
    """
    return None


# =========================
# 3) MÓDULO: PRODUCTOS
# =========================

def agregar_producto(user_id_propietario: str, titulo: str, descripcion: str,
                     categoria: str, estado: str) -> tuple[bool, str | None, dict | None]:
    """
    TODO (diseño): Crear un producto asociado a un usuario existente.
    - Validar que los textos no estén vacíos.
    - Verificar que user_id_propietario exista (buscar en USUARIOS_DB).
    - Crear un dict con 'disponible' = True.
    - Agregar a PRODUCTOS_DB.
    """
    return False, "No implementado aún.", None


def listar_productos_disponibles() -> list[dict]:
    """
    TODO (diseño): Retornar productos cuyo campo 'disponible' sea True.
    - Recorrer PRODUCTOS_DB y filtrar.
    """
    return []


def marcar_producto_no_disponible(producto_id: str) -> tuple[bool, str | None]:
    """
    TODO (diseño): Buscar producto por ID y marcar disponible=False.
    - Recorrer PRODUCTOS_DB con for, si coincide el ID, actualizar y retornar True.
    """
    return False, "No implementado aún."


def buscar_producto_por_id(producto_id: str) -> dict | None:
    """
    TODO (diseño): Retornar el producto con ese ID, o None si no existe.
    """
    return None


# =========================
# 3) MÓDULO: OFERTAS
# =========================

def crear_oferta(producto_id: str, user_id_ofertante: str, descripcion_oferta: str) -> tuple[bool, str | None, dict | None]:
    """
    TODO (diseño):
    - Validar texto no vacío en descripcion_oferta.
    - Verificar que el producto exista y esté disponible.
    - Verificar que el ofertante exista.
    - Crear oferta con estado 'pendiente' y agregar a OFERTAS_DB.
    """
    return False, "No implementado aún.", None


def listar_ofertas_por_producto(producto_id: str) -> list[dict]:
    """
    TODO (diseño): Filtrar OFERTAS_DB por producto_id y retornar la lista.
    """
    return []


def aceptar_oferta(oferta_id: str) -> tuple[bool, str | None]:
    """
    TODO (diseño):
    - Cambiar estado de la oferta a 'aceptada'.
    - Poner el producto en 'no disponible'.
    - (Opcional) registrar “intercambio” en otro módulo/archivo.
    """
    return False, "No implementado aún."


def rechazar_oferta(oferta_id: str) -> tuple[bool, str | None]:
    """
    TODO (diseño): Cambiar estado de la oferta a 'rechazada'.
    """
    return False, "No implementado aún."


# =========================
# 3) MÓDULO: CHAT ENTRE USUARIOS
# =========================

def enviar_mensaje(user_id_origen: str, user_id_destino: str, contenido: str) -> tuple[bool, str | None, dict | None]:
    
    #TODO (diseño):
    #- Validar que ambos usuarios existan y que el contenido no esté vacío.
    #- Crear dict de mensaje y agregarlo a CHATS_DB (con un ID simple).
    
    return False, "No implementado aún.", None


def listar_chat_entre(user_id_a: str, user_id_b: str) -> list[dict]:
    
    #TODO (diseño):
    #- Retornar mensajes entre A y B (en ambos sentidos).
    #- (Opcional) ordenar por un campo 'timestamp' si se añade.
    
    return []


# =========================
# 4) EJEMPLO DE USO (comentado)
# =========================


# Bucle while de ejemplo (no funcional, solo para mostrar la estructura):
contador = 0
while contador < 3:
    # Aquí podrías pedir datos por input() en una versión interactiva.
    contador += 1

