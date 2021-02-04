
/*---------------------------------------返回头部------------------------------*/
$('.top').on('click', function() {
            $('body,html').animate({ scrollTop: 0 }, 300);
});


/*---------------------------------------侧边目录------------------------------*/
// var viewW = $(window).width();
// if (viewW+17>=1200){
//         var right=viewW*0.5-540;
//         var Cright=right.toString()+'px';
//         $(".catalog").removeClass('hidden').css({"right":Cright})
// }
// else if (viewW+17<1200&viewW+17>992){
//         var right=viewW*0.5-440;
//         var Cright=right.toString()+'px';
//         $(".catalog").removeClass('hidden').css({"right":Cright})
// }


jQuery(window).bind('scroll', function() {
    var scroH = $(document).scrollTop(); //滚动高度
    /*出现导航栏与回到顶部*/
    if (scroH  > 700) {
        $(".catalog").removeClass('hidden')
        /*hidden时需要延时设置属性才有过度效果*/
        setTimeout('$(".catalog").css({"opacity":"1"})',10)
    } else {
        $(".catalog").addClass('hidden').css({"opacity":"0"})
    }
});

jQuery(window).resize(function() {//实时
    var viewW = $(window).width();
    if (viewW+17>=1200){
        var right=viewW*0.5-540;
        var Cright=right.toString()+'px';
        $(".catalog").removeClass('hidden').css({"right":Cright})
    }
    else if (viewW+17<1200&viewW+17>992){
        var right=viewW*0.5-440;
        var Cright=right.toString()+'px';
        $(".catalog").removeClass('hidden').css({"right":Cright})
    }
    if (viewW+17<992){
        $(".catalog").addClass('hidden')
    }
});