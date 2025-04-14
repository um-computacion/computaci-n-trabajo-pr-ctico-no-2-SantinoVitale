def is_palindrome(text):
    # Caso especial: texto vacío o un solo carácter es palíndromo
    if len(text) <= 1:
        return True
    
    # Convertir a minúsculas
    text = text.lower()
    
    # Verificar si es palíndromo comparando con su reverso
    return text == text[::-1]