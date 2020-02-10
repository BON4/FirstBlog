$(document).ready(function () {
    $.ajax({
        url:'/post/list/',
        type:'GET',
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        dataType:'json',
        success: function (data) {
            let posts = ``;
            data.forEach(post =>{
                posts +=`<article class="media content-section">
                          <div class="media-body">
                            <div class="article-metadata">
                              <a class="mr-2" href="#">${post.author.name}</a>
                              <small class="text-muted">${post.date_posted}</small>
                              <small><button id="like" class="fa fa-thumbs-up"></button>${post.likes } <button id="dislike" class="fa fa-thumbs-down"></button>${ post.dislikes }</small>
                            </div>
                            <h2><a class="article-title" href="#">${ post.title }</a></h2>
                            <p class="article-content">${ post.content }</p>
                          </div>
                        </article>`;
            });
            $('#figure-div').append(posts);
        }
    })
});

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