const btn = document.getElementById('prim-1');
btn.style.cursor = 'pointer'
btn.addEventListener("click", (event)=>{
    const email = document.getElementById('email-input').value;
    const name = document.getElementById('name-input').value;
    const password1 = document.getElementById('pass-input1').value;
    const password2 = document.getElementById('pass-input2').value;
    if (!name) {
        window.alert("enter your name!")
    } else if (email.match(/[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$/) === null){
        window.alert("enter a valid email examble@domain.com")
    } else if (password1.length < 8) {
        window.alert("Password should at least be 8 characters")
    } else if ( password1 !== password2 ){
        window.alert("passwords fields must match")
    } else{
        fetch('/signup', {
            method: 'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify({
                'name': name,
                'email': email,
                'password': password1,
            })
        }).then((res)=>{
            res = res.json()
            return res
        })
        .then((res)=>{
            if (res.success.status == true) {
                window.alert(`succeed: ${res.success.reason}`)
            }
            else {
                window.alert(`Failed To Signup: ${res.success.reason}`)
            }
        })
    }
    
})
    


const btn2 = document.getElementById('sec-1');
btn2.style.cursor = 'pointer'
btn2.onclick =()=>{
    window.location = "./login.html"
}

const logo = document.getElementsByClassName("logo")[0]
logo.style.cursor = 'pointer'
logo.onclick = () => {
    window.location = "./index.html"
}