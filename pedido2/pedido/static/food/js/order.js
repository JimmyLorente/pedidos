var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

// Añadir al carrito

function addEnsalada(pid){
    // nombre de la ensalada
    pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;
    pcart.innerHTML += '<li>'+ name +'</li>'; 
    // precio de la ensalda
    var radio = 'ens' + pid;
    var price = document.getElementsByName(radio).values;
    
    pcart.innerHTML += '<li>'+ name +''+ price[0].value + '</li>';
}