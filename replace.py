#Se copian funciones de ejercicio previo a modo de complementar esta evaluación.
def guardar_info(archivo, formato):
        """Crea un nuevo archivo con el nombre y formato especificados, escribiendo líneas de información. 
        Si el archivo ya existe, se captura una excepción FileExistsError y se informa al usuario.
        
        Args:
        archivo: nombre del archivo a crear\n
        formato: formato del archivo a crear
        """
        try:
            ruta = "./archivos/"
            nom_archivo = f"{archivo}.{formato}"
            path = ruta + nom_archivo
            
            archivo_nuevo =  open(path, "x")
            
            i=1
            while i<=5:
                archivo_nuevo.write(f"Datos de información en la línea {i}\n")
                i+=1
            archivo_nuevo.close()
        except FileExistsError:
            print(f"No es posible crear el archivo {archivo}.{formato} porque ya existe uno previo con este nombre.\nPorfavor intenta con otro nombre")

        except Exception as e:
            print("Error: ", e)


def agregar_info(archivo, formato):
        """Agrega nueva informacion a un archivo existente con el nombre y formato especificados. 
        Si el archivo con dicho nombre no existe, entonces lo crea.
        
        Args:
        archivo: nombre del archivo a crear\n
        formato: formato del archivo a crear
        """
        
        nuevas_lineas = ["Hola Mundo", 
                         "Este en una nueva línea en el archivo",
                         "agregando la segunda línea del archivo",
                         "finalizando la línea agregada"]
        
        try:
            ruta = "./archivos/"
            nom_archivo = f"{archivo}.{formato}"
            path = ruta + nom_archivo
            
            archivo_nuevo =  open(path, "a")
            for lineas in nuevas_lineas:
                archivo_nuevo.writelines(f"{lineas}\n")
            
            archivo_nuevo.close()
            
        except FileExistsError:
            print(f"No es posible crear el archivo {archivo}.{formato} porque ya existe uno previo con este nombre.\nPorfavor intenta con otro nombre")
    
        except Exception as e:
            print("Error: ", e)    
    
    
#Se agrega función para cumplir con lo solicitado en la presente evaluación.    
def remplazo_palabra(archivo, formato, palabra_antigua, palabra_nueva):
    """Agrega nueva informacion a un archivo existente con el nombre y formato especificados. 
        Si el archivo con dicho nombre no existe, entonces lo crea.
        
        Args:
        archivo: nombre del archivo a crear\n
        formato: formato del archivo a crear
        """
    try:
        ruta = "./archivos/"
        nom_archivo = f"{archivo}.{formato}"
        path = ruta + nom_archivo
    
            
        archivo_nuevo =  open(path, "r")
        contenido = archivo_nuevo.read()
        contenido_con_remplazo = contenido.replace(palabra_antigua, palabra_nueva)
        
        cuenta_cambio = contenido.count(palabra_antigua)   
        print(f"Se realizaron {cuenta_cambio} remplazos")
        
        archivo_nuevo.close()
        
        archivo_nuevo = open (path, "w")
        archivo_nuevo.writelines(contenido_con_remplazo)
        
            
    except FileExistsError:
        print(f"No es posible crear el archivo {archivo}.{formato} porque ya existe uno previo con este nombre.\nPorfavor intenta con otro nombre")
    
    except Exception as e:
        print("Error: ", e) 




    
def main():
    """Función principal del programa que entrega los parametros necesarios para la posterior ejecución de las funciones guadar_info() y agregar info() y remplazo_palabra().
    """
    nombre_archivo = "informacion"
    formato = "dat"    
    palabra_antigua = "información"
    palabra_nueva = "procesamiento"
        
    
    guardar_info(nombre_archivo, formato)   
    agregar_info(nombre_archivo, formato)
    remplazo_palabra(nombre_archivo, formato, palabra_antigua, palabra_nueva)
    
#Ejecución de la funcion para correr el programa
main()

