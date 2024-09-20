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