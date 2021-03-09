function mutatas(){
    $(".buttonka").css("display", "none");
    $(".tag").css("display", "block");
    $(".grid").css("display", "grid");
    //valamiért nem megy a this..
    if ($("#A").html()=="sikeres") 
        $("#A").css("color","#2dc71b") 
    if ($("#B").html()=="sikeres")
        $("#B").css("color","#2dc71b")
    if ($("#C").html()=="sikeres") 
        $("#C").css("color","#2dc71b") 
    if ($("#D").html()=="sikeres")
        $("#D").css("color","#2dc71b")
    if ($("#E").html()=="sikeres")
        $("#E").css("color","#2dc71b")
     if ($("#F").html()=="sikeres")
        $("#F").css("color","#2dc71b")
    
        
}
function bejelentkezes(){
    // megnézzük hogy üres-e, ha igen akkor visszadobjuk
    if ($("#vnev").val().replaceAll(" ","")=="" || $("#knev").val().replaceAll(" ","")=="" || $("#oma").val().replaceAll(" ","")=="")
    {
        alert("Valamelyik mező üresen maradt")
        return 0;
    }
}


