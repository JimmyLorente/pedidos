var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

//añadir pizza

function addEnsalada(pid){
    // Nombe de la ensalada
    pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;    
    // precio de la ensalada
    var radio = 'ensalada' + pid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if (pri[0].checked) {
        price = pri[0].value;
        size = 'M';
    }
    else {
        price = pri[1].value
        size = 'L';
    }
    var orders  = JSON.parse(localStorage.getItem('orders'));
    var total   = localStorage.getItem('total');
    var cartSize =orders.length;
    // Guardar item dento del carrito 
    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders',JSON.stringify(orders));


    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // Guardar items dentro del carrito
    var cart = document.querySelector("#cart");
    cart.innerHTML  = orders.length;


    butto = '<button class="del" onclick="removeEnsalada(' + cartSize + ')">X</button>';
    ptotal.innerHTML = 'Total: ' + total +' $';
    pcart.innerHTML += '<li>'+ name + ' ' + size + ': '  + price + '$' + butto + '</li>';
}

function pshoppinCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        butto = '<button class="del" onclick="removeEnsalada(' + i + ')">X</button>';
        pcart.innerHTML += '<li>'+ orders[i][0] + ' ' + orders[i][1] + ': '  + orders[i][2] + '$'+ butto + '</li>';        
    }
    ptotal.innerHTML = 'Total: ' + total +' $';
}
pshoppinCart();

function removeEnsalada(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total - Number(orders[n][2]));
    orders.splice(n, 1);

    var cart = document.querySelector("#cart");
    cart.innerHTML  = orders.length;
    
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    pshoppinCart();
}