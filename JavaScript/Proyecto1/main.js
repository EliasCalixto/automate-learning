function onDocumentLoaded(){
    const root=document.getElementById('root')

    const print5Divs = () =>{
        for(let n = 0; n < 5; n++){
            var div1 = document.createElement('div') 
            div1.classList.add('border','rounded','bg-success','p-2','mx-auto','w-25','text-center','h3')
            div1.textContent='asdasd'

            console.log(div1)
            root.appendChild(div1)
        }
    }

    print5Divs()
    print5Divs()
}

document.addEventListener('DOMContentLoaded',onDocumentLoaded)