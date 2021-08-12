const introduce = document.querySelector(".js-introduce");
const rule = document.querySelector(".js-rule");
const bookrestMap = document.querySelector(".js-bookrestMap");
const rule2 = document.querySelector(".js-rule2");
const faq = document.querySelector(".js-faq");


const introduceA = document.querySelector(".js-introduceA");
const ruleA = document.querySelector(".js-ruleA");
const bookrestMapA = document.querySelector(".js-bookrestMapA");
const faqA = document.querySelector(".js-faqA");


const NOTICESHOWING_CN = "noticeShowing";
const INTRODUCESHOW = "introduceShow";

const elementList = [introduce, rule, bookrestMap, faq];
let currentIndex = 0;
let beforeIndex = 0;
const elementLinkList = [introduceA, ruleA, bookrestMapA, faqA];

const addClassNameToCurrentElement = (index) => {
  elementList[beforeIndex].classList.remove(NOTICESHOWING_CN);
  elementList[index].classList.add(NOTICESHOWING_CN);
  beforeIndex = index;
};

const noticeInit = () => {
  elementLinkList.map((link, index) => {
    link.addEventListener("click", () => {
      addClassNameToCurrentElement(index);
    });
  });
};

noticeInit();
