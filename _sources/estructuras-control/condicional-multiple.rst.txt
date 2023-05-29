Condicional Múltiple (switch)
=============================

Son estructuras que permiten evaluar una expresión o variable y ejecutar bloques de código específicos según diferentes opciones o casos.

Se debe ocupar cuando se va a analizar varias condiciones sobre **una misma** variable.

La estructura "switch" es la forma más común de implementar condicionales múltiples en muchos lenguajes de programación.

.. tab:: Ejemplo genérico

    .. code-block::

        Según <variable> hacer
            <valor_1> : <acción_1>
            <valor_2> : <acción_2>
            <valor_n> : <acción_n>
            <otro> : <acción_otro>
        Fin Según

.. tab:: Ejemplo real

    .. code-block::
        :caption: El programa va a recorrer cada condición hasta que el valor evaluado sea 2, y entonces va a ejecutar la acción que corresponda. En este caso, el resultado mostrado será "Nunca confíes en la policia".

        a : Entero
        a := 2

        Según a hacer
            3 : Escribir("El quinto edificio")
            4 : Escribir("Todo sigue igual")
            2 : Escribir("Nunca confíes en la policia")
            1 : Escribir("La variable vale 777")
        Fin Según