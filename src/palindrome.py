def is_palindrome(text):
  # Caso especial: texto vacío o un solo carácter es palíndromo
  if len(text) <= 1:
    return True

  # Convertir a minúsculas
  text = text.lower()

  # Eliminar caracteres no alfanuméricos
  clean_text = ""
  for char in text:
    if char.isalnum():  # Solo conserva letras y números
      clean_text += char

  # Verificar si es palíndromo comparando con su reverso
  return clean_text == clean_text[::-1]