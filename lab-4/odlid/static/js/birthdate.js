var birthDate = localStorage.getItem("birthDate");

function isValidDate(dateString) {
    var regEx = /^\d{2}\.\d{2}\.\d{4}$/;
    if (!dateString.match(regEx)) return false;
    var parts = dateString.split(".");
    var day = parseInt(parts[0]);
    var month = parseInt(parts[1]);
    var year = parseInt(parts[2]);
    if (month < 1 || month > 12) return false;  // Неправильный месяц
    if (day < 1 || day > 31) return false;  // Неправильный день
    if (year < 1900 || year > new Date().getFullYear()) return false;  // Неправильный год
    return true;
}


if (!birthDate) {
    do {
        birthDate = prompt("Введите дату рождения в формате ДД.ММ.ГГГГ:");
    } while (!isValidDate(birthDate));

    var parts = birthDate.split(".");
    var day = parseInt(parts[0]);
    var month = parseInt(parts[1]) - 1;
    var year = parseInt(parts[2]);

    var birthDay = new Date(year, month, day);

    var today = new Date();
    var age = today.getFullYear() - birthDay.getFullYear();
    if (
        today.getMonth() < birthDay.getMonth() ||
        (today.getMonth() === birthDay.getMonth() && today.getDate() < birthDay.getDate())
    ) {
        age--;
    }

    var daysOfWeek = [
        "воскресенье",
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота"
    ];
    var birthDayOfWeek = daysOfWeek[birthDay.getDay()];

    var isAdult = age >= 18;

    alert("День недели вашей даты рождения: " + birthDayOfWeek);
    if (isAdult) {
        alert("Вам " + age + " лет. Добро пожаловать на сайт!");
    } else {
        alert("Вам " + age + " лет. Для использования сайта необходимо разрешение родителей.");
    }
}