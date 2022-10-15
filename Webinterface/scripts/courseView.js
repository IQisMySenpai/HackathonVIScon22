window.addEventListener('load', function() {
    let params = getParameters('search');
    let id = params['id'];

    /*$.ajax({
        url: '/api/getData/course',
        data: {
            'id': id
        },
        method: 'GET',
        success: function(data) {
            let course = new Course();

            course.setCourseName('Diskrete Mathematik')
            course.setCourseAddition('252-0025-01L');
            let desc = 'Inhalt: Mathematisches Denken und Beweise, Abstraktion. Mengen, Relationen (z.B. Aequivalenz- und Ordnungsrelationen), Funktionen, (Un-)abzählbarkeit, Zahlentheorie, Algebra (Gruppen, Ringe, Körper, Polynome, Unteralgebren, Morphismen), Logik (Aussagen- und Prädikatenlogik, Beweiskalküle).<br><br>Hauptziele der Vorlesung sind (1) die Einführung der wichtigsten Grundbegriffe der diskreten Mathematik, (2) das Verständnis der Rolle von Abstraktion und von Beweisen und (3) die Diskussion einiger Anwendungen, z.B. aus der Kryptographie, Codierungstheorie und Algorithmentheorie.';
            course.setCourseDescription(desc, 'ueli.jpeg', 'Ueli', 'Professor U. Maurer');

            course.addCourseTags([{'name': 'Informatik', 'color': 'dark sea green'}, {'name': 'Sem 1', 'color':'orchid'}, {'name': 'GlasKlar', 'color':'salmon'}, {'name': 'Exam', 'color':'lightgreen'}]);
            course.addCourseRatings([{'name': 'Difficulty', 'rating': 10}, {'name': 'Workload', 'rating': 7}, {'name': 'Jokes', 'rating': 5}]);

            let review = new Review(id);
        },
        error: function(data) {
            alert('\'Error [\' + xhr.status + \'] while running getting Tags:\n\n' + data.responseText);
        }
    });*/
});