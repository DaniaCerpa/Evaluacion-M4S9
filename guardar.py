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


