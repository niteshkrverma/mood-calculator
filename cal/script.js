const display = document.getElementById('display');
const moodDisplay = document.getElementById('moodDisplay');

const moods = [
    '😃', '🤩', '😎', '🤔', '😇', '🥳', '😱', '😅', '🤓', '😴',
    '😡', '🥶', '😜', '🤠', '😬', '😇', '🧐', '😲', '😏', '🤗',
    '🤑', '😤', '😳', '😌', '😈', '👻', '🤖', '👽', '🦄', '🐱‍👤'
];

function appendValue(val) {
    display.value += val;
}

function clearDisplay() {
    display.value = '';
    moodDisplay.textContent = '🤔';
}

function calculate() {
    try {
        display.value = eval(display.value);
        // Show a random mood/emoji after calculation
        const randomMood = moods[Math.floor(Math.random() * moods.length)];
        moodDisplay.textContent = randomMood;
    } catch {
        display.value = 'Error';
        moodDisplay.textContent = '😵';
    }
}
