document.addEventListener('click', function (event) {
    var dropdown = document.getElementById("myDropdown");
    
    if (!event.target.matches('.dropbtn')) {
        if (dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
        }
    }
});

function toggleDropdown() {
    var dropdown = document.getElementById("myDropdown");
    dropdown.classList.toggle("show");
}

function performAction(action) {
    console.log('Acción seleccionada:', action);

    const repuestosURL = 'task/task.html';
    const ventiladoresURL = 'project/project.html';

    switch (action) {
        case 'ver_repuestos':
            window.location.href = repuestosURL;
            break;
        case 'ver_despiece':
            window.location.href = ventiladoresURL;
            break;
        default:
            console.error('Acción no reconocida:', action);
    }
}
