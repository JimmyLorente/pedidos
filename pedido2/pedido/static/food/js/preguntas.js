let pregunta = document.querySelectorAll('.pregunta');
let btndebajo = document.querySelectorAll('.pregunta .mas')
let respuesta = document.querySelectorAll('.respuesta');
let parrafo = document.querySelectorAll('.respuesta p');

for ( let i = 0; i < btndebajo.length; i ++) {
    
    let altoParrafo = parrafo[i].clientHeight;
    let switchc = 0;

    btndebajo[i].addEventListener('click', () =>{
        if (switchc == 0) {
            respuesta[i].style.height = `${altoParrafo}px`;
            pregunta[i].style.marginBottom = '10px';
            btndebajo[i].innerHTML = '<i>-</i>';
            switchc ++;
        }

        else if ( switchc == 1 ) {

            respuesta[i].style.height = `0`;
            pregunta[i].style.marginBottom = '0';
            btndebajo[i].innerHTML = '<i>+</i>';
            switchc --;

        }
    })
}