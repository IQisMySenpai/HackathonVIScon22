class CourseSearch {
    _courseView = null;
    constructor() {
        this._courseView = $('<div class="lectures"></div>');
        $('main').append(this._courseView);

        this._courseView.on('click', 'div.lecture', function () {
            let id = $(this).attr('id');
            console.log(id);
        });
    }

    addCourse(id, name, addition, description) {
        let html = '<div class="lecture" id="';
        html += id;
        html += '"><div class="lectureHeader">';
        html += name;
        html += '</div><div class="lectureAddition">';
        html += addition;
        html += '</div><div class="lectureDescription">';
        html += description;
        html += '</div></div>';
        this._courseView.append(html);
    }

    addCourses(courses) {
        for (let i = 0; i < courses.length; i++) {
            this.addCourse(courses[i]['id'], courses[i]['name'], courses[i]['addition'], courses[i]['description']);
        }
    }
}

window.addEventListener('load', function() {
    var courseSearch = new CourseSearch();

    courseSearch.addCourse('1', 'Diskrete Mathematik', '252-0025-01L', 'Inhalt: Mathematisches Denken und Beweise, Abstraktion. Mengen, Relationen (z.B. Aequivalenz- und Ordnungsrelationen), Funktionen, (Un-)abzählbarkeit, Zahlentheorie, Algebra (Gruppen, Ringe, Körper, Polynome, Unteralgebren, Morphismen), Logik (Aussagen- und Prädikatenlogik, Beweiskalküle).<br><br>Hauptziele der Vorlesung sind (1) die Einführung der wichtigsten Grundbegriffe der diskreten Mathematik, (2) das Verständnis der Rolle von Abstraktion und von Beweisen und (3) die Diskussion einiger Anwendungen, z.B. aus der Kryptographie, Codierungstheorie und Algorithmentheorie.');
});