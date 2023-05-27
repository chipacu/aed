Lógicos
=======

Los operadores lógicos, nos permiten tomar decisiones basadas en la verdad y la falsedad de las proposiciones. Nos guían a través del laberinto de la lógica y nos permiten construir algoritmos que actúan con discernimiento.

.. tab:: Disyunción 

   .. list-table::
      :widths: 25 25 50
      :header-rows: 1

      * - A
        - B
        - :code:`A o B`
      * - Falso ❌
        - Falso ❌
        - **Falso** ❌
      * - Falso ❌
        - Verdad ✔
        - **Verdad** ✔
      * - Verdad ✔
        - Falso ❌
        - **Verdad** ✔
      * - Verdad ✔
        - Verdad ✔
        - **Verdad** ✔

.. tab:: Conjunción 

   .. list-table::
      :widths: 25 25 50
      :header-rows: 1

      * - A
        - B
        - :code:`A y B`
      * - Falso ❌
        - Falso ❌
        - **Falso** ❌
      * - Falso ❌
        - Verdad ✔
        - **Falso** ❌
      * - Verdad ✔
        - Falso ❌
        - **Falso** ❌
      * - Verdad ✔
        - Verdad ✔
        - **Verdad** ✔

.. tab:: Negación 

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - A
        - :code:`No(A)`
      * - Falso ❌
        - **Verdad** ✔
      * - Verdad ✔
        - **Falso** ❌