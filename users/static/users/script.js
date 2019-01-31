$(document).ready(function(){
$("#menu-toggle").click(function(e) {
// e.preventDefault();
console.log(e);
$("#wrapper").toggleClass("active");
/* alert(1);*/
});
});

$(document).ready(function(){
var timeKeeper;

$('#menu').click(function(event)
{
event.stopPropagation();
$('#abcd').show();
});

$('#menu ul').click(function(event)
{
event.stopPropagation();
clearTimeout(timeKeeper);
});

$('#menu').focusout(function()
{
timeKeeper = setTimeout(function() {$('#menu ul').hide()}, 150);
});

$('#menu').attr('tabIndex', -1);


$('#note-button-1').click(function(event){
//alert("in1");
event.stopPropagation();
if($('#note-button-1-actions').css('display') === 'none'){
$('#note-button-1-actions').css("display","block");
}else{
$('#note-button-1-actions').css("display","none");
}
});
// $('#menu ul').hide();
});