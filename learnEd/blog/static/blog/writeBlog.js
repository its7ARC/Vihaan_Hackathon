var topicEle = document.getElementById('topic');
var preRequisitesEle = document.getElementById('preRequisites');
var blogContentEle = document.getElementById('blogContent');

var errorMessageEle = document.getElementById('errorMessage');
var draftBlogEle = document.getElementById('draftBlog');
var submitBlogEle = document.getElementById('submitBlog');


var draftBoolEle = document.getElementById('draftBool');
var suggestions = document.getElementById("suggestions");

draftBlogEle.addEventListener('click',function(ev){
	draftBoolEle.value = 'True';
	let text = topicEle.value;
	text = text.trim();
	text = text.toLocaleLowerCase();
	topicEle.value = text;

	if(topicEle.value == ''){
		ev.preventDefault();
		errorMessageEle.style.display = 'block';
	}
});

submitBlogEle.addEventListener('click',function(ev){
	draftBoolEle.value = '';
	let text = topicEle.value;
	text = text.trim();
	text = text.toLocaleLowerCase();
	topicEle.value = text;

	if(topicEle.value == '' || preRequisitesEle.value == '' || blogContentEle.value==''){
		ev.preventDefault();
		errorMessageEle.style.display = 'block';
	}
});



//Topic dropdown

//AJAX 
function performSearch(keywords_string) {
	return ["Search 1", "Search 2", "Search 3", "Search 4", "Search 5","Search 6"];
}

//DropdownSearch
topicEle.addEventListener('keyup',function(e){

	text = topicEle.value
	if(text == ''){
		suggestions.style.display = "none";	
	}
	else{
		suggestions.style.display = "block";
		suggestions.innerText = "";

		let results = performSearch(topicEle.value);
		for(let i=0; i<6; i++){
			let div = document.createElement("div");
			div.innerText = results[i];
			suggestions.appendChild(div);
			div.addEventListener('click',function(e){
				suggestions.style.display = "None";
				topicEle.value = results[i];
			});
		}

	}	
	
});

topicEle.addEventListener('keydown',function(e){
	if(e.keyCode == 13 || e.which == 13){
		e.preventDefault();
	}
});

document.addEventListener('click',function(e){
	suggestions.style.display = "None";
});





//Custom Textarea

//
preRequisitesEle.addEventListener('keydown',function(e){
	//Custom Actions
	if(e.keyCode == 13 || e.which == 13){

		var position = 0;
		var cursorPos = this.selectionStart;
		var content = this.value.slice(0,cursorPos);
		var key = e.which || e.keyCode;

		for(let i = cursorPos - 1;content[i] != '\n' && i >= 0;i--){
			if(content[i] == '\t'){
				position++;
			}
		}

		e.preventDefault();
		insertString = '\n';
		for(let i = 0;i < (position); i++){
			insertString += '\t';
		}
		if(content[cursorPos - 1] == ':'){
			insertString += '\t';
		}
		this.value = this.value.substring(0,cursorPos) + insertString + this.value.substring(cursorPos,this.value.length);
		this.selectionStart = cursorPos + insertString.length;
		this.selectionEnd = cursorPos + insertString.length;
	}

	else if(e.keyCode == 9 || e.which == 9){

		var position = 0;
		var cursorPos = this.selectionStart;
		var content = this.value.slice(0,cursorPos);
		var key = e.which || e.keyCode;

		position = 0;
		position2 = 0;
		e.preventDefault();
		var j;
		for(j = cursorPos - 1;content[j] != ':' && j >= 0;j--){}
		for(let i = j;content[i] != '\n' && i >= 0; i--){
			if(content[i] == '\t'){
				position++;
			}
		}
		for(let i = cursorPos-1; content[i] != '\n' && i >=0; i--){
			if(content[i] == '\t'){
				position2 ++;
			}
		}
		var insertString = '';
		for(let i = 0;i < (position-position2+1); i++){
			insertString += '\t';
		}
		this.value = this.value.substring(0,cursorPos) + insertString + this.value.substring(cursorPos,this.value.length);
		this.selectionStart = cursorPos + insertString.length;
		this.selectionEnd = cursorPos + insertString.length;
	}
	
});
//

blogContentEle.addEventListener('keydown',function(e){
	if(e.keyCode == 13 || e.which == 13){

		var position = 0;
		var cursorPos = this.selectionStart;
		var content = this.value.slice(0,cursorPos);
		var key = e.which || e.keyCode;

		for(let i = cursorPos - 1;content[i] != '\n' && i >= 0;i--){
			if(content[i] == '\t'){
				position++;
			}
		}

		e.preventDefault();
		insertString = '\n';
		for(let i = 0;i < (position); i++){
			insertString += '\t';
		}
		if(content[cursorPos - 1] == ':'){
			insertString += '\t';
		}
		this.value = this.value.substring(0,cursorPos) + insertString + this.value.substring(cursorPos,this.value.length);
		this.selectionStart = cursorPos + insertString.length;
		this.selectionEnd = cursorPos + insertString.length;
	}

	else if(e.keyCode == 9 || e.which ==9){

		var position = 0;
		var cursorPos = this.selectionStart;
		var content = this.value.slice(0,cursorPos);
		var key = e.which || e.keyCode;

		position = 0;
		position2 = 0;
		e.preventDefault();
		var j;
		for(j = cursorPos - 1;content[j] != ':' && j >= 0;j--){}
		for(let i = j;content[i] != '\n' && i >= 0; i--){
			if(content[i] == '\t'){
				position++;
			}
		}
		for(let i = cursorPos-1; content[i] != '\n' && i >=0; i--){
			if(content[i] == '\t'){
				position2 ++;
			}
		}
		var insertString = '';
		for(let i = 0;i < (position-position2+1); i++){
			insertString += '\t';
		}
		this.value = this.value.substring(0,cursorPos) + insertString + this.value.substring(cursorPos,this.value.length);
		this.selectionStart = cursorPos + insertString.length;
		this.selectionEnd = cursorPos + insertString.length;
	}
});



document.addEventListener('DOMContentLoaded',function(){
	preRequisitesEle.placeholder = '';
	blogContentEle.placeholder = '';
	resourcesEle.placeholder = '';
	
});














