//bookmark = document.getElementByClassName('bookmark');
//upvote = document.getElementByClassName('upvoteIcon');
/*
bookmark.addEventListener('click',function(){
	bookmark.src = "../../static/blog/images/bookmarkFilledIcon.png";
});

upvote.addEventListener('click',function(){
	upvote.src = "../../static/blog/images/upvoteFilledIcon.png";
});
*/
/*------------*/

var page = 1;
var empty_page = false;
var block_request = false;

/*
$(window).scroll(function(){
	if($(window).scrollTop() > margin && empty_page == false && block_request == false){
		block_request = true;
		page += 1;
		$.get('?page=' + page, function(data) {
			if(data == '') { 
				empty_page = true;
			}
			else {
				block_request = false;
				$('#image-list').append(data);
			}
		});
	}
});
*/

var i;
$(document).ready(function(){
	let blogs = $('#blogs').children();
	for(i = 0; i < blogs.length; i++){
		let blog = blogs.eq(i);
		let blogInteract = blog.children().eq(1);
		blogInteract.children().eq(0).attr('id','upvote'+i);
		blogInteract.children().eq(1).attr('id','bookmark'+i);
		blogInteract.children().eq(2).attr('id','discuss'+i);
	}
		
});





















