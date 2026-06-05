
# 1 - Imprimir un mensaje de bienvenida a la tienda de manzanas 
print("*****************************************")
print("******      BIENVENDIDOS         ********")
print("*****  A LA TIENDA DE MANZANAS  *********")
print("*****************************************")

#2 - Pedir al cliente su nombre completo, y guardarlo en una variable llamada nombre_completo
print("Por favor ingrese su nombre completo: ")
nombre_completo = input()

#3 - Imprimir un mensaje, saludando al usuario por su nombre, e indicando que actualmente tiene 20 manzanas en stock
# el precio de cada manzana es de 5 (puede ser en peso, euro, dólar, ect).

manzanas_en_stock = 20
precio_manzana = 5 #precio de cada manzana
print("Bienvenido a la tienda de Manzanas, Señor:", nombre_completo, ".")
print("Actualmente tenemos", manzanas_en_stock, "manzanas en stock") 
print("El precio de cada manzana es de COP$:", precio_manzana)

#4 - Preguntar al cliente cuantas manzanas desea comprar 
print("Por favor nos indica cuantas manzanas quiere comprar?")

#4.1 - Validar si la cantidad solicitada es valida
if manzanas > manzanas_en_stock:
  print("Excuse, en el momento no contamos con la cantidad de manzanas deseadas")
else
#Calcular el valor total y mostrarlo
total_compra_manzanas = manzanas_comprar * 5
print("Usted compró {manzanas_comprar} manzanas_comprar, el precio total a pagar es de {total_compra_manzanas}")

#5 - El cliente ingresa el número de manzanas que desea comprar 
manzanas_comprar = input()

total_compra_manzanas = int(manzanas_comprar) * 5  

#6 - Indique cuantas manzanas compró el cliente, y cuanto gastó en total por su compra  
print("El cliente compró: ", manzanas_comprar)
print("El cliente gastó en total por su compra: COP$", total_compra_manzanas)

#7 - Indique cuantas manzanas quedan en stock después de la compra del cliente 
print("En la tienda nos queda en stock:" , manzanas_en_stock - int(manzanas_comprar))  


