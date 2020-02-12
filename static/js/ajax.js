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
            $('#like').on('click', function (element) {
                $.ajax({
                    url: `/post/like/${this.value}`,
                    type: 'POST',
                    dataType: 'json',
                    data: {'user_id': userid, 'post_id': this.value},
                    success: function () {
                        / TODO СДЕЛАТЬ НоРМАЛЬНО ЛАЙКИ
                    }
                })
            })
        }
    })
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
                                <small><button id="like" class="fa fa-thumbs-up" value="${post.pk}"></button>${post.likes} <button id="dislike" class="fa fa-thumbs-down"></button>${post.dislikes}</small>
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
                                <a class="mr-2" href="#">${data.author.name}</a>
                                <small class="text-muted">${date.getUTCDate()}/${date.getUTCMonth()}/${date.getFullYear()}</small>
                                <small><button id="like" class="fa fa-thumbs-up"></button>${data.likes} <button id="dislike" class="fa fa-thumbs-down"></button>${data.dislikes}</small>
                             </div>
                              <h2><a class="article-title" href="#">${data.title}</a></h2>
                              <p class="article-content">${data.content}</p>
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