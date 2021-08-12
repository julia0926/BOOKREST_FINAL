const container__slider = document.querySelector(".container__slider");
const firstSlide = document.querySelector(".js-container__slider__img");

const SHOWING_CN = "slider_showing";
const IMG_NUM = 4;

const changeSlide = () => {
  const currentSlide = container__slider.querySelector(`.${SHOWING_CN}`);

  if (currentSlide !== null) {
    currentSlide.classList.remove(SHOWING_CN);
    const nextSlide = currentSlide.nextElementSibling;

    if (nextSlide.className !== "blank") {
      nextSlide.classList.add(SHOWING_CN);
    } else {
      firstSlide.classList.add(SHOWING_CN);
    }
  } else {
    firstSlide.classList.add(SHOWING_CN);
  }
};

const handleSlideClick = () => {
  changeSlide();
};

const slideInit = () => {
  changeSlide();
  setInterval(changeSlide, 5900);
  container__slider.addEventListener("click", handleSlideClick);
};

slideInit();
