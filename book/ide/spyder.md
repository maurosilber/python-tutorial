# Spyder

[Spyder](https://www.spyder-ide.org)
es un entorno de desarrollo integrado (IDE)
para Python.
Principalmente,
se compone de un editor de texto
y la consola o terminal de Python.
A diferencia de un editor de texto común,
nos ofrece ciertas herramientas de análisis del código.
Por ejemplo,
nos avisa si cometimos un error de sintaxis
sin tener que correr el código.
En [la documentación de Spyder](https://docs.spyder-ide.org/current/quickstart.html),
tienen más detalles de todos los componentes que tiene (en inglés).

Hay diferentes formas de correr código en Spyder:

- correr un archivo completo
- correr por lineas
- correr por celdas

En particular,
este ültimo es el modo en el que corre código Google Colab.

## Correr archivo completo

Este es análogo al modo mixto en la terminal,
es decir, hacer `python -i ejemplo.py`,
donde el archivo completo se corre linea por linea,
y después podemos seguir de manera interactiva en la terminal:

<video width=100% controls>
  <source src="spyder/run_file.mov" type="video/mp4" />
</video>

Al correr el archivo con el botón ▶️ verde,
quedan definidas dos variables,
`x` e `y`,
que podemos ver en el explorador de variables,
arriba de la consola.

## Correr linea por linea

Otra manera de correr el código es
ejecutarlo linea por linea de manera manual.
Esto se puede hacer con el botón de ▶️ superpuesto a un cursor.
Es equivalente a copiar y pegar esa linea en la consola:

<video width=100% controls>
  <source src="spyder/run_line.mov" type="video/mp4" />
</video>

Noten que,
hasta no correr la linea correspondiente,
la variable aún no está definida en la consola,
y no aparece en el explorador de variables.
Conceptualmente,
en el editor, escribimos "una receta".
En la consola, "la cocinamos".

## Correr por celdas

Finalmente,
una manera similar a correr por lineas,
es correrlo por celdas.
Una celda es un conjunto de lineas delimitado por `# %%`:

<video width=100% controls>
  <source src="spyder/run_cell.mov" type="video/mp4" />
</video>

En el editor de texto,
se resalta la celda donde está ubicado el cursor.

## Peligros al correr por lineas o celdas

Al ver un código,
se presume que este se corre linea por linea,
en orden,
desde el principio hasta el final.
Sin embargo,
al correrlo manualmente,
podemos correr las lineas en otro orden.
Esto puede traer problemas
al querer reproducir los resultados de un análisis.

En el siguiente ejemplo,
se corre el código completo,
para luego borrar la linea `y = 2 * x` en el editor ("receta").
Noten que el editor nos avisa de un posible error en el código,
poniendo un punto rojo en esa linea.
Al volver a correr la linea `print(y)` manualmente,
la variable `y` sigue definida en la consola ("olla"),
y nos muestra su valor.
Más aún,
después cambiamos su valor desde la consola,
sin dejar registrado dicho comando en el editor.

La solución a este problema es correr el archivo completo,
con el botón ▶️ verde,
que corre la receta independientemente de lo que se haya corrido antes.
Nos va a aparecer un error,
avisandonos que la variable `y` no está definida.

<video width=100% controls>
  <source src="spyder/run_combined.mov" type="video/mp4" />
</video>

Otra opción es reiniciar la consola,
desde el menú ☰ de la consola,
que elimina todas las variables.
