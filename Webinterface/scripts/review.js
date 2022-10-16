class Review {
    _id = null;
    _review = null;
    _reviews = false
    _oldReviews = null;
    _tags = [];
    _review_count = 0;

    constructor(id) {
        this._id = id;
        this._review = $('<div class="reviews"></div>');
        $('main').append(this._review);
    }

    newReviewField(ratings) {
        let html = '<div class="reviewHeader">Write a review</div><div class="newReview"><div class="newReviewContent"><div class="newReviewTexts"><textarea class="newReviewTextArea" placeholder="Write your review here"></textarea><div class="newReviewPosVNegs"><textarea onchange="formatText(this, \'+\')" class="newReviewPos" placeholder="Positives"></textarea><textarea onchange="formatText(this, \'-\')" class="newReviewNeg" placeholder="Negatives"></textarea></div></div><div class="newReviewRatings">';
        for (let i = 0; i < ratings.length; i++) {
            html += '<div class="newReviewRating"><div class="newReviewRatingHeader">' + ratings[i]['name'] + '</div><div class="newReviewRatingStars"><input type="range" min="0" max="10" value="5" onmousedown="starMove(this)"><div class="newReviewStars">';
            html += getStars(0);
            html += '</div></div></div>';
        }
        html += '</div></div><div class="newReviewButtons"><div class="newTags"></div><select class="newTagSelect" onchange="selectTag(this)"><option disabled selected>Add Course Tag</option>';
        for (let i = 0; i < this._tags.length; i++) {
            html += '<option data-color="' + this._tags[i]['color'] + '" value="' + this._tags[i]['id'] + '">' + this._tags[i]['name'] + '</option>';
        }
        html += '</select><button onclick="postReview()">Post</button></div></div>';

        this._review.append(html);

        $('.newReviewPos').on('keydown', function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                let end = this.value.length;
                this.setSelectionRange(end, end);
                this.focus();
                formatText(this, '+');
            }
        });
        $('.newReviewNeg').on('keydown', function (e) {
            if (e.keyCode === 13) {
                e.preventDefault();
                let end = this.value.length;
                this.setSelectionRange(end, end);
                this.focus();
                formatText(this, '-');
            }
        });
        armPosNNeg();

        $('.newTags').on('click', '.courseTag' , function (e) {
            let tag = $(this);
            $('select.newTagSelect').append('<option data-color="' + tag.data('color') + '" value="' + tag.data('id') + '">' + tag.html() + '</option>');
            tag.remove();
        });

        return this;
    }

    oldReviews() {
        if (!this._reviews) {
            this._oldReviews = $('<div class="oldReviews"><div class="reviewHeader">Reviews</div></div>');
            this._review.parent().append(this._oldReviews);
            this._reviews = true;
        }

        return this;
    }

    addOldReview(username, date, rating, text, pos, neg, id) {
        if (!this._reviews) {
            this.oldReviews();
        }

        let html = '';

        html += '<div class="review" id="' + id + '"><div class="reviewContent"><div class="reviewTexts">'
        html += '<div class="reviewTextArea">' + text + '</div>';
        html += '<div class="reviewPosVNegs"><div class="reviewPos">';
        for (let i = 0; i < pos.length; i++) {
            html += '<div class="reviewItem"> + ' + pos[i] + '</div>';
        }
        html += '</div><div class="reviewNeg">';
        for (let i = 0; i < neg.length; i++) {
            html += '<div class="reviewItem"> - ' + neg[i] + '</div>';
        }
        html += '</div></div>';
        html += '</div><div class="reviewRatings">';
        if (rating !== undefined) {
            for (let i = 0; i < rating.length; i++) {
                html += '<div class="reviewRating"><div class="reviewRatingHeader">' + rating[i]['name'] + '</div><div class="reviewRatingStars">';
                html += getStars(rating[i]['rating']);
                html += '</div></div>';
            }
        }
        html += '</div></div>';
        html += '<div class="reviewInfo"><div class="reviewUsername">';
        html += username;
        html += '</div> - <div class="reviewDate">';
        let dateObj = new Date(date);
        html += '' + dateObj.getDate() + '.' + (dateObj.getMonth() + 1) + '.' + dateObj.getFullYear();
        html += '</div> <button class="reviewReport" onclick="report(this)">- Report</button></div>';

        this._oldReviews.append(html);
    }

    addOldReviews(reviews) {
        for (let i = 0; i < reviews.length; i++) {
            this.addOldReview(reviews[i]['author'], reviews[i]['date'], reviews[i]['ratings'], reviews[i]['text'], reviews[i]['pos'], reviews[i]['neg'], reviews[i]['id']);
        }
    }
}

function getStars (rating = 0) {
    let stars = '';
    for (let i = 0; i < Math.floor(rating / 2); i++) {
        stars += '<i class="fas fa-star"></i>';
    }
    if (rating % 2 === 1) {
        stars += '<i class="far fa-star-half-stroke"></i>';
    }
    for (let i = 0; i < Math.floor((10-rating) / 2); i++) {
        stars += '<i class="far fa-star"></i>';
    }
    return stars;
}

