$('.toggle').click(function(){
  // Switches the Icon
  $(this).children('i').toggleClass('fa-pencil');
  // Switches the forms  
  $('.form').animate({
    height: "toggle",
    'padding-top': 'toggle',
    'padding-bottom': 'toggle',
    opacity: "toggle"
  }, "slow");
});
function login(){
      document.getElementById("login").style.visibility = "visible";
      document.getElementById("login_main").style.visibility = "visible";
}
function start(){
    document.getElementById("login_main").style.visibility = "visible";
    document.getElementById("seoul").style.visibility = "visible"
    document.getElementById("do").style.visibility = "visible";
    document.getElementById("won").style.visibility = "visible";
    document.getElementById("book").style.visibility = "visible";
    document.getElementById("song").style.visibility = "visible";
    document.getElementById("sung").style.visibility = "visible";
    document.getElementById("gold").style.visibility = "visible";
    document.getElementById("jak").style.visibility = "visible";
    document.getElementById("cho").style.visibility = "visible";
    document.getElementById("nam").style.visibility = "visible";
    document.getElementById("kd").style.visibility = "visible";
    document.getElementById("ks").style.visibility = "visible";
    document.getElementById("aah").style.visibility = "visible";
    document.getElementById("po").style.visibility = "visible";
    document.getElementById("goo").style.visibility = "visible";
    document.getElementById("seo").style.visibility = "visible";
    document.getElementById("dong").style.visibility = "visible";
    document.getElementById("rang").style.visibility = "visible";
    document.getElementById("eun").style.visibility = "visible";
    document.getElementById("ro").style.visibility = "visible";
    document.getElementById("jin").style.visibility = "visible";
    document.getElementById("dragon").style.visibility = "visible";
    document.getElementById("yang").style.visibility = "visible";
    document.getElementById("ma").style.visibility = "visible";
    document.getElementById("joog").style.visibility = "visible";
    document.getElementById("seo").style.visibility = "visible";
    document.getElementById("dae").style.visibility = "visible";
}
