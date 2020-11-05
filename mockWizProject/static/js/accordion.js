let selected = document.querySelectorAll('.panel');
let content = document.querySelectorAll('accordion-content');

function initAccordion(document){
   //when panel is clicked, handlePanelClick is called.          
function handlePanelClick(event){
  showPanel(event.currentTarget);
}
  function showPanel(panel){
    //Hide current one. First time it will be null. 
    //  var expandedPanel = document.querySelector(".active");
    //  console.log(expandedPanel);
    //  if (expandedPanel){
    //    console.log("yes");
    //      expandedPanel.classList.remove("active");
    //  }
     //Show new one
     panel.classList.toggle("active");
  }

  for (var i = 0, len = selected.length; i < len; i++){
    selected[i].addEventListener("click", handlePanelClick);
  }

// showPanel(selected[0])
}
initAccordion(document.getElementById("acc"));