function starMove (element) {
    starChange(element);

    $(element).on('mousemove', function() {
        starChange(element);
    });

    $(element).on('mouseup', function() {
        $(element).off('mousemove');
        $(element).off('mouseup');
    });
}

function starChange (element) {
    let rating = $(element).val();
    let stars = getStars(rating);
    $(element).siblings('.newReviewStars').html(stars);
}

function formatText (textArea, split) {
    let text = $(textArea).val();
    let newText = '';
    let lines = text.split(new RegExp('\\n|\\' + split));
    for (let i = 0; i < lines.length; i++) {
        let line = lines[i].trim();
        if (line.length > 0) {
            newText += split + ' ' + line + '\n';
        }
    }
    newText += split + ' ';
    $(textArea).val(newText);
}

function selectTag (element) {
    let tag = $(element).find('option:selected');
    let tagName = tag.text();
    let tagId = tag.val();
    let tagColor = tag.attr('data-color');

    $('.newTags').append('<div class="courseTag" data-id="' + tagId + '" style="background-color: ' + tagColor + ';">' + tagName + '</div>');

    tag.remove();
    $(element).find('option:first').prop("selected", true)
}

function armPosNNeg () {
    $('.newReviewPos').on('click', function (e) {
        formatText(this, '+');
        $('.newReviewPos').off('click');
    });
    $('.newReviewNeg').on('click', function (e) {
        formatText(this, '-');
        $('.newReviewNeg').off('click');
    });
}

function postReview () {
    let textElement = $('.newReviewTextArea');
    let text = textElement.val();
    let posElement = $('.newReviewPos');
    let pos = [];
    let positives = posElement.val().split(new RegExp('\\n|\\+'));
    let negElement = $('.newReviewNeg');
    let neg = [];
    let negatives = negElement.val().split(new RegExp('\\n|\\-'));

    for (let i = 0; i < positives.length; i++) {
        let point = positives[i].trim();
        if (point.length > 0) {
            pos.push(point);
        }
    }
    for (let i = 0; i < negatives.length; i++) {
        let point = negatives[i].trim();
        if (point.length > 0) {
            neg.push(point);
        }
    }

    let ratingElements = $('.newReviewRating');
    let rating = [];
    for (let i = 0; i < ratingElements.length; i++) {
        let ratingElement = $(ratingElements[i]);
        let ratingName = ratingElement.find('.newReviewRatingHeader').text();
        let ratingValue = ratingElement.find('.newReviewRatingStars input').val();
        rating.push({
            name: ratingName,
            rating: ratingValue
        });
    }

    let tags = [];
    let tagElements = $('.newTags .courseTag');
    for (let i = 0; i < tagElements.length; i++) {
        let tagElement = $(tagElements[i]);
        tags.push(tagElement.data('id'));
    }

    let id = $('.courseHeader').attr('id');

    let data = {
        course_id: id,
        text: text,
        pos: pos,
        neg: neg,
        rating: rating,
        tags: tags
    };

    let cookie = getCookies()['id_token'];

    if (cookie === undefined || cookie === null || cookie === '') {
        alert('You must be logged in to post a review.');
        return;
    }

    $.ajax({
        url: '/api/courses/review',
        method: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        processData: false,
        headers: {
            'Authorization': cookie || ''
        },
        success: function(data) {
            // Clear Values
            textElement.val('');
            posElement.val('');
            negElement.val('');
            tagElements.each(function () {
                let tag = $(this);
                $('select.newTagSelect').append('<option data-color="' + tag.data('color') + '" value="' + tag.data('id') + '">' + tag.html() + '</option>');
                tag.remove();
            });
            ratingElements.each(function () {
                let rating = $(this);
                rating.find('.newReviewRatingStars input').val(0);
                rating.find('.newReviewRatingStars').html(getStars(0));
            });
        },
        error: function(data) {
            alert('\'Error [\' + xhr.status + \'] while running getting Tags:\n\n' + data.responseText);
        }
    });
}

function report (element) {
    let id = $('.courseHeader').attr('id');
    let review = $(element).closest('.review');
    let reviewId = review.attr('id');
    let cookie = getCookies()['id_token'];

    if (cookie === undefined || cookie === null || cookie === '') {
        alert('You must be logged in to report a report.');
        return;
    }

    $.ajax({
        url: '/api/courses/review/report',
        method: 'POST',
        data: {
            course_id: id,
            review_id: reviewId
        },
        headers: {
            'Authorization': cookie || ''
        },
        success: function(data) {
            alert('Course Reported');
            review.remove();
        },
        error: function(data) {
            alert('\'Error [\' + xhr.status + \'] while running getting Tags:\n\n' + data.responseText);
        }
    });
}
