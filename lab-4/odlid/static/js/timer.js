
function formatTime(seconds) {
    let hours = Math.floor(seconds / 3600);
    let minutes = Math.floor((seconds % 3600) / 60);
    let remainingSeconds = seconds % 60;

    hours = String(hours).padStart(2, '0');
    minutes = String(minutes).padStart(2, '0');
    remainingSeconds = String(remainingSeconds).padStart(2, '0');

    return `${hours}:${minutes}:${remainingSeconds}`;
}

function updateTimer() {
    const currentTime = Math.floor(Date.now() / 1000);
    const sessionStart = localStorage.getItem('sessionStart');
    const sessionDuration = 3600; // 3600 секунд = 1 час

    if (!sessionStart) {
        localStorage.setItem('sessionStart', currentTime);
    } else {
        const elapsedTime = currentTime - sessionStart;
        const remainingTime = Math.max(sessionDuration - elapsedTime, 0);
        document.getElementById('timer').textContent = formatTime(remainingTime);

        if (remainingTime <= 0) {
            alert('Сессия истекла!');
            clearInterval(timerInterval);
        }
    }
}

updateTimer();
const timerInterval = setInterval(updateTimer, 1000);

function clearLocalStorage() {
    localStorage.clear();
}