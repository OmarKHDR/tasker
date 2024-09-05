btn = document.getElementById('prim-1');
btn.style.cursor = 'pointer'

btn2 = document.getElementById('sec-1');
btn2.style.cursor = 'pointer'
btn2.onclick =()=>{
    window.location = "./login.html"
}

logo = document.getElementsByClassName("logo")[0]
logo.style.cursor = 'pointer'
logo.onclick = () => {
    window.location = "./index.html"
}