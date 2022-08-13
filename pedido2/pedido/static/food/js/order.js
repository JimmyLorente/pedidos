var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

// Añadir al carrito

function addEnsalada(pid){
    // nombre de la ensalada
    pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;    
    // precio de la ensalda
    var radio = 'ensalada' + pid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if (pri[0].cheked) {
        price = pri[0].value;
        size = 'M';
    }
    else {
        price = pri[1].value;
        size = 'L';
    }
    var orders  = JSON.parse(localStorage.getItem('orders'));
    var total   = localStorage.getItem('total');
    var cartSize = orders.length;

    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders',JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);


    // Los numero que van al carrito
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    // Aqui el total de todo
    butto = '<div class="del" onclick="removerEnsalada(' + cartSize + ')">x</div>';
    ptotal.innerHTML = 'Total: ' + total + ' $';
    pcart.innerHTML += '<li>'+ name + ' ' + size + ': '+ price + '$' + butto +'</li>';
}

function pshoppingCart() {
    var orders  = JSON.parse(localStorage.getItem('orders'));
    var total   = localStorage.getItem('total');
    var cartSize = orders.length;
    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        butto = '<div class="del" onclick="removerEnsalada(' + i + ')">x</div>';
        pcart.innerHTML += '<li>'+ orders[i][0] + ' ' +orders[i][1]  + ': ' + orders[i][2] +' $' + butto + '</li>'; 
    }
    ptotal.innerHTML = 'Total: '+ total + '$';
}

pshoppingCart();

function removerEnsalada(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders',JSON.stringify(orders));
    localStorage.setItem('total', total);
    pshoppingCart();

}