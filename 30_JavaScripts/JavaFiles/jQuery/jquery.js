function func2()
{
  // $(element name).action()
  $("#img1").fadeToggle(2000);
}

function func1()
{
  // $(element name).action()
  $("div").css('bacground-color','orange');
}

$("div").click(function(){
  $(this).css('background-color','red');
})