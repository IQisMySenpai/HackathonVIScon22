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
        if (courses.length === 0) {
            this._courseView.append('Seems like only you and me are wanting to take this course...');
        }
        for (let i = 0; i < courses.length; i++) {
            this.addCourse(courses[i]['id'], courses[i]['title'], courses[i]['readable_id'], courses[i]['abstract']);
        }
    }
}

window.addEventListener('load', function() {
    var courseSearch = new CourseSearch();

    let params = getParameters('search');

    let data = {
        query: params['query']
    };

    if (params['tags'] !== undefined) {
        data['tags'] = params['tags'];
    }

    $.ajax({
        url: '/api/query/courses',
        method: 'GET',
        data: data,
        success: function(data) {
            courseSearch.addCourses(data['courses']);
        },
        error: function(data, textStatus, xhr) {
            alert('Error [' + xhr.status + '] while running search:\n\n' + data.responseText);
        }
    });
});