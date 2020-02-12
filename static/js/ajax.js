$(document).ready(function () {
    $.ajax({
        url:'/post/list/',
        type:'GET',
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        dataType:'json',
        success: function (d) {
            data_lengh = d.length;
            updatedata(d);
            var timer =setInterval(function () {
                axios.get('/post/list/').then(function (data) {
                if(data.data.length !== data_lengh) {
                    if(data.data.length > data_lengh){
                        updatedata(data.data[data.data.length-1]);
                        data_lengh += 1;
                    }
                    else if(data.data.length < data_lengh)
                    {
                        updatedata(data.data);
                        data_lengh -= 1
                    }
                }
                })
                .catch(function(err){
                    console.log('err', err);
                    clearTimer('An error occurred', timer);
                });
            }, 30000);

            $('.likebutton').on('click', function (element) {
                if(userid === 'None'){
                    alert("You are not logged in");
                    return null;
                }
                var post_id = this.id.split('_')[0];
                $.ajax({
                    url: `/post/like/${post_id}/`,
                    type: 'POST',
                    dataType: 'json',
                    data: {'user_id': userid, 'post_id': post_id},
                    success: function (response) {
                        var likes = document.getElementById(`${post_id}_like`).textContent;
                        if(response.err.length !== 0){
                            alert(response.err);
                        }
                        else {
                            likes = parseInt(likes) + 1;
                            document.getElementById(`${post_id}_like`).textContent = likes;
                        }
                    }
                })
            });

            $('.dislikebutton').on('click', function (element) {
                if(userid === 'None'){
                    alert("You are not logged in");
                    return null;
                }
                var post_id = this.id.split('_')[0];
                $.ajax({
                    url: `/post/dislike/${post_id}/`,
                    type: 'POST',
                    dataType: 'json',
                    data: {'user_id': userid, 'post_id': post_id},
                    success: function (response) {
                        var dislikes = document.getElementById(`${post_id}_dislike`).textContent;
                        if(response.err.length !== 0){
                            alert(response.err);
                        }
                        else {
                            dislikes = parseInt(dislikes) + 1;
                            document.getElementById(`${post_id}_dislike`).textContent = dislikes;
                        }
                    }
                })
            });
            if(userid !== 'None') {

                $.ajax({
                    url: `/user/${userid}/liked_posts/`,
                    type: 'GET',
                    headers: {"X-CSRFToken": getCookie("csrftoken")},
                    dataType: 'json',
                    success: function (data) {
                        for (var i = 0; i < data.length; i++) {
                            document.getElementById(`${data[i]}_like`).style.backgroundColor = 'green';
                        }
                    }
                });

                $.ajax({
                    url: `/user/${userid}/disliked_posts/`,
                    type: 'GET',
                    headers: {"X-CSRFToken": getCookie("csrftoken")},
                    dataType: 'json',
                    success: function (data) {
                        for (var i = 0; i < data.length; i++) {
                            document.getElementById(`${data[i]}_dislike`).style.backgroundColor = 'red';
                        }
                    }
                });
            }
        }
    });
});

function clearTimer(message, timer) {
               clearInterval(timer);
               alert(message);
            }

function updatedata(data) {
    if(Array.isArray(data)){
        let posts = ``;
        $('#figure-div').html("");
        data.forEach(post => {
            var date = new Date(post.date_posted);
            var options = { day: 'numeric', year: 'numeric', month: 'numeric', weekday: 'short' };
            posts += `
                          <article class="media content-section">
                            <div class="media-body">
                              <div class="article-metadata">
                                <a class="mr-2" href="#">${post.author.name}</a>
                                <small class="text-muted">${date.toLocaleDateString("ru", options)}</small>
                                <small id="ratings">
                                    <button id="${post.pk}_like" class="fa fa-thumbs-up likebutton">${post.likes}</button>
                                    <button id="${post.pk}_dislike" class="fa fa-thumbs-down dislikebutton">${post.dislikes}</button>
                                </small>
                             </div>
                              <h2><a class="article-title" href="#">${post.title}</a></h2>
                              <p class="article-content">${post.content}</p>
                            </div>
                          </article>`;
        });
        $('#figure-div').append(posts);
    }
    else{
        let posts = ``;
        var date = new Date(data.date_posted);
            posts += `
                          <article class="media content-section">
                            <div class="media-body">
                              <div class="article-metadata">
                                <a class="mr-2" href="#">${post.author.name}</a>
                                <small class="text-muted">${date.toLocaleDateString("ru", options)}</small>
                                <small id="ratings">
                                    <button id="${post.pk}_like" class="fa fa-thumbs-up">${post.likes}</button>
                                    <button id="${post.pk}_dislike" class="fa fa-thumbs-down">${post.dislikes}</button>
                                </small>
                             </div>
                              <h2><a class="article-title" href="#">${post.title}</a></h2>
                              <p class="article-content">${post.content}</p>
                            </div>
                          </article>`;
        $('#figure-div').append(posts);
    }
}


function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }