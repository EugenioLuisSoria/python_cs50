def get_media_type(filename):
  """
  Determina el tipo de medio de un archivo basado en su extensión.

  Args:
      filename: El nombre del archivo.

  Returns:
      El tipo de medio del archivo o "application/octet-stream" si no se conoce.
  """

  # Extensiones válidas y sus tipos de medios correspondientes
  extensions = {
      ".gif": "image/gif",
      ".jpg": "image/jpeg",
      ".jpeg": "image/jpeg",
      ".png": "image/png",
      ".pdf": "application/pdf",
      ".txt": "text/plain",
      ".zip": "application/zip"
  }

  # Convierte el nombre del archivo a minúsculas para evitar problemas de mayúsculas y minúsculas
  filename_lower = filename.lower()

  # Extrae la extensión del archivo
  dot_pos = filename_lower.rfind(".")
  if dot_pos == -1:
    return "application/octet-stream"  # No hay extensión

  extension = filename_lower[dot_pos:]

  # Busca la extensión en el diccionario y devuelve el tipo de medio correspondiente
  if extension in extensions:
    return extensions[extension]
  else:
    return "application/octet-stream"  # Extensión desconocida

# Solicita el nombre del archivo al usuario
filename = input("Ingrese el nombre del archivo: ")

# Determina el tipo de medio
media_type = get_media_type(filename)

# Imprime el resultado
print(f"El tipo de medio del archivo '{filename}' es: {media_type}")
