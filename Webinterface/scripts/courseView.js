window.addEventListener('load', function() {
    var course = new Course();
    course.setCourseName('Test');
    course.setCourseAddition('This is a cool course');
    let desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.';
    course.setCourseDescription(desc, 'ueli.jpeg', 'Ueli', 'This is Ueli');

    course.addCourseTags([{'name': 'test', 'color':'red'}, {'name': 'test2', 'color':'blue'}]);
    course.addCourseRatings([{'name': 'Test', 'rating': 5}, {'name': 'Test2', 'rating': 3}]);

    var review = new Review();
    review.newReviewField([{'name': 'Test'}, {'name': 'Test2'}, {'name': 'Test3'}]);
    review.oldReviews();
    review.addOldReview('Ueli', '15.10.2022', [{'name': 'Test', 'rating': 5}, {'name': 'Test2', 'rating': 3}], 'This is a cool course', ['He likes Turtles', 'Cookies are good'], ['This Course is shit']);
});