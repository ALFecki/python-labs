const tableContainer = document.getElementById('table-container');
const transposeButton = document.getElementById('transpose-button');
const addRowButton = document.getElementById('add-row-button');
const addColumnButton = document.getElementById('add-column-button');
const maxSelectionInput = document.getElementById('max-selection');
const table = document.getElementById('table');

let maxSelection = 1; // Максимальное количество выбора по умолчанию
let selectedCells = [];

const tableSizeInput = document.getElementById('table-size');
const createTableButton = document.getElementById('create-table-button');

createTableButton.addEventListener('click', () => {
    const newSize = parseInt(tableSizeInput.value);
    if (!isNaN(newSize) && newSize > 0) {
        tableSize = newSize;
        generateTable(tableSize);
        selectedCells = [];
    }
});


function generateTable(size) {
    table.innerHTML = '';

    for (let i = 0; i < size; i++) {
        const row = document.createElement('tr');
        for (let j = 0; j < size; j++) {
            const cell = document.createElement('td');
            cell.textContent = Math.floor(Math.random() * 100); // Случайные числа
            row.appendChild(cell);

            cell.addEventListener('click', () => handleCellClick(cell));
        }
        table.appendChild(row);
    }
}

function handleCellClick(cell) {
    if (!cell.classList.contains('selected')) {
        if (selectedCells.length < maxSelection) {
            const lastSelectedCell = selectedCells[selectedCells.length - 1];
            if (!lastSelectedCell || !checkNeighbours(cell)) {
                cell.classList.add('selected');
                selectedCells.push(cell);
            }
        }
    } else {
        cell.classList.remove('selected');
        selectedCells = selectedCells.filter((selectedCell) => selectedCell !== cell);
    }
}

function areNeighbours(cell1, cell2) {
    const row1 = cell1.parentNode;
    const row2 = cell2.parentNode;
    const rowIndex1 = Array.from(row1.children).indexOf(cell1);
    const rowIndex2 = Array.from(row2.children).indexOf(cell2);
    return Math.abs(rowIndex1 - rowIndex2) > 1;
}

function checkNeighbours(cell) {
    if (!selectedCells.forEach((cell1) => {
        if (!areNeighbours(cell, cell1)) {
            return false;
        }
    } )) {
        return false;
    };
    return true
}
transposeButton.addEventListener('click', () => {
    transposeTable();
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});

addRowButton.addEventListener('click', () => {
    tableSize++;
    generateTable(tableSize);
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});

addColumnButton.addEventListener('click', () => {
    tableSize++;
    generateTable(tableSize);
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});


maxSelectionInput.addEventListener('input', () => {
    maxSelection = parseInt(maxSelectionInput.value);
    selectedCells.forEach((cell) => cell.classList.remove('selected'));
    selectedCells = [];
});

function transposeTable() {
    const rows = Array.from(table.querySelectorAll('tr'));
    const cols = rows[0].querySelectorAll('td');
    const newTable = Array.from({ length: tableSize }, () => []);

    rows.forEach((row, rowIndex) => {
        row.querySelectorAll('td').forEach((cell, colIndex) => {
            newTable[colIndex][rowIndex] = cell;
        });
    });

    table.innerHTML = '';

    newTable.forEach((newRow) => {
        const row = document.createElement('tr');
        newRow.forEach((cell) => row.appendChild(cell));
        table.appendChild(row);
    });
}
