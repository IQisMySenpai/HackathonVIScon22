window.addEventListener('load', function() {
    $('.tags').on('click', '.tag', function() {
        let elem = $(this);

        if (!elem.hasClass('selectedTag')) {
            $(elem.clone()).appendTo('.searchTags');
            elem.addClass('selectedTag');
        } else {
            let tag = elem.attr('data-name');
            elem.removeClass('selectedTag');
            $('div.searchTags .tag[data-name="' + tag + '"]').remove();
        }§
    });

    $('.searchTags').on('click', '.tag', function() {
        let elem = $(this);

        let tag = elem.attr('data-name');
        $('div.tags .tag[data-name="' + tag + '"]').removeClass('selectedTag');
        elem.remove();
    });

    $.ajax({
        url: '/api/tags',
        method: 'GET',
        success: function(data) {
            createTags(JSON.parse(data)['tags']);
        },
        error: function(data) {
            alert('Error while running tags:\n\n' + data.responseText);
        }
    });
});

function createTags (tags) {
    for (let i = 0, len = tags.length; i < len; i++) {
        $('.tags').append('<div class="tag" data-name="' + tags[i]['name'] + '" style="background-color: ' + tags[i]['color'] + '">' + tags[i]['name'] + '</div>');
    }
}
