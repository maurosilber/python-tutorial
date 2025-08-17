<head>
<style>
    .buttons {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1em;

        height: 10em;

        button,
        input {
            font-size: large;
        }

        input {
            width: 8em;
            text-align: center;
        }

        label {
            text-align: right;
            align-content: center;
        }
    }

    table {
        max-height: 150px;
        overflow-y: auto;
        display: block;

        text-align: center;

        thead th {
            position: sticky;
            top: 0;
            background: white;
            z-index: 1;
        }

        tbody tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        tbody tr:nth-child(odd) {
            background-color: #fff;
        }
    }
</style>
</head>

# Cronómetro

Presionar el botón:

- **medir**: para realizar mediciones (o la "M" en el teclado).
- **borrar**: borra la tabla de mediciones y reinicia el cronómetro.
- **exportar**: descarga las mediciones en un archivo de texto.

````{admonition} Las mediciones son consecutivas.
:class: note, dropdown
Se puede calcular periodos
como la diferencia entre dos mediciones consecutivas.

En Python,
```python
import numpy as np

tiempos = np.loadtxt("datos.txt")
periodos = np.diff(tiempos)  # [t1-t0, t2-t1, ...]
```
````

::::{grid}

:::{grid-item}
:columns: 8

<div class="buttons">
<label for="total_tiempo">Tiempo</label>
<input id="total_tiempo" readonly value=0>
<button id="start"><u>M</u>edir (M)</button>
<label for="total_mediciones">Mediciones</label>
<input id="total_mediciones" readonly value=0>
<button id="reset">Borrar</button>
<label for="nombre_archivo">Nombre</label>
<input id="nombre_archivo" value="datos.txt">
<button id="export">Exportar</button>
</div>
:::

:::{grid-item}
:columns: 4

<table>
    <thead>
        <tr>
            <th>Tiempo [s]</th>
        </tr>
    </thead>
    <tbody id="table">
    </tbody>
</table>
:::

::::

<script>
    // Define variables
    let startTime = null;
    let table = document.getElementById("table")
    let total_mediciones = document.getElementById("total_mediciones")
    let total_tiempo = document.getElementById("total_tiempo")
    let currentTime;

    // Define functions
    function addTime() {
        let time = new Date();
        if (startTime === null) {
            startTime = time;
            currentTime = setInterval(() => total_tiempo.setAttribute("value", getTime()), 10)
        }
        let elapsed = (time - startTime) / 1000;
        let newText = document.createTextNode(elapsed.toFixed(3));
        table.insertRow().insertCell().appendChild(newText);
        // Scroll table to bottom
        table.parentElement.scrollTop = table.parentElement.scrollHeight;total_mediciones.value = parseFloat(total_mediciones.value) + 1;
    }

    function getTime() {
        let time = new Date();
        return (time - startTime) / 1000;
    }

    function resetTimer() {
        startTime = null;
        table.innerHTML = "";
        total_mediciones.value = "0";
        clearInterval(currentTime);
        total_tiempo.setAttribute("value", 0);
    }

    function exportCsv() {
        let blob = new Blob(['# tiempo [s]\r\n' + table.innerText.replaceAll("\n", "\r\n")], { type: 'text/csv;charset=utf-8;' });
        let url = URL.createObjectURL(blob);
        let link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', document.getElementById("nombre_archivo").value);
        document.body.appendChild(link);
        link.click();
    }

    // Attach event listeners
    document.getElementById('start').addEventListener('click', addTime);
    document.getElementById('reset').addEventListener('click', resetTimer);
    document.getElementById('export').addEventListener('click', exportCsv);
    addEventListener("keydown", (event) => {
      if (
        !event.repeat &&
        event.key.toLowerCase() === "m" &&
        event.target.id != "nombre_archivo"
      ) {
        addTime();
      }
    });
</script>
