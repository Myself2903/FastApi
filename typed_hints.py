### typed hints ###

#puedes especificar el tipo de dato de una variable como en los lenguajes de tipado fuerte
#a pesar que en python el tipado sea dinamico

my_typed_string: str = "My typed string variable"

#however, esto solo es una convención, en la practica el interprete seguirá entendiendo el 
#tipo de dato sengun el valor que hayas ingresado, en lugar de la definición

my_typed_variable: int = "My typed string variable"


#esto ayuda a la eficiencia de fastApi y al entorno de desarrollo a proponer funciones referentes al
#tipo de dato especificado, es decir, si defines una variable como int y le colocas un string,
#el entorno propondrá funciones de los enteros
