<head>
  <link rel="stylesheet" type="text/css" href="terminal/asciinema-player.css" />
  <script src="terminal/asciinema-player.min.js"></script>
</head>

# La terminal

Correr Python desde la terminal es la forma más básica de usarlo
y, aunque no vayan a usar Python de esta manera,
es útil entender como funciona.
Los otros entornos que usen para correr Python,
como Google Colab,
van a estar haciendo esto detrás de escenas.

## De manera interactiva

Para correr Python de manera interactiva,
escribimos `python` en una terminal,
y se abre un *REPL* (*Read-Eval-Print-Loop*),
que va a leer (*read*) los comandos que escribamos,
evaluarlos (*eval*),
mostrar o imprimir (*primt*) el resultado,
y repetir (*loop*) estos pasos.

Después vamos a ver más en detalle que hace el código,
pero,
para entender que esta pasando,
la sintaxis `x = 1`
define una variable con el nombre `x`,
donde *guarda* el valor `1`,
para que lo podamos reutilizar más adelante.

<div id="interactive"></div>
<script>AsciinemaPlayer.create({data: [
{"version": 2, "width": 80, "height": 13, "timestamp": 1679010876, "env": {"SHELL": "/bin/zsh", "TERM": "xterm-256color"}},
[0., "o", "maurosilber@annie ~ % "],
[0.5, "o", "p"],
[0.6, "o", "y"],
[0.7, "o", "t"],
[0.8, "o", "h"],
[0.9, "o", "o"],
[1.0, "o", "n"],
[1.1, "o", "3"],
[1.2, "o", "\r\n"],
[1.5, "o", "Python 3.11.2 (main, Feb 16 2023, 02:55:59) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin\r\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\r\n"],
[2.0, "o", ">>> "],
[2.0, "o", "2"],
[2.1, "o", " "],
[2.2, "o", "+"],
[2.3, "o", " "],
[2.4, "o", "2"],
[2.5, "o", "\r\n"],
[2.5, "o", "4"],
[2.5, "o", "\r\n"],
[2.5, "o", ">>> "],
[3.0, "o", "x"],
[3.1, "o", " "],
[3.2, "o", "="],
[3.3, "o", " "],
[3.4, "o", "1"],
[3.5, "o", "\r\n"],
[3.5, "o", ">>> "],
[4.0, "o", "x"],
[4.1, "o", "\r\n"],
[4.1, "o", "1"],
[4.1, "o", "\r\n"],
[4.1, "o", ">>> "],
[4.6, "o", "y"],
[4.7, "o", " "],
[4.8, "o", "="],
[4.9, "o", " "],
[5.0, "o", "2"],
[5.1, "o", " "],
[5.2, "o", "*"],
[5.3, "o", " "],
[5.4, "o", "x"],
[5.5, "o", "\r\n"],
[5.5, "o", ">>> "],
[6.0, "o", "p"],
[6.1, "o", "r"],
[6.2, "o", "i"],
[6.3, "o", "n"],
[6.4, "o", "t"],
[6.5, "o", "("],
[6.6, "o", "y"],
[6.7, "o", ")"],
[6.8, "o", "\r\n"],
[6.8, "o", "2\r\n"],
[6.8, "o", ">>> "]
]},
document.getElementById("interactive"),
{
    rows: 13,
    preload: true,
    }
);</script>

## Desde un archivo de texto

Para poder volver a correr un mismo código
sin tener que tipearlo nuevamente,
los programas se escriben en un archivo de texto.
Generalmente,
se suelen guardar con extensión `.py`,
para señalar que es un archivo de Python.

Por ejemplo,
en un archivo de texto escribimos
los mismos los comandos del ejemplo anterior:

```python
2 + 2
x = 1
x
y = 2 * x
print(y)
```

y lo guardamos como `ejemplo.py`.

Para correr este código,
en la terminal ponemos:

```sh
python ejemplo.py
```

<div id="non-interactive"></div>
<script>AsciinemaPlayer.create({data: [
{"version": 2, "width": 80, "height": 10, "timestamp": 1679010876, "env": {"SHELL": "/bin/zsh", "TERM": "xterm-256color"}},
[0., "o", "maurosilber@annie ~ % "],
[0.5, "o", "p"],
[0.6, "o", "y"],
[0.7, "o", "t"],
[0.8, "o", "h"],
[0.9, "o", "o"],
[1.0, "o", "n"],
[1.1, "o", "3"],
[1.2, "o", " "],
[1.3, "o", "e"],
[1.4, "o", "j"],
[1.5, "o", "e"],
[1.6, "o", "m"],
[1.7, "o", "p"],
[1.8, "o", "l"],
[1.9, "o", "o"],
[2.0, "o", "."],
[2.1, "o", "p"],
[2.2, "o", "y"],
[2.3, "o", "\r\n"],
[2.5, "o", "2\r\n"],
[3.0, "o", "maurosilber@annie ~ % "]
]},
document.getElementById("non-interactive"),
{
    rows: 5,
    preload: true,
    }
);</script>

Noten que,
a diferencia de cuando lo corremos de manera interactiva,
solo vemos el resultado de la expresión que está dentro de `print(...)`.

## De manera mixta

Estas dos maneras de correr código no son exclusivas.
Podemos empezar corriendo un archivo de texto y,
luego,
seguir interactuando con las variables que quedaron definidas.
Para ello,
hay que agregar `-i` (de interactivo) al correr el archivo:

```sh
python -i ejemplo.py
````

<div id="mixed"></div>
<script>AsciinemaPlayer.create({data: [
{"version": 2, "width": 80, "height": 10, "timestamp": 1679010876, "env": {"SHELL": "/bin/zsh", "TERM": "xterm-256color"}},
[0., "o", "maurosilber@annie ~ % "],
[0.5, "o", "p"],
[0.6, "o", "y"],
[0.7, "o", "t"],
[0.8, "o", "h"],
[0.9, "o", "o"],
[1.0, "o", "n"],
[1.1, "o", "3"],
[1.2, "o", " "],
[1.3, "o", "-"],
[1.4, "o", "i"],
[1.5, "o", " "],
[1.6, "o", "e"],
[1.7, "o", "j"],
[1.8, "o", "e"],
[1.9, "o", "m"],
[2.0, "o", "p"],
[2.1, "o", "l"],
[2.2, "o", "o"],
[2.3, "o", "."],
[2.4, "o", "p"],
[2.5, "o", "y"],
[2.6, "o", "\r\n"],
[3.0, "o", "2\r\n"],
[3.5, "o", ">>> "],
[4.5, "o", "x"],
[4.6, "o", "\r\n"],
[5.0, "o", "1\r\n"],
[5.0, "o", ">>> "]
]},
document.getElementById("mixed"),
{
    rows: 5,
    preload: true,
    }
);</script>
