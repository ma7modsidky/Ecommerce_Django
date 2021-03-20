const showMenu = (toggleId, navId , otherId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId), 
    other = document.getElementById(otherId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            console.log('clicked')
            nav.classList.toggle('show')
            other.classList.remove('show')
        })
    }
}

showMenu('btnHamburger','header__menu', 'mobileSearch')
showMenu('toggleSearch','mobileSearch', 'header__menu')