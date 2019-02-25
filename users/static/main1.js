
////for toggle
//
   /* $(document).ready(function(){
 $("#menu-toggle").click(function() {
//        e.preventDefault();
//    console.log(e);
        $("#wrapper").toggleClass("active");

});

});
*/




$(document).ready(function(){
  $("#btn4").click(function(){
    $.get("http://127.0.0.1:8000/get_labels1/", function(data, status){
      r1=JSON.parse(data.message)
      //console.log('---------------')
      //console.log(r1[1].fields['label'])
      //console.log(r1[1].pk)
      //console.log('----------------')

      for(i=0;i<r1.length;i++){
var element = document.createElement("input");


   //Assign different attributes to the element.
   element.setAttribute("type", "text");
   element.setAttribute("value", r1[i].fields['label']);
   element.setAttribute("name", r1[i].fields['label']);
   element.setAttribute("id", "id"+r1[i].pk );
   element.setAttribute("onclick", "clic(this)" );

     var id="#"+"id"+r1[i].pk // important
     console.log(id)
    $("#labelForm").append(element)
        jQuery('#labelForm').append("<br>")

    <!--console.log("text" + i  )-->
  <!--var value=jQuery("#id112").val();-->
        <!--console.log(value)-->

  var value1=jQuery(id).val();
        console.log(value1)



        <!--$("#Label_").append(r1[i].fields['label']+"&nbsp&nbsp&nbsp&nbsp&nbsp"+ r1[i].pk + "<br>")-->
        <!--console.log(r1[i].fields['label'] + "  ")-->
            <!--id=r1[i].pk-->
            <!--name=r1[i].fields['label']-->
            <!--value=r1[i].fields['label']-->
            <!--input = jQuery('<input type="text" id="id"  value="value" >');-->
             <!--jQuery('#labelForm').append(input);-->
             <!--jQuery('#labelForm').append("<br>")-->
             <!--var bla = $('#id').val();-->
              <!--$('#id').val(r1[i].fields['label']);-->
        }



        <!--$("#labelinput").append(r1[0].fields['label'])-->
        <!--var bla = $('#labelinput').val();-->
        <!--alert(bla)-->
    <!--//Set-->
    <!--$('#labelinput').val(r1[0].fields['label']);-->
    <!--input = jQuery('<input name="myname" id="my1">');-->
    <!--input1 = jQuery('<input name="myname1" id="myinput" value="KKK" >');-->
    <!--jQuery('#labelForm').append(input);-->
    <!--jQuery('#labelForm').append(input1);-->
    <!--jQuery('#myinput').remove();-->
    <!--jQuery('#my1').remove();-->




<!--var element = document.createElement("input");-->
   <!--//Assign different attributes to the element.-->
   <!--element.setAttribute("type", "text");-->
   <!--element.setAttribute("value", r1[3].fields['label']);-->
   <!--element.setAttribute("name", r1[3].fields['label']);-->
   <!--element.setAttribute("id",r1[1].pk );-->


<!--var element1 = document.createElement("input");-->


   <!--//Assign different attributes to the element.-->
   <!--element1.setAttribute("type", "text");-->
   <!--element1.setAttribute("value", "Saurabh");-->
   <!--element1.setAttribute("name", "name1");-->
   <!--element1.setAttribute("id", "My2st");-->

<!--$("#labelForm").append(element)-->
  <!--jQuery('#My2st').append(element);-->
<!--$("#labelForm").append(element1)-->
  <!--jQuery('#My2st').append(element1);-->


  <!--var r = document.createElement('span');-->
<!--var y = document.createElement("INPUT");-->
<!--y.setAttribute("type", "text");-->
<!--y.setAttribute("placeholder", "Name");-->
<!--increment();-->
<!--y.setAttribute("Name", "textelement_" + i);-->
<!--r.appendChild(y);-->
<!--r.setAttribute("id", "id_" + i);-->
<!--document.getElementById("labelForm").appendChild(r);-->
    });
  });
});








var id="";
var name="";
var value="";
console.log(id+" "+"id")
function clic(element)
{
   console.log("Clicked on " + element);
   console.log("Clicked on " + element.id);
  console.log("Clicked on " + element.name);
   console.log("Clicked on " + element.value);

id=element.id;
name=element.name;
value=element.value;
console.log(id+" "+"id")
}


