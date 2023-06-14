// DOM ELEMENT REFERENCES
const hobbiesResult = document.getElementById('hobbies-result');
const transportResult = document.getElementById('transport-result');
const musicResult = document.getElementById('music-result');

const radioButtons = document.getElementsByName('transport-method');
const musicDropdown = document.getElementById('music-preference');

/*
    Default Value
*/
musicResult.textContent = musicDropdown.value;

/*
    Checkbox Listeners
 */
document.getElementById('sports-checkbox').addEventListener('change', ($event) => {
    if ($event.target.checked) {
        hobbiesResult.children[0].classList.remove('text-secondary');
    }
    else {
        hobbiesResult.children[0].classList.add('text-secondary');
}
});

document.getElementById('games-checkbox').addEventListener('change', ($event) => {
    if ($event.target.checked) {
        hobbiesResult.children[1].classList.remove('text-secondary');
    }
    else {
        hobbiesResult.children[1].classList.add('text-secondary');
    }
});

document.getElementById('music-checkbox').addEventListener('change', ($event) => {
    if ($event.target.checked) {
        hobbiesResult.children[2].classList.remove('text-secondary');
    }
    else {
        hobbiesResult.children[2].classList.add('text-secondary');
    }
});

/*
    Radio Listeners
*/
for (let i=0; i < radioButtons.length; i++) {
    radioButtons[i].addEventListener('change', ($event) => {
        transportResult.textContent = $event.target.value;
    })
}

/* 
    Dropdown Listeners
*/
musicDropdown.addEventListener('change', ($event) => {
    musicResult.textContent = $event.target.value;
})
