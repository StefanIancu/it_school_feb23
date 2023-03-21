import logger

def circle_are(radius):
    """Calculate circle area. Radius has to be a positive integer.
    
    Args:
        -radius (float): Circle radius 
    
    Raises:
        -ValueError: if radius is less than zero 
    """
    if radius < 0:
        raise ValueError("Raza trebuie sa fie mai mare decat zero.")


    return 3.14 * radius ** 2

logger.error("Salut")