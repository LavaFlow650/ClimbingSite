function feedback_update() {
    console.log(route.value);
    if (route.value) {
        rating_bool.parentElement.style.display = "block";
        rating.style.display = "block";
        grade.style.display = "block";
    } else {
        rating_bool.parentElement.style.display = "none";
        rating.style.display = "none";
        grade.style.display = "none";
    }
}

function bool_update() {
    rating_bool.checked = false;
}

// listen to when user selcts a route
route = document.getElementById("id_route");
rating_bool = document.getElementById("id_rating_bool");
rating = document.getElementById("id_rating").parentElement;
grade = document.getElementById("id_grade_int").parentElement;
feedback_update();
route.onchange = feedback_update;
rating.onchange = bool_update;
