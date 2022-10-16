window.addEventListener('load', function() {
    let params = getParameters('search');
    let id = params['id'];

    $.ajax({
        url: '/api/courses/',
        data: {
            'course_id': id
        },
        method: 'GET',
        success: function(data) {
            let lecture = data['courses'];
            let course = new Course();
            course.setCourseName(lecture[0]['title'], id);
            course.setCourseAddition(lecture[0]['readable_id']);
            let desc = lecture[0]['abstract'] + '<br><br>' + lecture[0]['objective'];
            if (lecture[0]['content'] !== null && lecture[0]['content'].length > 30) {
                desc += '<br><br>' + lecture[0]['content'];
            }
            course.setCourseDescription(desc);

            course.addCourseTags(lecture[0]['tags']);
            let ratings = lecture[0]['reviews'][0]['ratings'];

            if (ratings == null || ratings.length === 0) {
                ratings = [{'name': 'Difficulty', 'rating': 0}, {'name': 'Workload', 'rating': 0}, {'name': 'Jokes', 'rating': 0}];
            }

            course.addCourseRatings(ratings);

            let review = new Review(id);

            $.ajax({
                url: '/api/tags',
                method: 'GET',
                success: function(stuff) {
                    review._tags = stuff['tags'];
                    review.newReviewField(ratings);

                    review.oldReviews();
                    review.addOldReviews(reviews);
                },
                error: function(data) {
                    alert('\'Error [\' + xhr.status + \'] while running getting Tags:\n\n' + data.responseText);
                }
            });


        },
        error: function(data) {
            alert('\'Error [\' + xhr.status + \'] while running course load:\n\n' + data.responseText);
        }
    });
});
