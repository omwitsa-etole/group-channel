function copy(id)
{
var copyTextarea = id;
copyTextarea.select(); 
document.execCommand("copy"); 
}
function showmenu(id)
{ 
	var menu = document.getElementById(id);    
	if (menu.style.display == "none"){ 
		menu.style.display = 'block'; 
	}else{   
		menu.style.display = 'none'; 
	} 
}