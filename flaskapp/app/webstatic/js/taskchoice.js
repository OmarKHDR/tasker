add = document.getElementById('add-btn')
inp = document.getElementById('task-name')
desc = document.getElementById('task-desc')
list = document.getElementById('tags-list')
next = document.getElementById('next-pg')
save = document.getElementById('save-btn')

window.onload = get_tasks;

add.addEventListener('click', event=>{
    event.preventDefault();
    task_name = inp.value.trim();
    task_desc = desc.value.trim();
    if (task_name != ''){
        fetch('')
        tag = document.createElement('li');
        tag.innerHTML = `<span desc="${task_desc}" task_id="${uni_id()}">${task_name} </span>`;
        tag.innerHTML +=  `<img src="/webstatic/images/Vector.png" class="edit-task">`
        list.appendChild(tag)
        save.setAttribute('class','active-save')
        save.value = 'save'
        inp.value = ''
        desc.value = ''
    }
})

list.addEventListener('click', event=>{
    if (event.target.classList.contains('edit-task')){
        console.log('about to fetch')
        fetch('/deletetask/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                'task_id':event.target.parentElement.firstChild.getAttribute('task_id')
            })
        })
        inp.value = event.target.parentElement.firstChild.innerText
        desc.value = event.target.parentElement.firstChild.getAttribute('desc');
        event.target.parentElement.remove()
        save.setAttribute('class','active-save')
        save.textContent = save
    }
})

save.addEventListener('click',(event)=>{
    if (save.getAttribute('class') == 'active-save'){
        save.setAttribute('class','inactive-save')
        save.value = 'saved';
        send_tasks(false)
    }
})


next.addEventListener('click', ()=> send_tasks(true))

function send_tasks(finish){
    let tasks = {}
    ch = list.children
    for (let i=0; i < ch.length; i++){
        tasks[`${ch[i].firstChild.innerText}`] = [ch[i].firstChild.getAttribute('desc'),ch[i].firstChild.getAttribute('task_id')];
    }
    fetch('/createtasks',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            'tasks':tasks,
            'finished':finish
        })
    })
    .then(res=> res.json())
    .then(res=>{
        if (res.status == "failed"){
            if (save.getAttribute('class') == 'inactive-save'){
                save.setAttribute('class','active-save')
                window.alert(`sorry, failed to save: ${res.reason}`)
            }            
        }
    })
}

function get_tasks(){
    fetch('/gettasks/',{
        method:'GET'
    })
    .then(res => res.json())
    .then((res)=>{
        for (let i = 0; i < res.length ; i++){
            tag = document.createElement('li');
            tag.innerHTML = `<span desc="${res[i]['desc']}" task_id=${res[i]['task_id']}>${res[i]['name']} </span>`;
            tag.innerHTML +=  `<img src="/webstatic/images/Vector.png" class="edit-task">`
            list.appendChild(tag)
            save.value = 'save'
        }
    })
}

function uni_id(){
    return Math.random().toString(36).substr(2)+Math.random().toString(36).substr(2);
}