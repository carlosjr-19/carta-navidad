from .cards import CARTAS_FAMILIARES as cartas

CARTAS_FAMILIARES = cartas

def buscar_carta(nombre: str, fecha: str) -> dict:
    """
    Busca una carta basada en nombre y fecha
    """
    # Crear clave de búsqueda
    clave = f"{nombre.lower().strip()}_{fecha.strip()}"
    
    # Buscar en el diccionario
    if clave in CARTAS_FAMILIARES:
        return {
            "encontrada": True,
            "data": CARTAS_FAMILIARES[clave]
        }
    
    return {
        "encontrada": False,
        "data": None
    }

def obtener_carta_por_id(carta_id: str) -> dict:
    """
    Obtiene una carta por su ID
    """
    for carta in CARTAS_FAMILIARES.values():
        if carta["carta_id"] == carta_id:
            return carta
    
    return None