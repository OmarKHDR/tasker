const btn = document.getElementById('prim-1');
btn.style.cursor = 'pointer'
btn.addEventListener("click", (event)=>{
    event.preventDefault();
    const email = document.getElementById('email-input').value;
    const password1 = document.getElementById('pass-input1').value;
    if (email.match(/[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$/) === null){
        window.alert("enter a valid email examble@domain.com")
    } else if (password1.length < 8) {
        window.alert("Password should at least be 8 characters")
    } else{
        fetch('/login', {
            method: 'POST',
            redirect: "follow",
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                'email': email,
                'password': password1,
            })
        }).then(res=>{
            if (res.redirected){
                window.location.href = res.url
                console.log(res)
            }
        })
        // .then(res=>{
        //     console.log(res);
        //     return res.json()
        // }).then(res=>{
        //     if (res.success.status == true) {
        //         window.alert("success")
        //     }
        //     else {
        //         window.alert(`Failed To login: ${res.success.reason}`)
        //     }
        // })
    }
})
btn2 = document.getElementById('sec-1');
btn2.style.cursor = 'pointer'
btn2.onclick =()=>{
    window.location = "/signup.html"
}

logo = document.getElementsByClassName("logo")[0]
logo.style.cursor = 'pointer'
logo.onclick = () => {
    window.location = "/index.html"
}
