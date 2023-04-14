<head>
<style>
    .cronometer-button {
        width: 10ch;
    }
    label, input {
        width: 10ch;
        text-align: right;
    }

</style>
</head>

# Cronómetro

Presionar el botón:
- **medir**: para realizar mediciones (o cualquier tecla en el teclado).
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
:columns: 9
<label for="total_tiempo">Tiempo total</label>
<input id="total_tiempo" readonly value=0>
<button class="cronometer-button" id="start">Medir</button>

<label for="total_mediciones">Mediciones</label>
<input id="total_mediciones" readonly value=0>
<button class="cronometer-button" id="reset">Borrar</button>

<label for="nombre_archivo">Nombre</label>
<input id="nombre_archivo" value="datos.txt">
<button class="cronometer-button" id="export">Exportar</button>
:::

:::{grid-item}
:columns: 3
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
        let newText = document.createTextNode((time - startTime) / 1000);
        table.insertRow().insertCell().appendChild(newText);
        total_mediciones.value = parseFloat(total_mediciones.value) + 1;
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
        if (!event.repeat && event.target.id != "nombre_archivo") addTime()
    });
</script>
