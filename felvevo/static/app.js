function mutatas(){
    $(".buttonka").css("display", "none");
    $(".tag").css("display", "block");
    $(".grid").css("display", "grid");
    //valamiért nem megy a this..
       
        
}
function bejelentkezes(){
    // megnézzük hogy üres-e, ha igen akkor visszadobjuk
    if ($("#vnev").val().replaceAll(" ","")=="" || $("#knev").val().replaceAll(" ","")=="" || $("#oma").val().replaceAll(" ","")=="")
    {
        alert("Valamelyik mező üresen maradt")
        return 0;
    }
}


