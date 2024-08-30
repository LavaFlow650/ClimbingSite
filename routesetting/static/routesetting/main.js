home_url = document.location.origin;

async function edit_route(id) {
    id = id.slice(1);
    window.location.href = home_url + "/routesetting" + "/edit_route/" + id;
}

async function delete_route(id) {
    id = id.slice(1);
    window.location.href = home_url + "/routesetting" + "/delete_route/" + id;
}

async function archive_route(id) {
    id = id.slice(1);
    window.location.href = home_url + "/routesetting" + "/archive_route/" + id;
}

//chat gpt generated
function dispaly_grade(grade, type = 0) {
    let pre;
    if (type === "T") {
        pre = "5.";
    } else if (type === "B") {
        pre = "V";
    } else {
        pre = "invalid route type";
    }

    const mod = grade % 10;
    if (mod < 5) {
        return pre + Math.floor(grade / 10) + "+".repeat(mod);
    } else if (mod === 5) {
        return pre + "fuck you";
    } else {
        return pre + (Math.floor(grade / 10) + 1) + "-".repeat(10 - mod);
    }
}

function display_dist(output_graph, route_list, type) {
    const color_lookup = JSON.parse(document.getElementById("color_lookup").textContent);
    let grades = [];
    let route_dist = [];
    for (route of route_list) {
        if (!grades.includes(route[0])) {
            grades.push(route[0]);
        }

        var route_tick = {
            x: [dispaly_grade(route[0], type)],
            y: [1],
            type: "bar",
            marker: {
                color: "#" + color_lookup[route[1]],
            },
            customdata: [route[2]],
            hovertemplate: "%{customdata}<extra></extra>",
        };
        route_dist.push(route_tick);
    }

    grades.sort(function (a, b) {
        return a - b;
    });
    let dis_grades = [];
    for (grade of grades) {
        dis_grades.push(dispaly_grade(grade, type));
    }

    var layout = {
        barmode: "stack",
        showlegend: false,
        bargap: 0.1,
        //paper_bgcolor: "lightslategray",
        yaxis: {
            zeroline: false,
            //gridwidth: 1,
            fixedrange: true,
            // tickformat: ",d",
            dtick: 1,
        },
        xaxis: {
            type: "category",
            categoryorder: "array",
            categoryarray: dis_grades,
            fixedrange: true,
        },
        margin: {
            l: 40,
            r: 40,
            b: 40,
            t: 20,
            pad: 4,
        },
    };

    Plotly.newPlot(output_graph, route_dist, layout, {
        displayModeBar: false,
        staticPlot: false,
        responsive: true,
    });
}

if (window.location.href.indexOf("view_routes") != -1) {
    const b_list = JSON.parse(document.getElementById("b_list").textContent);
    const tr_list = JSON.parse(document.getElementById("tr_list").textContent);
    display_dist("boulder dist", b_list, "B");
    display_dist("toprope dist", tr_list, "T");
}

function set_route_type(type) {
    document.getElementById("id_type").value = type;
    document.getElementById("route-form").style.display = "block";
}
