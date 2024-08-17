async function edit_route(id) {
    home_url = document.location.origin;
    window.location.href = home_url + "/edit_route/" + id;
}

function get_x_axis(max_grade, min_grade = 0) {
    var x_axis = []
    for (let i = min_grade; i <= max_grade; i++) {
        x_axis.push("V" + i)
    }
    return x_axis
}

async function display_dist() {
    const route_dist = JSON.parse(document.getElementById('route_dist').textContent);
    const color_lookup = JSON.parse(document.getElementById('color_lookup').textContent);
    console.log(route_dist)
    console.log(color_lookup)
    x_axis = get_x_axis(Object.values(route_dist)[0].length - 1)

    var color_data = []
    for (color in route_dist) {
        var color_trace = {
            x: x_axis,
            y: route_dist[color],
            type: 'bar',
            marker: {
                color: '#' + color_lookup[color]
            },
            hoverinfo: poop
        }
        color_data.push(color_trace)
    }
    var layout = {
        barmode: 'stack',
        showlegend: false,
        bargap: 0.05,
        //paper_bgcolor: "lightslategray",
        yaxis: {
            zeroline: false,
            gridwidth: 1,
            minor: {
                tickvals: [0, 1, 2, 3, 5]
            }
        },
    };

    Plotly.newPlot('toprope dist', color_data, layout, { staticPlot: false, responsive: false });
    Plotly.newPlot('boulder dist', color_data, layout, { staticPlot: true, responsive: false });
}

if (window.location.href.indexOf("view_routes") != -1) {
    display_dist()
}