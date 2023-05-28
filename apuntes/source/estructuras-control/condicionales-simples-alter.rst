Condicionales Simples o Alternativos (if-else)
====================================

Son mecanismos que permiten tomar decisiones y controlar el flujo de ejecución de un programa en base a si se cumplen o no, ciertas condiciones.

Se debe ocupar cuando se van a analizar varias condiciones sobre **varias variables** distintas.

.. tab:: Condicional simple

    .. code-block::

        Si <condición> entonces
            // acciones si se cumple la condición
        Fin Si
        
.. tab:: Condicional anidado

    .. code-block::

        Si <condición> entonces
            // acciones si se cumple la condición
        sino
            // acciones si NO se cumple la condición
        Fin Si

Si necesitaras evaluar más de una condición, podrías anidar estas estructuras.

.. code-block::
    :caption: Por esto es importante indentar correctamente.

    Si <condición> entonces
        Si <condición> entonces
            // acciones si se cumple la condición
        sino
            // acciones si NO se cumple la condición
        Fin Si
    sino
        Si <condición> entonces
            // acciones si se cumple la condición
        sino
            Si <condición> entonces
                // acciones si se cumple la condición
            Fin Si
        Fin Si
    Fin Si
