
let ip = '192.168.1.7';


let prev_m = 1;
let prev_icon=2;
let is_connected = localStorage.getItem("is_connected");

  // if(history.replaceState)
  //     history.replaceState({}, "", "/");
// var stateObj = { edit_attraction: "bar" };
// history.replaceState(stateObj, "", "/");

  function allowOnlyConnectedUsers() {
    if(is_connected == "false")
        window.location.href = '/error_page';
}