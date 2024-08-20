home_url = document.location.origin;

async function edit_route(id) {
    id = id.slice(1)
    window.location.href = home_url + "/edit_route/" + id;
}

async function delete_route(id) {
    id = id.slice(1)
    window.location.href = home_url + "/delete_route/" + id
}

function get_x_axis(max_grade, min_grade = 0) {
    var x_axis = []
    for (let i = min_grade; i <= max_grade; i++) {
        x_axis.push("V" + i)
    }
    return x_axis
}

function dispaly_grade(grade_int, type) {
    if (type == "T") {
        var pre = "5.";
    } else if (type == "B") {
        var pre = "V";
    } else {
        var pre = "invalid route type";
    }

    var mod = grade_int % 10
    if (mod < 5) {
        return pre + int(grade_int / 10).toString() + "+" * mod
    } else if (mod == 5) {
        return pre + "fuck you"
    } else {
        return pre + str(1 + math.floor(grade_int / 10)) + "-" * (10 - mod)
    }
}

async function display_dist(output_graph, route_list) {
    //console.log(route_list)
    const color_lookup = JSON.parse(document.getElementById('color_lookup').textContent);
    //console.log(color_lookup)
    // x_axis = get_x_axis(Object.values(route_dist)[0].length - 1)

    var routes = []
    for (route in route_list) {
        console.log(dispaly_grade(route[0], route[1]))
    }
    for (route in route_list) {
        var route_tick = {
            x: dispaly_grade(route[0], route[1]),
            y: [2],
            type: 'bar',
            marker: {
                color: '#' + color_lookup[route[1]]
            },
            hoverinfo: route[3]
        }
        routes.push(route_tick)
    }

    // var color_data = []
    // for (color in route_dist) {
    //     var color_trace = {
    //         x: x_axis,
    //         y: route_dist[color],
    //         type: 'bar',
    //         marker: {
    //             color: '#' + color_lookup[color]
    //         },
    //         hoverinfo: poop
    //     }
    //     color_data.push(color_trace)
    // }
    // var layout = {
    //     barmode: 'stack',
    //     showlegend: false,
    //     bargap: 0.05,
    //     //paper_bgcolor: "lightslategray",
    //     yaxis: {
    //         zeroline: false,
    //         gridwidth: 1,
    //         minor: {
    //             tickvals: [0, 1, 2, 3, 5]
    //         }
    //     },
    // };

    Plotly.newPlot('toprope dist', color_data, layout, { staticPlot: false, responsive: false });
    Plotly.newPlot('boulder dist', color_data, layout, { staticPlot: true, responsive: false });
}

if (window.location.href.indexOf("view_routes") != -1) {
    const b_list = JSON.parse(document.getElementById('b_list').textContent);
    const tr_list = JSON.parse(document.getElementById('tr_list').textContent);
    display_dist('boulder dist', b_list)
    display_dist('toprope dist', tr_list)
}

function set_route_type(type) {
    document.getElementById("id_type").value = type;
}