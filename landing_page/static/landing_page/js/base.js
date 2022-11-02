const userDropdownBtn = document.querySelector("#userDropdownBtn")
const hamburgerNavbar = document.querySelector("#hamburgerNavbar")

if (userDropdownBtn !== null) {
    userDropdownBtn.addEventListener('click', () => {
        const userDropdown = document.querySelector("#userDropdown")
        userDropdown.classList.toggle("hidden")
    })
}

if (hamburgerNavbar !== null) {
    hamburgerNavbar.addEventListener('click', () => {
        const navbarItems = document.querySelector("#mobile-menu-2")
        navbarItems.classList.toggle("hidden") 
    })
}