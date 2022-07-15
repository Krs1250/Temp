let copy = document.getElementById("copy")
let information = document.getElementById("information")
let password = document.getElementById("password")
let namea = document.getElementById("namea")
let namec = document.getElementById("namec")
let number = document.getElementById("number")
let numberc = document.getElementById("numberc")
let phone = document.getElementById("phone")
let phonec = document.getElementById("phonec")
let college = document.getElementById("college")
let collegec = document.getElementById("collegec")
let classa = document.getElementById("classa")
let classc = document.getElementById("classc")
information.addEventListener("click",() => {
    passwordr = password.value
    if (passwordr === "010805") {
        copy.style.display = 'inline-block'
    } 
})

namec.addEventListener("click",() => {
    namea.select()
    document.execCommand('copy')
})

numberc.addEventListener("click",() => {
    number.select()
    document.execCommand('copy')
})

phonec.addEventListener("click",() => {
    phone.select()
    document.execCommand('copy')
})

collegec.addEventListener("click",() => {
    college.select()
    document.execCommand('copy')
})

classc.addEventListener("click",() => {
    classa.select()
    document.execCommand('copy')
})