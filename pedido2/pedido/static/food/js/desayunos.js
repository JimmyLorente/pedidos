var dcart = document.querySelector('#dcart');
var dtotal = document.querySelector('#dtotal');

// Añadir al carrito

function addDesayunos(pid){
    // nombre de la ensalada
    desayunoId = '#desa' + pid;
    var name = document.querySelector(desayunoId).innerHTML;    
    // precio de la ensalda
    var radio = 'desayunos' + pid;
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
    butto = '<button class="del" onclick="removeDesayunos(' + cartSize + ')">X</button>';
    dtotal.innerHTML = 'Tota:' +total + '$';
    dcart.innerHTML += '<li>'+ name + ' ' + size + ': '+ price +'$' + butto + '</li>';
}

function dshoppingCart() {
    var orders  = JSON.parse(localStorage.getItem('orders'));
    var total   = localStorage.getItem('total');
    var cartSize = orders.length;
    dcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        butto = '<button class="del" onclick="removeDesayunos(' + i + ')">X</button>';
        dcart.innerHTML += '<li>'+ orders[i][0] + ' ' +orders[i][1]  + ': ' + orders[i][2] +' $' + butto + '</li>'; 
    }
    dtotal.innerHTML = 'Total: '+ total + '$';
}

dshoppingCart();

function removeDesayunos(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total - Number(orders[n][2]));
    orders.splice(n, 1);

    var cart = document.querySelector("#cart");
    cart.innerHTML  = orders.length;
    
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    dshoppinCart();
}