$(document).ready(function(){
  $("#btnCreate").click(function(){

 <!--var id="#"+id-->
   <!--var value1=jQuery(id).val();-->
   <!--console.log(value1,+"  value1")-->
    $.post("http://127.0.0.1:8000/create_label/",
    {
      name: name,
      id: id,
      value:value
    },
    function(data,status){
      console.log("Data: " + data + "\nStatus: " + status);
            console.log(data)
    });
  });
});






$(document).ready(function(){
  $("#btn10").click(function(){

 var id="#"+id
   var value1=jQuery(id).val();
   console.log(value1,+"  value1")
    $.post("http://127.0.0.1:8000/edit_label/",
    {
      name: name,
      id: id,
      value:value
    },
    function(data,status){
      console.log("Data: " + data + "\nStatus: " + status);
            console.log(data)
    });
  });
});



$(document).ready(function(){
  $("#btn11").click(function(){

 id="#"+id
   var value1=jQuery(id).val();
   alert(value1,+"  value1----->");


    $.post("http://127.0.0.1:8000/delete_label_from_db/",
    {
      name: name,

      value:value
    },
    function(data,status){
      console.log("Data: " + data + "\nStatus: " + status);
            console.log(data)

            jQuery(id).remove();

            <!--r1=JSON.parse(data.message)-->
    });



  });
});






$(document).ready(function(){
  $("#inputlg").click(function(){
    $("#hide_this").hide();
    $("#show").hide();
  });

  <!--actually i have not used this show function yet -->
  $("#show").click(function(){
    $("#hide_this").show();
    $("#show").hide();
});


$("#create_note").click(function(){

$("#hide_this").hide();
$("#show").show();

});


$("#profileImage").click(function(){

$("#profilePanel").show();

});

$("#closeProfileCard").click(function(){

$("#profilePanel").hide();

});

});






//this search code is not working here so i am putting in base only

//<!--Below jquery code i am using for search -->





//for take a note hide and show
//$(document).ready(function(){
//    var timeKeeper;
//
//    $('#menu').click(function(event)
//    {
//    event.stopPropagation();
//        $('#abcd').show();
//    });
//
//    $('#menu ul').click(function(event)
//    {
//    event.stopPropagation();
//        clearTimeout(timeKeeper);
//    });
//
//    $('#menu').focusout(function()
//    {
//        timeKeeper = setTimeout(function() {$('#menu ul').hide()}, 150);
//    });
//
//    $('#menu').attr('tabIndex', -1);
////    $('#menu ul').hide();
//


//$('#note-button-1').click(function(event){
//  //alert("in1");
////    event.stopPropagation();
////    if($('#note-button-1-actions').css('display') === 'none'){
////    $('#note-button-1-actions').css("display","block");
////    }else{
////    $('#note-button-1-actions').css("display","none");
////    }
////    });
//// $('#note-button-2').click(function(event){
////   //alert("in1");
////    event.stopPropagation();
////    if($('#note-button-2-actions').css('display') === 'none'){
////    $('#note-button-2-actions').css("display","block");    }else{
//    $('#note-button-2-actions').css("display","none");
//    }
//    });
//


// $('#note-button-3').click(function(event){
////alert("in1");
//event.stopPropagation();
//if($('#note-button-3-actions').css('display') === 'none'){
//$('#note-button-3-actions').css("display","block");
//}else{
//$('#note-button-3-actions').css("display","none");
//}
//});
//
//    $('#note-button-6').click(function(event){
//    //alert("in");
//    event.stopPropagation();
//    if($('#note-button-6-actions').css('display') === 'none'){
//        $('#note-button-6-actions').css("display","block");
//    }else{
//        $('#note-button-6-actions').css("display","none");
//    }
//
//    });
//
//
//
//
//});
//
////$(document).ready(function(){
//$('button').click(function(e) {
//    if ($(this).hasClass('grid')) {
//        $('#container ul').removeClass('list').addClass('grid');
//    }
//    else if($(this).hasClass('list')) {
//        $('#container ul').removeClass('grid').addClass('list');
//    }
//});
//});