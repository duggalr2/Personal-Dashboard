/**
 * Created by Rahul on 2017-04-24.
 */

// TODO: Create a Localstorage protytype which requires the keyname
    // TODO: Have GetLocalStorage/SetLocalStorage as methods...
    // TODO: Each item that uses local storage will then have a separate object so it won't intefere

var circle = new ProgressBar.Circle('#library-test', {
    color: '#333',
    // This has to be the same size as the maximum width to
    // prevent clipping
    width: 4,
    strokeWidth: 4,
    trailWidth: 1,
    easing: 'easeInOut',
    duration: 1400,
    // text: {
    //     value: '',
    //     autoStyleContainer: false
    // }
});

circle.text(25);

function setLocalStorage(x) {
    localStorage.setItem('circle_new', x)
}

function getLocalStorage() {
    return localStorage.getItem('circle_new')
}

function init() {

    var i = getLocalStorage();
    if (i) {
        circle.animate(i);
    }
    else {
        circle.animate(0.1);
        setLocalStorage(0.1);
    }
    // circle.setText(i);
    // document.getElementById('show_percentage').innerHTML = i
}

function circle_add(){
    var x = getLocalStorage();
    var y = Number(x) + 0.15;
    if (0.95 < x && x <= 1.0) {
        setLocalStorage(0.1);
        circle.animate(0.1);
    }
    else {
        setLocalStorage(y);
        circle.animate(y);
    }
    circle.setText(y);
    // document.getElementById('show_percentage').innerHTML = y
}

init();

