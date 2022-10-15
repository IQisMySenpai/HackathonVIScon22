class Review {
    _review = null;
    _reviews = false
    _oldReviews = null;

    constructor(id) {
        this._review = $('<div class="reviews"></div>');
        $('main').append(this._review);
    }

    newReviewField(ratings) {
        let html = '<div class="reviewHeader">Write a review</div><div class="newReview"><div class="newReviewContent"><div class="newReviewTexts"><textarea class="newReviewTextArea" placeholder="Write your review here"></textarea><div class="newReviewPosVNegs"><textarea class="newReviewPos" placeholder="Positives"></textarea><textarea class="newReviewNeg" placeholder="Negatives"></textarea></div></div><div class="newReviewRatings">';
        for (let i = 0; i < ratings.length; i++) {
            html += '<div class="newReviewRating"><div class="newReviewRatingHeader">' + ratings[i]['name'] + '</div><div class="newReviewRatingStars"><input type="range" min="0" max="10" value="5" onmousedown="starMove(this)"><div class="newReviewStars">';
            html += getStars(0);
            html += '</div></div></div>';
        }
        html += '</div></div><div class="newReviewButtons"><button>Post</button></div></div>';

        this._review.append(html);

        return this;
    }

    oldReviews() {
        if (!this._reviews) {
            this._oldReviews = $('<div class="oldReviews"><div class="reviewHeader">Reviews</div></div>');
            this._review.append(this._oldReviews);
            this._reviews = true;
        }

        return this;
    }

    addOldReview(username, date, rating, text, pos, neg) {
        if (!this._reviews) {
            this.oldReviews();
        }

        let html = '<div class="review"><div class="reviewContent"><div class="reviewTexts">'
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
        for (let i = 0; i < rating.length; i++) {
            html += '<div class="reviewRating"><div class="reviewRatingHeader">' + rating[i]['name'] + '</div><div class="reviewRatingStars">';
            html += getStars(rating[i]['rating']);
            html += '</div></div>';
        }
        html += '</div></div>';
        html += '<div class="reviewInfo"><div class="reviewUsername">';
        html += username;
        html += '</div> - <div class="reviewDate">';
        html += date;
        html += '</div> <div class="reviewReport">- Report</div></div>';

        this._oldReviews.append(html);
    }

}

/*
* <div class="review">
                    <div class="reviewInfo">
                        <div class="reviewUsername">
                            IQisMySenpai
                        </div>
                        -
                        <div class="reviewDate">
                            15.10.2022
                        </div>
                        <div class="reviewReport">
                            - Report
                        </div>
                    </div>
                    <div class="reviewContent">
                        <div class="reviewTexts">
                            <div class="reviewTextArea">sfghfsdhjdsfh</div>
                            <div class="reviewPosVNegs">
                                <div class="reviewPos">dfsiuhgfaiugh</div>
                                <div class="reviewNeg">soijgdfoi;fjdg</div>
                            </div>

                        </div>
                        <div class="reviewRatings">
                            <div class="reviewRating">
                                <div class="reviewRatingHeader">
                                    Hardness
                                </div>
                                <div class="reviewRatingStars">
                                    <i class="fas fa-star"></i>
                                    <i class="far fa-star-half-stroke"></i>
                                    <i class="far fa-star"></i>
                                    <i class="far fa-star"></i>
                                    <i class="far fa-star"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
* */

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
    $(element).on('mousemove', function() {
        let rating = $(element).val();
        let stars = getStars(rating);
        $(element).siblings('.newReviewStars').html(stars);
    });

    $(element).on('mouseup', function() {
        $(element).off('mousemove');
        $(element).off('mouseup');
    });
}