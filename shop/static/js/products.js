const add_to_cart = document.querySelectorAll('.add_to_cart');
const cart_icon = document.querySelector('.cart_items_numbre')
let cart_items = parseInt(cart_icon.textContent)

add_to_cart.forEach( button => {
    button.addEventListener('click', e => {
    e.preventDefault();
    console.log('clicked')
    let _data = {
            id: add_to_cart.dataset.id ,
        }
        
    fetch('{% url "cart:cart_add_ajax" %}',
    {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest' },
        body: JSON.stringify(_data)              
    }).then(response => response.json())
    .then(response => {
        if (response['status'] == 'ok') {
            cart_items += 1
        }
    })
});
    
})