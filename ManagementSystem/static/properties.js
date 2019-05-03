let ip = '192.168.1.18';
let prev_m = 1;
let prev_icon=2;
let is_connected = localStorage.getItem("is_connected");

function allowOnlyConnectedUsers() {
    if(is_connected == "false")
        window.location.href = '/error_page';
}