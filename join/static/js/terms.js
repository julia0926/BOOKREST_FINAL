const termsForm = document.querySelector(".termsForm");
const register = document.querySelector(".js-register");
const noregister = document.querySelector(".js-noregister");

const termsBox = document.querySelector(".js-termsBox");
const signupBox = document.querySelector(".js-signupBox");
const SHOWING_CN = "showing";

const signupAnimate = () => {
  termsBox.classList.remove(SHOWING_CN);
  signupBox.classList.add(SHOWING_CN);

};


const onNoregisterClick = (event) => {
  event.preventDefault();
  if (window.confirm("회원가입을 취소하고 BOOKREST 첫 화면으로 돌아가시겠습니까?")) {
    location.replace("/");
  }
};

const termsCheckbox = (event) => {
  event.preventDefault();
  const agreement1 = document.querySelector(".js-agreement1");
  const agreement2 = document.querySelector(".js-agreement2");
 
  if (!agreement1.checked) {
    window.alert("이용약관 이용동의는 필수입니다.");
  } else if (!agreement2.checked) {
    window.alert("개인정보의 수집 및 이용동의는 필수입니다.");
  } else {
    signupAnimate();
  }
};

const agreeInit = () => {
  register.addEventListener("click", termsCheckbox);
  noregister.addEventListener("click", onNoregisterClick);
};

agreeInit();
