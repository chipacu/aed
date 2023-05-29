# aed
Apuntes (no oficiales) para la cursada para Algoritmos y Estructuras de Datos 👨‍💻 de la UTN FRRe 2023. 

Todavia estan muy MUY verdes, falta mucho para que sean usables

## Cómo correr la página en local

1. Instalar python y git
2. Clonar el repositorio y posicionarte

``` powershell
git clone https://github.com/chipacu/aed.git
cd aed/
```

4. Crear un entorno virtual y activarlo

``` powershell
py venv .venv
.\.venv\Scripts\Activate.ps1
```

5. Descargar las dependecias

``` powershell
pip install sphinx furo sphinx-autobuild sphinx-copybutton sphinx-inline-tabs
```

6. Correr el servidor

``` powershell
sphinx-autobuild.exe .\apuntes\source .\apuntes\build\html\
```

7. Abrí tu navegador y poné http://localhost:8000/
