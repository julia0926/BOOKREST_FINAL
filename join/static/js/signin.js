const signinForm = document.querySelector(".signinForm");
const email = document.querySelector(".email");
const password = document.querySelector(".password");

const errorRed = (input, message) => {
  const formControl = input.parentElement;
  formControl.classList.add("error");
  const small = formControl.querySelector("small");
  small.innerText = message;
};

const successLight = (input) => {
  const formControl = input.parentElement;
  formControl.classList.remove("error");
};

const setDefault = (input, check) => {
  const formControl = input.parentElement;
  formControl.className = "signinBoxTool__signinBox__form-control";
};

const checkPassword = () => {
  if (password.value.length >= 8) {
    successLight(password);
  } else {
    errorRed(password, `비밀번호는 8자 이상이어야 합니다`);
  }
};

const checkEmail = () => {
  const emailRule =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (emailRule.test(email.value.trim())) {
    successLight(email);
  } else {
    errorRed(email, `이메일이 유효하지 않습니다`);
  }
};

const signInit = () => {
  email.addEventListener("input", checkEmail);
  password.addEventListener("input", checkPassword);

  signinForm.addEventListener("submit", (e) => {
    e.preventDefault();
    checkPassword(password, 1, 8);
    checkEmail(email);
  });
};

signInit();