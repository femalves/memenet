(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        {% comment %} document.body.appendChild(document.createElement('script')).src='https://2e977006.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999); {% endcomment %}
        document.body.appendChild(document.createElement('script')).src='https://memesbyfernanda.herokuapp.com'+Math.floor(Math.random()*99999999999999999999);
    }
})();