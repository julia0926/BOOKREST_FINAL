const currentPath = location.pathname;
const navLinks = document.querySelectorAll(".js-nav__menu__link");
const ANIMATE_CN = "nav__menu__link--animate";

const compareCurrentPath = () => {
  navLinks.forEach((navLink) => {
    if (currentPath === navLink.dataset.path) {
        navLink.classList.add(ANIMATE_CN);
    }
  });
};

const navInit = () => {
  console.log(currentPath);
//   compareCurrentPath();
  window.setTimeout(compareCurrentPath, 130);
};

navInit();
