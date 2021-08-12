$(".return").click(function(){
    if(confirm("반납하시겠습니까?") == true){
        alert("반납신청되었습니다");
    }
    else{
        return ;
    }
});