function onDocumentLoaded(){
    sum = (num1,num2) => {
        num1 = parseInt(prompt('ingrese num1:'))
        num2 = parseInt(prompt('ingrese num2:'))
        alert(num1+num2)
    }
    res = (num1,num2) => {
        num1 = parseInt(prompt('ingrese num1:'))
        num2 = parseInt(prompt('ingrese num2:'))
        alert(num1-num2)
    }
    mul = (num1,num2) => {
        num1 = parseInt(prompt('ingrese num1:'))
        num2 = parseInt(prompt('ingrese num2:'))
        alert(num1*num2)
    }
    div = (num1,num2) => {
        num1 = parseInt(prompt('ingrese num1:'))
        num2 = parseInt(prompt('ingrese num2:'))
        let result = (num1/num2).toFixed(2)
        alert(result)
    }
    test = () =>{
        what = (Math.random()*10000).toFixed(2)
        alert(what)
    }
}

document.addEventListener('DOMContentLoaded',onDocumentLoaded)