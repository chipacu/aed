Cómo escribir pseudocódigo
==========================

Para comenzar, podemos ver la estructura básica de la cátedra.

.. code-block::
    :caption: Acordate que se ejecuta secuencialmente (de arriba para abajo).

    Accion Un_ejemplo es
        Ambiente
            // aquí se declaran variables/c, se definen funciones/p...
        Algoritmo
            // donde ocurre la magia...
    fin accion

.. admonition:: Escritura flexible.
    :class: tip

    En pseudocódigo te podés encontrar estas y otras instrucciones escritas con mayúsculas o minúsculas indistintamente, eso al parecer, no es tan importante y los profes te lo tomas como válido (Ej: :code:`AMBIENTE / ambiente`). En lenguajes reales, esto ya no es tan así.

Guarda con la indentación
-------------------------

La "indentación" en criollo, es cuando nos referirnos a la **sangría** del código. Por ahora no es indispensable, pero si se recomienda usarla, de lo contrario muere un perrito.

No, en serio, indentá bien lctm.

.. tab:: Sin indentar 👿

    .. code-block::

        Para i := 1 a 10 hacer
        Si i mod 2 = 0 entonces
        Escribir(i)
        Fin si
        Fin Para


.. tab:: Indentado 😇

    .. code-block::

        Para i := 1 a 10 hacer
            Si i mod 2 = 0 entonces
                Escribir(i)
            Fin si
        Fin Para
