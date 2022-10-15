window.addEventListener('load', function() {
    var course = new Course();
    course.setCourseName('Diskrete Mathematik')
    course.setCourseAddition('252-0025-01L');
    let desc = 'Inhalt: Mathematisches Denken und Beweise, Abstraktion. Mengen, Relationen (z.B. Aequivalenz- und Ordnungsrelationen), Funktionen, (Un-)abzählbarkeit, Zahlentheorie, Algebra (Gruppen, Ringe, Körper, Polynome, Unteralgebren, Morphismen), Logik (Aussagen- und Prädikatenlogik, Beweiskalküle).<br><br>Hauptziele der Vorlesung sind (1) die Einführung der wichtigsten Grundbegriffe der diskreten Mathematik, (2) das Verständnis der Rolle von Abstraktion und von Beweisen und (3) die Diskussion einiger Anwendungen, z.B. aus der Kryptographie, Codierungstheorie und Algorithmentheorie.';
    course.setCourseDescription(desc, 'ueli.jpeg', 'Ueli', 'Professor U. Maurer');

    course.addCourseTags([{'name': 'Informatik', 'color': 'dark sea green'}, {'name': 'Sem 1', 'color':'orchid'}, {'name': 'GlasKlar', 'color':'salmon'}, {'name': 'Exam', 'color':'lightgreen'}]);
    course.addCourseRatings([{'name': 'Difficulty', 'rating': 10}, {'name': 'Work', 'rating': 7}, {'name': 'Jokes', 'rating': 5}]);

    var review = new Review();
    review.newReviewField([{'name': 'Difficulty', 'rating': 10}, {'name': 'Work', 'rating': 7}, {'name': 'Jokes', 'rating': 5}]);
    review.oldReviews();
    review.addOldReview('Jannick', '15.10.2022', [{'name': 'Difficulty', 'rating': 8}, {'name': 'Work', 'rating': 9}, {'name': 'Jokes', 'rating': 10}], 'Really Hard Work. Fun Professor with good jokes', ['Interesting Topics', 'Good Stories', 'Good Script'], ['Hard Work for 7KP', 'Homework is corrected strictly']);
    review.addOldReview('Zhao Na', '05.10.2022', [{'name': 'Difficulty', 'rating': 6}, {'name': 'Work', 'rating': 7}, {'name': 'Jokes', 'rating': 3}], 'Easy Peasy Lemon Squeezy', ['Ez 6 in my Exam'], ['No good Jokes']);
});