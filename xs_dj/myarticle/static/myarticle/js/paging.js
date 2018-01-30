$(function () {
    $('#per_page_num_get').change(function () {
        var per_page_display_num = $('#per_page_num_get').val();
        $.ajax({
            url:"/myarticle/page_cache/",
            type:"GET",
            data:{"data":per_page_display_num,"url_path":"/myarticle/index/"},
        });
    })
})


