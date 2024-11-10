const wordele = document.querySelector(".ans");
let word = document.querySelector(".ans").innerHTML;
const submitButton = document.querySelector(".sub")



if (document.querySelector("img").getAttribute("src") === "/static/images/5.png") {
    submitButton.setAttribute("disabled", "true");
    submitButton.style.backgroundColor = "red";
    submitButton.style.border = "black";
}

// function full(){
//     const ch = word.split("");
//     let dashed = false;

//     for(let i=0; i<ch.length; i++){
//         if(ch[i]=="_"){
//             dashed =true;
//             break;
//         }

//     if(dashed === false){
//         submitButton.setAttribute("disabled", "true");
//         submitButton.style.backgroundColor = "red";
//         submitButton.style.border = "black";
//     }
//     }
// }

// submitButton.onclick=full;



function blinker(){
    let chars = word.split("");
    for(let i=0; i<chars.length; i++){
        if(chars[i]=="_"){
            chars[i]=" ";
        }
        else if(word[i]==" "){
            chars[i] = "_";
        }
    word = chars.join("");
    wordele.innerHTML = word;
}};

setInterval(blinker, 400);

