class Review {
    _review = null;

    constructor(id) {
        this._review = $('<div class="reviews"></div>');
        $('main').append(this._review);
    }

    newReviewField(ratings) {
        let html = '<div class="reviewHeader">Write a review</div><div class="newReview"><div class="newReviewContent"><div class="newReviewTexts"><textarea class="newReviewTextArea" placeholder="Write your review here"></textarea><div class="newReviewPosVNegs"><textarea class="newReviewPos" placeholder="Positives"></textarea><textarea class="newReviewNeg" placeholder="Negatives"></textarea></div></div><div class="newReviewRatings">';
        for (let i = 0; i < ratings.length; i++) {
            html += '<div class="newReviewRating"><div class="newReviewRatingHeader">' + ratings[i]['name'] + '</div><div class="newReviewRatingStars"><input type="range" min="0" max="10" value="5">';
            for (let j = 0; j < 5; j++) {
                html += '<i class="far fa-star"></i>';
            }
            html += '</div></div>';
        }
        html += '</div></div></div>';

        this._review.append(html);


        return this;
    }


}