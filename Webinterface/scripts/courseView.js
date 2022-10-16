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
            course.setCourseName(lecture[0]['title']);
            course.setCourseAddition(lecture[0]['readable_id']);
            let desc = lecture[0]['abstract'] + '<br><br>' + lecture[0]['objective'];
            if (lecture[0]['content'] !== null && lecture[0]['content'].length > 30) {
                desc += '<br><br>' + lecture[0]['content'];
            }
            course.setCourseDescription(desc);

            course.addCourseTags(lecture[0]['tags']);
            if (lecture[0]['ratings'] == null || lecture[0]['ratings'].length === 0 || lecture[0]['ratings'] === undefined) {
                course.addCourseRatings([{'name': 'Difficulty', 'rating': 0}, {'name': 'Workload', 'rating': 0}, {'name': 'Jokes', 'rating': 0}]);
            } else {
                course.addCourseRatings(lecture[0]['ratings']);
            }

            let review = new Review(id);
        },
        error: function(data) {
            alert('\'Error [\' + xhr.status + \'] while running getting Tags:\n\n' + data.responseText);
        }
    });
});