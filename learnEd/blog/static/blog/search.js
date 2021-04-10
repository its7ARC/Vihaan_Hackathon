var skill = document.getElementById('skill');
var search = document.getElementById('search');
var names = ['Music...','Web Development...','Writing...','Data Science...','Surfing...','Algebra...','Dance...'];
var i = 0;
var myVar;
var myVar2;
var submitEle = document.getElementById('submit');

//Placeholder in searchBar
var normalState = function(){
	var k = 0;

	var setI = function(){
    	i = parseInt((Math.random()*7)-0.1);
    	k = 0;
	}
	myVar = setInterval(setI,6000);

	var setPlaceholder = function(){
		if(k > names[i].length){
			skill.placeholder = names[i]
		}
		else{
			skill.placeholder = names[i].slice(0,k);
		}
		k++;
	}
	myVar2 = setInterval(setPlaceholder,90);

}

document.addEventListener('DOMContentLoaded',normalState);	



//AJAX 
function performSearch(keyword) {
	let results
	$.ajax({
		url: "dynamicSearch/",
		data: {
			'keyword' : keyword
		},
		async:false,
		dataType:'json',
		success: function(data){
			results = data.topics;
		}

	});
	return results
};

//DropdownSearch
skill.addEventListener('keyup',function(e){
	text = $("#skill").val();
	if(text == ''){
		if(e.keyCode == 8 || e.which == 8){
			$('#search').removeClass('focusSearch');
		}
	}

	else{
		$('#search').addClass('focusSearch');
		let suggestions = document.getElementById("suggestions");
		suggestions.style.display = "block";	
		suggestions.style.width = '28rem';
		suggestions.innerText = "";
		
		let results = performSearch(skill.value);

		for(let i=0; i<results.length; i++){

			let div = document.createElement("div");
			div.innerText = results[i];
			suggestions.appendChild(div);
			div.addEventListener('click',function(e){
				skill.value = results[i];
			});
		}

	}	
	
});

/*
document.addEventListener('click',function(){
	$('#search').removeClass('focusSearch');
});
*/

//SubmitProcessing
submitEle.addEventListener('click',function(ev){
	ev.stopImmediatePropagation();
	let text = skill.value;
	text = text.trim();
	text = text.toLocaleLowerCase();
	skill.value = text;

	if(skill.value == '' || skill.value.length > 32){	//letMoreCharsIn
		ev.preventDefault();
	}
});




//searchIcon(NavBar)
var search_div = document.getElementById("search-div");

document.getElementById("search-icon").onclick = function (){
	//toggling visibility of search div
	if (search_div.style.display == "none") {
    	search_div.style.display = "flex";
  	} 
  	else {
    	search_div.style.display = "none";
  	}
};

document.onclick = function(e){
	$('#search').removeClass('focusSearch');
    if(e==null || e.target == null || (e.target.id !== "search-div" && e.target.parentNode.parentNode.id !== "search-div" && e.target.parentNode.parentNode.parentNode.id !== "search-div" && e.target.parentNode.parentNode.parentNode.parentNode.id !== "search-div" && e.target.id !== "s-i" && e.target.id !== "search-icon" && e.target.id !== "suggestions" && e.target.id !== "search-inp" && e.target.id !== "s-img" && e.target.parentNode.id !== "suggestions" && e.target.parentNode.id !== "search-div")){
        // console.log(e.target.id); 
        if(search_div.style.display == "flex"){
        	search_div.style.display = 'none';
        	//console.log(e.target.parentNode.parentNode);
        }
    }

};

var s = document.getElementById("search-inp");
s.addEventListener('keyup',function(e){

	//display relevant search results for blog

	let text = s.value;
	console.log(text);
	if(text == ''){
		console.log('null');
		if(e.keyCode == 8 || e.which == 8){
			$('#b3').removeClass('focusSearch1');
		}
	}

	else{
		$('#b3').addClass('focusSearch1');
		let suggestions1 = document.getElementById("suggestions1");
		suggestions1.style.display = "block";	
		suggestions1.style.width = '28rem';
		suggestions1.innerText = "";
		
		let results1 = performSearch(s.value);

		for(let i=0; i<results1.length; i++){

			let div = document.createElement("div");
			div.innerText = results1[i];
			suggestions1.appendChild(div);
			div.addEventListener('click',function(e){
				s.value = results1[i];
			});
		}

	}	

});
/*
s.onblur = function (e) {
	$('#b3').removeClass('focusSearch1');
	document.getElementById("suggestions1").style.display = "none";

}
*/
/*
s.onfocus = function (e) {
	
}

*/




