
 ***Que es un modelo?***

En matematicas y computacion es una formula matematica simplificada que intenta imitar la realidad. Se podria ver a un modelo como un mapa... 
    
    - Nunca es perfecto 
    - Su objetivo es ser util para navegar
      Matematicamente, un modelo es una funcion f(x): y = f(x) + error

Donde:  X (input): Los datos 
        y (output): La prediccion   
        f (funcion): Regla interna que transforma X en y

Cuando creamos un modelo estamos eligiendo que forma tendra esa f

Existen familias de modelos que se utilizan segun el problema:

 * Modelos lineales (Regresion logistica y Regresion Lineal): Este tipo de modelos imaginan que el mundo es una linea recta. Su formula es simple, * y = m * x + b *
 Este tipo de modelos se utiliza cuando la relacion es simple y proporcional (por ej: "mientras mas cara sea la casa")

 * Modelos de arboles (Decision Trees y Random Forest): Estos modelos realizan preguntas en cadena (por ej: "¿El precio es mayor a 1000? Sí. -> ¿La volatilidad es alta? No. -> Entonces Sube". )
Se utilizan cuando los datos tienen reglas complejas "saltos" y  no siguen una linea recta. 

 * Redes neuronales (Deep Learning): Este modelo imita la estructura del cerebro con capas  de "neuronas" conectadas. Se utiliza para datos no estructurados como reconocer imagenes, audios, texto, etc.



***Como funciona .fit(data_train, data_real)***
Es un proceso de Optimización. Imagina que el modelo es una radio vieja con muchas perillas (parámetros).

* Inicio: El modelo pone las perillas en una posición al azar.

* Prueba: Mira la primera fila de X_train, hace una predicción y la compara con la respuesta real y_train.

* Cálculo del Error (Loss Function): Calcula qué tan lejos estuvo.

* Ajuste: Mueve las perillas un milímetro para intentar reducir ese error.

* Repetición: Lo hace miles de veces hasta que mover las perillas ya no reduce más el error.

