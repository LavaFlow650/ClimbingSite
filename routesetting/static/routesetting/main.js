async function edit_route(id) {
    home_url = document.location.origin
    window.location.href = home_url + "/create_route/" + id
}