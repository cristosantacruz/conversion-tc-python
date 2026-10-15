# Paso 1: Definir el valor actual del Euro y Dolar con respecto al peso mexicano

tipo_cambio_eur_a_mxn1 = 23.70 # si fuera real lo definiriamos con una base de datos actualizada. en lo real no puede ser hard coded.
tipo_cambio_usd_a_mxn = 20.75 # si fuera real lo definiriamos con una base de datos actualizada. en lo real no puede ser hard coded.

# Paso 2: Solicitar al usuario el tipo de conversión. Euro/Dolar a Mnx

tipo_conversion = input("ingrese la moneda origen para la conversión (EUR/USD): ")

# Paso 3: Solicitar el usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el TC correspondiente
# Paso 5: Mostrarle al usuario la conversión del TC correcto

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de conversión de EUR a MXN es:", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de conversión de USD a MXN es:", resultado)
else:
    print("Tipo de conversión no disponible")

