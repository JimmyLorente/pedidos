var acart = document.querySelector('#acart');
var atotal = document.querySelector('#atotal');

// Añadir al carrito

function addAlmuerzos(pid){
    // nombre de la ensalada
    almuerzoId = '#almu' + pid;
    var name = document.querySelector(almuerzoId).innerHTML;    
    // precio de la ensalda
    var radio = 'alm' + pid;
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


    // Guardar items dentro del carrito
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;


    butto = '<button class="del" onclick="removeAlmuerzo(' + cartSize + ')">X</button>';
    atotal.innerHTML = 'Total: ' + total + ' $';
    acart.innerHTML += '<li>'+ name + ' ' + size + ': '+ price +'$' + butto + '</li>';
}

function ashoppingCart() {
    var orders  = JSON.parse(localStorage.getItem('orders'));
    var total   = localStorage.getItem('total');
    var cartSize = orders.length;
    acart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        butto = '<button class="del" onclick="removeAlmuerzo(' + i + ')">X</button>';
        acart.innerHTML += '<li>'+ orders[i][0] + ' ' +orders[i][1]  + ': ' + orders[i][2] +' $'+ butto + '</li>'; 
    }
    atotal.innerHTML = 'Total: '+ total + '$';
}

ashoppingCart();

function removeAlmuerzo(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total - Number(orders[n][2]));
    orders.splice(n, 1);

    var cart = document.querySelector("#cart");
    cart.innerHTML  = orders.length;
    
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    ashoppingCart();
}