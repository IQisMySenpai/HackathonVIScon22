class Review {
    _review = null;

    constructor(id) {
        this._review = $('<div class="reviews"></div>');
        $('main').append(this._review);
    }
}