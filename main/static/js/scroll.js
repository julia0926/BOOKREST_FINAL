// const animationTarget = document.querySelector(".js-scroll");
// const animationTarget1 = document.querySelector(".js-scroll1");
// const ANIMATE_CN = "scroll--animate";

// const handleScroll = () => {
//     const animationRectTop = animationTarget.getBoundingClientRect().top;
//     const animationRectTop1 = animationTarget1.getBoundingClientRect().top;
//     const currentWindowHeight = window.pageYOffset;
//     if ((currentWindowHeight /2) > animationRectTop) {
//         console.log("하이하이")
//         animationTarget.classList.add(ANIMATE_CN);
//     }

//     if ((currentWindowHeight /2) > animationRectTop1) {
//         console.log("하이하이")
//         animationTarget1.classList.add(ANIMATE_CN);
//     }

// };

// const init = () => {
//     window.addEventListener("scroll", handleScroll);
// };

// init();

const animationTarget = document.querySelectorAll(".js-scroll");
const SCROLLANIMATE_CN = "scroll--animate";
const body = document.querySelector("body");

const handleScroll = () => {
    for (let item of animationTarget) {
        const itemYpos = item.getBoundingClientRect().top;
        const detectRatio = window.innerHeight * 0.5;

        console.log(itemYpos);
        if (itemYpos < detectRatio) {
            item.classList.add(SCROLLANIMATE_CN);
        }
    }
};

const scrollInit = () => {
    body.addEventListener("scroll", handleScroll);
};

scrollInit();
