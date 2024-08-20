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

//chat gpt generated
function dispaly_grade(grade, type) {
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

async function display_dist(output_graph, route_list) {
    console.log(route_list)
    const color_lookup = JSON.parse(document.getElementById('color_lookup').textContent);
    //console.log(color_lookup)
    // x_axis = get_x_axis(Object.values(route_dist)[0].length - 1)

    var route_dist = []
    for (route of route_list) {
        var route_tick = {
            x: dispaly_grade(route[0], route[1]),
            y: [1],
            type: 'bar',
            marker: {
                color: '#' + color_lookup[route[2]]
            },
            hoverinfo: route[3]
        }
        route_dist.push(route_tick)
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

    Plotly.newPlot(output_graph, color_data, layout, { staticPlot: false, responsive: false });
    // Plotly.newPlot('boulder dist', color_data, layout, { staticPlot: true, responsive: false });
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