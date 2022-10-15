class Course {
    _course = null;
    _tagsCreated = false;
    _ratingCreated = false;

    constructor(id) {
        this._course = $('<div class="course"></div>');
        $('main').append(this._course);
    }

    setCourseName(name) {
        this._course.append('<div class="courseHeader">' + name + '</div>');
        $('title').html(name);
        return this;
    }

    setCourseAddition(addition) {
        this._course.append('<div class="courseSubheader">' + addition + '</div>');
        return this;
    }

    setCourseDescription(description, img = null, imgAlt = null, imgTitle = null) {
        let html = '<div class="courseMainContent"><div class="courseSummary">' + description + '</div>';
        if (img != null) {
            html += '<div class="courseProfile"><img class="courseProfilePicture" alt="' + imgAlt + '" src="../test_images/' + img;
            html += '"><div class="courseProfileNote">' + imgTitle + '</div></div>';
        }
        html += '</div>';
        this._course.append(html);
        return this;
    }

    createCourseTags() {
        if (!this._tagsCreated) {
            this._tagsCreated = true;
            this._course.append('<div class="courseTags"></div>');
        }
        return this;
    }

    addCourseTag(tag, color) {
        if (!this._tagsCreated) {
            this.createCourseTags();
        }
        this._course.find('.courseTags').append('<div class="courseTag" data-name="' + tag + '" style="background-color: ' + color + ';">' + tag + '</div>');
        return this;
    }

    removeCourseTag(tag) {
        this._course.find('.courseTag[data-name="' + tag + '"]').remove();
        return this;
    }

    addCourseTags(tags) {
        if (!this._tagsCreated) {
            this.createCourseTags();
        }

        for (let i = 0; i < tags.length; i++) {
            this.addCourseTag(tags[i]['name'], tags[i]['color']);
        }
        return this;
    }

    removeCourseTags(tags) {
        for (let i = 0; i < tags.length; i++) {
            this.removeCourseTag(tags[i]);
        }
        return this;
    }

    createCourseRatings() {
        if (!this._ratingCreated) {
            this._ratingCreated = true;
            this._course.append('<div class="courseRatings"></div>');
        }
        return this;
    }

    addCourseRating(name, rating) {
        if (!this._ratingCreated) {
            this.createCourseRatings();
        }
        this._course.find('.courseRatings').append('<div class="courseRating" data-name="' + name + '"><div class="courseRatingName">' + name + ':</div>&emsp;' + rating + '/10</div>');
        return this;
    }

    removeCourseRating(name) {
        this._course.find('.courseRating[data-name="' + name + '"]').remove();
        return this;
    }

    addCourseRatings(ratings) {
        if (!this._ratingCreated) {
            this.createCourseRatings();
        }

        for (let i = 0; i < ratings.length; i++) {
            this.addCourseRating(ratings[i]['name'], ratings[i]['rating']);
        }
        return this;
    }

    removeCourseRatings(ratings) {
        for (let i = 0; i < ratings.length; i++) {
            this.removeCourseRating(ratings[i]['name']);
        }
        return this;
    }
}