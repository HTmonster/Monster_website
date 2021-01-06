
/*--------------------------------最上面 导航栏去边框----------------*/

window.onload=function (){
    $(".navbar").addClass('border-0');
    $(".form-inline").hide();
};
jQuery(window).bind('scroll', function() {
    var scroH = $(document).scrollTop(); //滚动高度
    /*出现导航栏与回到顶部*/
    if (scroH  > 20) {
        $(".navbar").removeClass('border-0');
        $(".form-inline").show();
    }else{
        $(".navbar").addClass('border-0');
        $(".form-inline").hide();
    }
});