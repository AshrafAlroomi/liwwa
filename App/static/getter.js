SKIP = 0


function create_rows(data) {
    var table = document.getElementById('Table1').getElementsByTagName('tbody')[0];
    for (var i = 0; i < data.length; i++) {
        var newRow = table.insertRow();

        var dep = data[i]["Department"]
        var name = data[i]["Full Name"]
        var birth = data[i]["Birthday"]
        var exp = data[i]["Experience"]

        row = `<tr>
                <th scope="row">${dep}</th>
                <td>${name}</td>
                <td>${birth}</td>
                <td>${exp}</td>
            </tr>`
        newRow.innerHTML = row

    }
}

function get_data() {
    const D = new FormData();

    request = new XMLHttpRequest();
    url = `/api/admin?skip=${SKIP}`
    request.open('GET', url, true);
    request.setRequestHeader("X-ADMIN", 1)
    request.onreadystatechange = function() {
        if (this.status == 200 && this.readyState == 4) {
            let d = JSON.parse(request.responseText);
            if (d['users'].length > 0) {
                SKIP += d['users'].length;
                create_rows(d['users'])
            } else {
                var button = document.getElementById('loadbutton')
                button.innerHTML = "No More Users"
                button.disabled = true
            }

        } else {
            var button = document.getElementById('loadbutton')
            button.innerHTML = "No Users"
            button.disabled = true
        }
    }
    request.send(D)

}

get_data()