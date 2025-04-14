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

def main():
  try:
    while True:
      text = input("Ingrese una palabra o frase: ")
      if is_palindrome(text):
        print(f'"{text}" es un palíndromo')
      else:
        print(f'"{text}" no es un palíndromo')
        print()
  except KeyboardInterrupt:
    print("\nPrograma finalizado.")
    exit(0)

if __name__ == "__main__":
  main()

