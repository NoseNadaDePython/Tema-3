import os

def crear_Archivo(archivo):
    direccion = r'C:/Users\isc20/OneDrive/Escritorio/codigos/'
    direccion_complet= direccion + archivo
    file = open(direccion_complet,'w+')
    print('Archivo'+ archivo+ 'Ha sido creado correctamente ')
    return file
def modifica_archivo (archivo,agrega):
  direccion= r'C:/Users\isc20/OneDrive/Escritorio/codigos/'
  direccion_complet= direccion + archivo
  file = open(direccion_complet,"a+")
  file.write(agrega+os.linesep)
  print('Archivo'+ archivo+ 'Modificado ')
  cerrar_archivo(file)
  
def cerrar_archivo (file):
      file.close()
      print('Archivo cerrado')
    
    
archivo = input ("Teclee el nombre del archivo: [con extension .txt]")
puntero=crear_Archivo (archivo)
agrega= input ('Texto a agregar')
modifica_archivo(archivo, agrega)

