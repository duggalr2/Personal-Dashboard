/**
 * Created by Rahul on 2017-05-04.
 */
function init() {
    x = getLocalStorage();
    if (x) {
        document.getElementById('bar').style.width = x + '%';
    }
}

function setLocalStorage(x) {
    localStorage.setItem('progress_width', x)
}

function getLocalStorage() {
    return localStorage.getItem('progress_width')
}

function add() {
    var x = getLocalStorage();
    var y = Number(x) + 20;
    if (Number(x) >= 100) {
        setLocalStorage(0);
        document.getElementById('bar').style.width = 0;
    }
    else {
        setLocalStorage(y);
        document.getElementById('bar').style.width = y.toString() + '%';
    }
}

function decrease() {
    var x = getLocalStorage();
    var y = Number(x) - 20;
    setLocalStorage(y);
    document.getElementById('bar').style.width = y.toString() + '%';
}

function reset() {
    setLocalStorage(0);
    document.getElementById('bar').style.width = 0;
}

function complete() {
    setLocalStorage(100);
    document.getElementById('bar').style.width = '100%';
}

init();
