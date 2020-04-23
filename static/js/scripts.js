/**
 * Function toggling sidebar
 */
$(document).ready(function () {
    $('#sidebar-toggle').on('click', function () {
        $('#sidebar_wrapper').toggleClass('no-sidebar-wrapper')
    });
});
/**
 * Navbar collapsing on click
 */
$('.navbar-nav>li>a').on('click', function(){
    $('.navbar-collapse').collapse('hide');
});