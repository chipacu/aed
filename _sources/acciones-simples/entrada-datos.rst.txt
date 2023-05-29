Entrada de datos
================

Similar a un ritual ancestral, el programador puede abrir las puertas de la interacción con el usuario. Creando así un vínculo entre el reino digital y el mundo tangible, una conexión que permite que los datos ingresados desde afuera se :doc:`asignen <../acciones-simples/asignacion>` a una :doc:`variable <../variables-constantes/variables>` ya definida.

.. code-block::
    :caption: Se le asigna un valor ingresado por teclado a la variable que se nombró entre <>.

    Leer( <VARIABLE> )

    
Ejemplos:

.. code-block::

    Leer(a)
    Leer(primer-nombre)
    Leer(una_variable, otra_variable, ...)

.. admonition:: Importante!
   :class: important

   Siempre antes de ocupar un :code:`Leer()` debemos ocupar un :code:`Escribir()` con un mensaje detallando qué queremos que el usuario ingrese por pantalla.
   
   .. code-block::

      Escribir(“Ingrese la fecha de forma de Dia, Mes y Año: ”)
      Leer(Dia, Mes, Anio)

