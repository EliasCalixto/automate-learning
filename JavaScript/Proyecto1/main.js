function onDocumentLoaded(){
    const root=document.getElementById('root')

    const section1 = document.createElement('section')
        root.appendChild(section1)

    printSection1 = () =>{
        section1.classList.add('border','bg-info','mx-auto','text-center','rounded','m-2')
        const h1 = document.createElement('h1')
        h1.classList.add('h1')
        h1.textContent='Este es el h1'
        section1.appendChild(h1)

        const p1 = document.createElement('p')
        p1.classList.add('h4')
        p1.textContent='texto en el p1 asdasdasdasdasdasasdadsasadsadsasd'
        section1.appendChild(p1)
    }

    const createDiv2 = () =>{
        const div2=document.createElement('div')
        div2.classList.add('border','bg-success','mx-auto','text-center','p-4')
        root.appendChild(div2)

        const print5Divs = () =>{
            for(let n = 0; n < 5; n++){
                var asd = document.createElement('div') 
                asd.classList.add('border','rounded','bg-success','p-2','mx-auto','w-25','text-center','h3')
                asd.textContent='asdasd'
                div2.appendChild(asd)
            }
        }
        print5Divs()
    }
    createDiv2()
}

document.addEventListener('DOMContentLoaded',onDocumentLoaded)