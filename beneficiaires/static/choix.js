$(document).ready(function() {

    $("#Choix").on("change",function(){
        if($("#Choix").val() == 1){
            $(".formBene").css("display","none");
            $(".formProd").css("display","none");
            $(".formCate").css("display","none");
            $("form").attr("action","addBenef/");
        }
        if($("#Choix").val() == 2){
            $(".formBene").css("display","none");
            $(".formProd").css("display","none");
            $(".formCate").css("display","none");
            $("form").attr("action","addProd/");
        }
        if($("#Choix").val() == 3){
            $(".formBene").css("display","none");
            $(".formProd").css("display","none");
            $(".formCate").css("display","none");
            $("form").attr("action","addCategorie/");
        }
        if($("#Choix").val() == 4){
            $(".formBene").css("display","block");
            $(".formProd").css("display","none");
            $(".formCate").css("display","none");
            $("form").attr("action","upBenef/");
        }
        if($("#Choix").val() == 5){
            $(".formBene").css("display","none");
            $(".formProd").css("display","block");
            $(".formCate").css("display","none");
            $("form").attr("action","upProd/");
        }
        if($("#Choix").val() == 6){
            $(".formBene").css("display","none");
            $(".formProd").css("display","none");
            $(".formCate").css("display","block");
            $("form").attr("action","upCategorie/");
        }
    })
});

