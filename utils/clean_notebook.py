from __future__ import annotations

from typing import TypedDict

import nbformat


class Notebook(TypedDict):
    cells: list[Cell]
    metadata: dict
    nbformat: int
    nbformat_minor: int


class Cell(TypedDict):
    cell_type: str
    metadata: dict
    source: str | list
    execution_count: int | None
    outputs: list


def process_notebook(notebook: Notebook):
    clean_notebook(notebook)
    hide_solutions(notebook)


def clean_notebook(notebook: Notebook):
    remove_notebook_metadata(notebook)

    keep = {"tags"}
    for cell in notebook["cells"]:
        remove_cell_metadata(cell, keep=keep)
        if cell["cell_type"] == "code":
            remove_output(cell)


def hide_solutions(notebook: Notebook):
    cells = notebook["cells"]
    for i, cell in enumerate(cells):
        if is_solution_section(cell):
            for cell in cells[i:]:
                if cell["cell_type"] == "code":
                    hide_cell(cell)
                    break

    hide_solutions_in_colab(notebook)


def remove_notebook_metadata(notebook: Notebook):
    metadata = notebook["metadata"]
    metadata.clear()
    metadata["language_info"] = {
        "name": "python",
        "file_extension": ".py",
    }
    # Esto es necesario para que aparezcan
    # el launch button para Google Colb
    metadata["kernelspec"] = {
        "display_name": "python",
        "language": "python",
        "name": "python",
    }


def remove_output(cell: Cell):
    cell["outputs"].clear()
    cell["execution_count"] = None


def remove_cell_metadata(cell: Cell, keep: set[str] = None):
    metadata = cell["metadata"]
    if keep is None:
        metadata.clear()
        return

    cell["metadata"] = {k: v for k, v in metadata.items() if k in keep}


def is_solution_section(cell: Cell):
    title = "# Solución"
    source = cell["source"]

    if isinstance(source, str):
        return title in source

    for line in source:
        if title in line:
            return True
    else:
        return False


def hide_cell(cell: Cell):
    tag = "hide-cell"

    tags = cell["metadata"].setdefault("tags", [])
    if tag not in tags:
        tags.append(tag)


def hide_solutions_in_colab(notebook: Notebook):
    cells = notebook["cells"]
    solution_cells = filter(is_solution_section, cells)

    collapsed_sections = []
    for i, cell in enumerate(solution_cells):
        id = f"solution_{i}"
        cell["metadata"]["id"] = id
        collapsed_sections.append(id)

    if len(collapsed_sections) > 0:
        notebook["metadata"]["colab"] = {"collapsed_sections": collapsed_sections}


if __name__ == "__main__":
    import sys

    file = sys.argv[1]
    notebook = nbformat.read(file, as_version=4)
    process_notebook(notebook)
    nbformat.write(notebook, file)
