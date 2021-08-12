$(".star_img").click(function(){
    if(confirm("관심 리스트에서 제거하시겠습니까?") == true){
        alert("제거되었습니다");
    }
    else{
        return ;
    }
});