// getElementById and tagname

function Func2(){
  var x = document.getElementsByTagName("div");
  // Access individual element
  x[0].style.fontFamily = "Courier New";
  x[1].style.fontSize = 20;
  x[1].style.color = "Blue";
  x[2].style.fontStyle = "Bold";
  x[3].style.textDecoration = "Line-through";
  x[2].style.textTransform = "uppercase";
  x[3].style.backgroundColor = "green";

  // Apply get elements by tag name to all
  for (var i = 0; i< x.length; i++){
    x[i].style.fontWeight = "Bolder";
    x[i].style.color = "red";
  }
}

// Apply getelements by class name
function Func1(){
  var y = document.getElementsByClassName("cls");
  // Access individual element
  y[0].style.fontFamily = "Courier New";
  y[1].style.color = "Blue";
  y[2].style.backgroundColor = "green";

  // Loop and Apply get elements by classname 
for (var i = 0; i < y.length; i++){
  y[i].style.backgroundColor = "green";
  y[i].style.fontSize = 40;
}
}
