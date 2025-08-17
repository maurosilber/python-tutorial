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

````{tab-set}
```{tab-item} Separadas
:name: separadas
Frenando el cronómetro entre mediciones.
```
```{tab-item} Consecutivas
:name: consecutivas
Mediciones consecutivas sin frenar el cronómetro.
```
```{tab-item} Decimales ocultos
:name: decimales
Se ocultan los decimales antes de medir.
```
````

::::{grid}

:::{grid-item}
:columns: 8

<div class="buttons">
<label for="total_tiempo">Tiempo</label>
<input id="total_tiempo" readonly value=0>
<button id="start">Iniciar (M)</button>
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
    let startButton = document.getElementById("start");
    let table = document.getElementById("table")
    let total_mediciones = document.getElementById("total_mediciones")
    let total_tiempo = document.getElementById("total_tiempo")
    let currentTime;
    
    let measurementFunc;
    let shown_time = (t) => t;

    function separateMeasurement() {
        if (startTime === null) {
            startTimer("Frenar (M)")
        } else {
            let time = getTime();
            addMeasurement(time);
            stopTimer()
        }
    }

    function consecutiveMeasurement() {
        if (startTime === null) {
            startTimer("Medir (M)")
        } else {
            let time = getTime();
            addMeasurement(time);
        }
    }

    measurementFunc = separateMeasurement;

    // Get input given its label id
    function getInputFromLabelId(id) {
        let label = document.getElementById(id);
        let input = document.getElementById(label.htmlFor);
        return input
    }

    function attachOnChange(radio, callback) {
        radio.addEventListener('change', (event) => {
            if (event.target.checked) {
                resetTimer();
                callback();
            }
        });
    }

    attachOnChange(getInputFromLabelId("separadas"), () => {
      measurementFunc = separateMeasurement;
      shown_time = (t) => t;
    });

    attachOnChange(getInputFromLabelId("consecutivas"), () => {
      measurementFunc = consecutiveMeasurement;
      shown_time = (t) => t;
    });

    attachOnChange(getInputFromLabelId("decimales"), () => {
      measurementFunc = separateMeasurement;
      shown_time = (t) => Math.floor(t);
    });

    function startTimer(text) {
        startTime = new Date();
        currentTime = setInterval(() => total_tiempo.setAttribute("value", shown_time(getTime())), 10)
        startButton.innerText = text;
    }

    function stopTimer() {
        clearInterval(currentTime);
        total_tiempo.setAttribute("value", 0);
        startTime = null;
        startButton.innerText = "Iniciar (M)";
    }

    function resetTimer() {
        stopTimer()
        table.innerHTML = "";
        total_mediciones.value = "0";
    }

    function addMeasurement(elapsed) {
        // Increase counter
        total_mediciones.value = parseFloat(total_mediciones.value) + 1;
        // Insert new row
        let newText = document.createTextNode(elapsed.toFixed(3));
        table.insertRow().insertCell().appendChild(newText);
        // Scroll table to bottom
        table.parentElement.scrollTop = table.parentElement.scrollHeight;
    }

    function getTime() {
        let time = new Date();
        return (time - startTime) / 1000;
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
    document.getElementById('start').addEventListener('click', measurementFunc);
    document.getElementById('reset').addEventListener('click', resetTimer);
    document.getElementById('export').addEventListener('click', exportCsv);
    addEventListener("keydown", (event) => {
      if (
        !event.repeat &&
        event.key.toLowerCase() === "m" &&
        event.target.id != "nombre_archivo"
      ) {
        measurementFunc()
      }
    });
</script>
