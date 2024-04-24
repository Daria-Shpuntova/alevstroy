$('.openmodal').click(function (e) {
         e.preventDefault();
         $('.modalwindow').addClass('opened');
    });
$('.closemodal').click(function (e) {
         e.preventDefault();
         $('.modalwindow').removeClass('opened');
    });


var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});


$(function(){
    $(".rem_list").click(function(){
        if ($(".rem").hasClass("show_rem")){
            $(".rem").removeClass("show_rem");
        } else {
            $(".rem").addClass("show_rem");
        };
    });
    $(".re_list").click(function(){
        if ($(".re").hasClass("show_re") && $(".remont").hasClass("show_re")){
            $(".re").removeClass("show_re");
            $(".remont").removeClass("show_re");
        } else {
            $(".re").addClass("show_re");
            $(".remont").addClass("show_re");
        };
    });
    $(".oth_list").click(function(){
        if ($(".oth").hasClass("show_oth")  && $(".other").hasClass("show_oth")){
            $(".oth").removeClass("show_oth");
            $(".other").removeClass("show_oth");
        } else {
            $(".oth").addClass("show_oth");
            $(".other").addClass("show_oth");
        };
    });
});



$(function(){
    $(".mob_menu").click(function(){
        if ($(".menu").hasClass("show_menu")){
            $(".menu").removeClass("show_menu");
            $(".menu2").removeClass("show_menu2");
        } else {
            $(".menu").addClass("show_menu");
            $(".menu2").addClass("show_menu2");
        }
    });
});