from datetime import datetime

# Lista de los nombres de meses en español
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def formatear_fecha(fecha):
    # Intentamos analizar la fecha ingresada en ambos formatos
    try:
        # Intentamos analizar la fecha en formato mes/día/año
        fecha_dt = datetime.strptime(fecha, "%m/%d/%Y")
    except ValueError:
        try:
            # Intentamos analizar la fecha en formato mes día, año
            fecha_dt = datetime.strptime(fecha, "%B %d, %Y")
        except ValueError:
            # Si no podemos analizar la fecha en ninguno de los formatos, mostramos un mensaje de error
            return "Formato de fecha no válido. Intente nuevamente."
    
    # Formateamos la fecha en el formato AAAA-MM-DD
    fecha_formateada = fecha_dt.strftime("%Y-%m-%d")
    
    return fecha_formateada

# Función principal para solicitar y procesar la entrada del usuario
def main():
    # Solicitamos que ingrese por teclado la feche el usuario
    fecha_usuario = input("Ingrese la fecha (en el formato mes/día/año o Mes día, año): ")
    
    # Formateamos la fecha ingresada
    fecha_formateada = formatear_fecha(fecha_usuario)
    
    # Mostramos el resultado en pantalla
    print("Fecha en formato AAAA-MM-DD:", fecha_formateada)

# Ejecutamos la función principal
if __name__ == "__main__":
    main()