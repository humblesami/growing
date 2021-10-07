$(function(){
    $('#group_list_search_form').submit(function(e){
        e.preventDefault();
        let now_url = window.location + '';
        let nn = now_url;
        $(this).find('input').each(function(i, el){
            if(el.value){
                now_url = web_utils.add_param_to_url(now_url, el.name, el.value);
            }
        });
        console.log(nn, now_url);
        window.location = now_url;
    });
});