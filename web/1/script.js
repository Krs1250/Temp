const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array) {
    return array[Math.floor(Math.random() * array.length)];
  }

let storyText = '今天气温 34 摄氏度，:inserta:出去遛弯。当走到:insertb:门前时，突然就:insertc:。人们都惊呆了，:insertd:全程目睹但并没有慌，因为:inserta:是一个 130 公斤的胖子，天气又辣么热。'

let insertX = ['a','b','c']
let insertY = ['肯德基','迪士尼乐园','白宫']
let insertZ = ['自燃了','在人行道化成了一坨泥','变成一条鼻涕虫爬走了']

randomize.addEventListener('click', result);

function getRndInteger() {
    return Math.floor(Math.random() * (3) ) ;
  }

function result() {
    newstory = storyText
    xItem = insertX
    yItem = insertY
    zItem = insertZ

    let name ="李雷"

    if(customName.value !== '') {
        name = customName.value;
    }
    alert(newstory)
    
    x = getRndInteger()
    y = getRndInteger()
    z = getRndInteger()
    newstory=newstory.replace(':inserta:',xItem[x])
    newstory=newstory.replace(':insertb:',yItem[y])
    newstory=newstory.replace(':insertc:',zItem[z])
    newstory=newstory.replace(':insertd:',name)
    story.textContent = newstory;
    story.style.visibility = 'visible';
}