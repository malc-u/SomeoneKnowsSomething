/**
 * Function toggling sidebar
 */
$(document).ready(function () {
    $('#sidebar-toggle').on('click', function () {
        $('#sidebar_wrapper').toggleClass('no-sidebar-wrapper')
    });
});