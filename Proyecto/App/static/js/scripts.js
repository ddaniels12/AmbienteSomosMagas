// static/js/scripts.js
let carrito = [];
let total = 0;

// Toggle para mostrar/ocultar el carrito
document.getElementById('toggleCarrito').addEventListener('click', function() {
    const carritoContenido = document.getElementById('carritoContenido');
    carritoContenido.style.display = carritoContenido.style.display === 'none' ? 'block' : 'none';
});

// Agregar productos al carrito
function agregarAlCarrito(id, nombre, precio) {
    const cantidadInput = document.getElementById(`cantidad_${id}`);
    const cantidad = parseInt(cantidadInput.value) || 0; // Manejar casos donde la entrada no es un número

    if (cantidad <= 0) {
        alert("Por favor, ingresa una cantidad válida.");
        return;
    }

    // Buscar si el producto ya está en el carrito
    const productoExistente = carrito.find(producto => producto.id === id);
    if (productoExistente) {
        productoExistente.cantidad += cantidad;
    } else {
        carrito.push({ id: id, nombre: nombre, precio: precio, cantidad: cantidad });
    }

    // Actualizar el total
    total += precio * cantidad;
    actualizarCarrito();
    alert(`${nombre} ha sido agregado al carrito.`);
}

// Actualizar la visualización del carrito
function actualizarCarrito() {
    const productosCarrito = document.getElementById('productos-carrito');
    productosCarrito.innerHTML = '';

    carrito.forEach(producto => {
        const item = document.createElement('div');
        item.innerHTML = `${producto.nombre} - Precio: $${producto.precio.toFixed(2)} - Cantidad: ${producto.cantidad}`;
        productosCarrito.appendChild(item);
    });

    document.getElementById('total-cantidad').innerText = total.toFixed(2);
}

// Función para limpiar el carrito
function limpiarCarrito() {
    carrito = [];
    total = 0;
    actualizarCarrito();
    alert("El carrito ha sido limpiado.");
}
