let checka = document.getElementById('checka')
let a0 = document.getElementById('a0')
let labela = document.getElementById('labela')

let checkb = document.getElementById('checkb')
let b0 = document.getElementById('b0')
let labelb = document.getElementById('labelb')

let checkc = document.getElementById('checkc')
let c0 = document.getElementById('c0')
let labelc = document.getElementById('labelc')

let checkd = document.getElementById('checkd')
let d0 = document.getElementById('d0')
let labeld = document.getElementById('labeld')

let checke = document.getElementById('checke')
let e0 = document.getElementById('e0')
let labele = document.getElementById('labele')

checka.addEventListener('click',()=>{
    if(checka.checked == true) {
        a0.hidden = true;
        labela.innerHTML="👉";
    } else if(checka.checked == false) {
        a0.hidden = false;
        labela.innerHTML="👇";
    }
})

checkb.addEventListener('click',()=>{
    if(checkb.checked == true) {
        b0.hidden = true;
        labelb.innerHTML="👉";
    } else if(checkd.checked == false) {
        b0.hidden = false;
        labelb.innerHTML="👇";
    }
})

checkc.addEventListener('click',()=>{
    if(checkc.checked == true) {
        c0.hidden = true;
        labelc.innerHTML="👉";
    } else if(checkc.checked == false) {
        c0.hidden = false;
        labelc.innerHTML="👇";
    }
})

checkd.addEventListener('click',()=>{
    if(checkd.checked == true) {
        d0.hidden = true;
        labeld.innerHTML="👉";
    } else if(checkd.checked == false) {
        d0.hidden = false;
        labeld.innerHTML="👇";
    }
})

checke.addEventListener('click',()=>{
    if(checke.checked == true) {
        e0.hidden = true;
        labele.innerHTML="👉";
    } else if(checke.checked == false) {
        e0.hidden = false;
        labele.innerHTML="👇";
    }
})