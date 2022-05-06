let grid = document.getElementById('grid');

function buildGrid(){

    for (let i = 0; i<6; i++){
        let row = document.createElement('div')
        for (let j = 0; j<5; j++){
            let cell = document.createElement('div')
            cell.className = 'cell'
            cell.textContent = 'A'
            row.appendChild(cell)
        }
        grid.appendChild(row)
    }
}

buildGrid();

let wordList = [
    'patio',
    'darts',
    'piano',
    'horse',
]

let randomIndex = Math.round(Math.random()* wordList.length)
let secret = wordList[randomIndex]

let attempts = []
let currentAttempt = ''

let counter = 0

function updateGrid(){
    let row = grid.firstChild
    for (let attempt of attempts){
        drawPastAttempt(row,attempt)
        row = row.nextSibling
    }
    drawCurrentAttempt(row, currentAttempt)
}
