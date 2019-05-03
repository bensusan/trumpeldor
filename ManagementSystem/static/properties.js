let ip = '192.168.1.18';
let is_connected = false;
let prev_m = 1;
let prev_icon=2;

function allowOnlyConnectedUsers() {
    if(is_connected == false)
        window.location.href = '/error_page';
}