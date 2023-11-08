var birthDate = localStorage.getItem("birthDate");

if (!birthDate) {
    var birthDate = prompt("Введите дату рождения в формате ДД.ММ.ГГГГ:");

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