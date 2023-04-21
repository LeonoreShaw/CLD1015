function setSetpoint() {
    var setpoint = document.getElementById("setpoint").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/set_setpoint");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("setpoint-value").innerHTML = setpoint;
        }
    };
    xhr.send("setpoint=" + setpoint);
}

function turnOn() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/turn_on");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("ld-status").innerHTML = "ON";
        }
    };
    xhr.send();
}

function turnOff() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/turn_off");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("ld-status").innerHTML = "OFF";
        }
    };
    xhr.send();
}