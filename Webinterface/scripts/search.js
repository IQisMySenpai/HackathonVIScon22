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
        }
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
            createTags(data['tags']);
        },
        error: function(data) {
            alert('Error [' + xhr.status + '] while running getting Tags:\n\n' + data.responseText);
        }
    });

    $('.search').on('keyup', function(e) {
        if (e.keyCode === 13) {
            search();
        }
    });
});

function createTags (tags) {
    for (let i = 0, len = tags.length; i < len; i++) {
        $('.tags').append('<div class="tag" data-name="' + tags[i]['id'] + '" style="background-color: ' + tags[i]['color'] + '">' + tags[i]['name'] + '</div>');
    }
}

function search () {
    let tags = [];
    $('.searchTags .tag').each(function() {
        tags.push($(this).attr('data-name'));
    });

    let tagString = tags.toString();
    let query = $('.search').val()

    let url = '/search?query=' + query;
    if (tagString.length > 5) {
        url += '&tags=' + tagString;
    }

    window.location.href = url;
}
