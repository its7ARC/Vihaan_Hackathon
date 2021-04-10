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


upvote = document.getElementById('upvoteIcon');
bookmark = document.getElementById('bookmarkIcon');
discuss = document.getElementById('discuss');


upvote.addEventListener('click'){
	$("#upvoteIcon").attr(src,"{% static 'blog/images/upvoteFilledIcon.png' %}");
	/*
	$.ajax({
             type: "POST",
             url: "{% url 'blog:upvote' %}",
             data: {
             	'csrfmiddlewaretoken': '{{ csrf_token }}'
             },
             async = false,
             dataType: "json",
             success: function(response) {
                    if(response.status==true){
                      upvote.src =  "{% static 'blog/images/upvoteFilledIcon.png' %}";
                    }
                    else if(response.status==false){
                      upvote.src =  "{% static 'blog/images/upvoteIcon.png' %}";
                    }
              }

        });
    */

};




















