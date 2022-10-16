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
            let lecture = data['course'];
            let course = new Course();
            course.setCourseName(lecture[0]['title']);
            course.setCourseAddition(lecture[0]['readable_id']);
            let desc = lecture[0]['abstract'] + '<br><br>' + lecture[0]['objective'] + '<br><br>' + lecture[0]['content'];
            course.setCourseDescription(desc);

            course.addCourseTags([{'name': 'Informatik', 'color': 'dark sea green'}, {'name': 'Sem 1', 'color':'orchid'}, {'name': 'GlasKlar', 'color':'salmon'}, {'name': 'Exam', 'color':'lightgreen'}]);
            course.addCourseRatings([{'name': 'Difficulty', 'rating': 10}, {'name': 'Workload', 'rating': 7}, {'name': 'Jokes', 'rating': 5}]);

            let review = new Review(id);
        },
        error: function(data) {
            alert('\'Error [\' + xhr.status + \'] while running getting Tags:\n\n' + data.responseText);
        }
    });
});