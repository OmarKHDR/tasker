prim_arr = document.getElementsByClassName('prim-btn')
sec_arr = document.getElementsByClassName('sec-btn')
Array.from(prim_arr).forEach(element => {
    element.style.cursor = 'pointer'
    element.onclick = () => {
        window.location = "/signup.html"
    }
});

Array.from(sec_arr).forEach(element => {
    element.style.cursor = 'pointer'
    element.onclick = () => {
        window.location = "/login.html"
    }
});

logo = document.getElementsByClassName("logo")[0]

logo.style.cursor = 'pointer'
logo.onclick = () => {
    window.location = "/index.html"
}
