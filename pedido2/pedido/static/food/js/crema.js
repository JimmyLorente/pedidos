var ccart = document.querySelector('#ccart');
var ctotal = document.querySelector('#ctotal');

// Añadir al carrito

function addCrema(pid){
    // nombre de la ensalada
    cremasId = '#crem' + pid;
    var name = document.querySelector(cremasId).innerHTML;    
    // precio de la ensalda
    var radio = 'crema' + pid;
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
    butto = '<button class="del" onclick="removeCrema(' + cartSize + ')">X</button>';
    ctotal.innerHTML = 'Total: ' + total + ' $';
    ccart.innerHTML += '<li>'+ name + ' ' + size + ': '+ price +'$' + butto + '</li>';
}

function cshoppingCart() {
    var orders  = JSON.parse(localStorage.getItem('orders'));
    var total   = localStorage.getItem('total');
    var cartSize = orders.length;
    ccart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        butto = '<button class="del" onclick="removeCrema(' + i + ')">X</button>';
        ccart.innerHTML += '<li>'+ orders[i][0] + ' ' +orders[i][1]  + ': ' + orders[i][2] +' $' + butto + '</li>'; 
    }
    ctotal.innerHTML = 'Total: '+ total + '$';
}

cshoppingCart();

function removeCrema(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total - Number(orders[n][2]));
    orders.splice(n, 1);

    var cart = document.querySelector("#cart");
    cart.innerHTML  = orders.length;
    
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    cshoppinCart();
}