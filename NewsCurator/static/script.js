let subButton = document.body.querySelector("button");
let left = document.body.querySelector(".left");
let video = document.body.querySelector("video");
let titles;

subButton.onclick = () => {
    left.style.justifyContent = 'start';

    setTimeout(() => {
        titles = document.querySelectorAll(".title");

        if (titles.length > 0) { // Check if titles exist
            for (let i = 0; i < titles.length; i++) {
                console.log(titles[i]);
            }
        } else {
            console.log("No titles found");
        }
    }, 2000);
};
