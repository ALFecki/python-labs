document.addEventListener('DOMContentLoaded', function () {
    const dateForm = document.getElementById('dateForm');
    const monthInput = document.getElementById('month');
    const dayInput = document.getElementById('day');
    const summerDatesList = document.getElementById('summerDates');
    const winterDatesList = document.getElementById('winterDates');
    const fileInput = document.getElementById('file');

    dateForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const month = monthInput.value.trim().toLowerCase();
        const day = parseInt(dayInput.value);

        if (isValidDate(month, day)) {
            const dateItem = document.createElement('li');
            dateItem.textContent = `${month} ${day}`;

            if (isSummerMonth(month)) {
                summerDatesList.appendChild(dateItem);
            } else if (isWinterMonts(month)) {
                winterDatesList.appendChild(dateItem);
            }

            monthInput.value = '';
            dayInput.value = '';
        } else {
            alert('Пожалуйста, введите корректную дату (месяц и число).');
        }
    });

    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (event) {
                const fileContent = event.target.result;
                const lines = fileContent.split('\n');

                lines.forEach((line) => {
                    const [month, day] = line.trim().split(' ');
                    if (isValidDate(month, day)) {
                        const dateItem = document.createElement('li');
                        dateItem.textContent = `${month} ${day}`;

                        if (isSummerMonth(month)) {
                            summerDatesList.appendChild(dateItem);
                        } else if (isWinterMonts(month)) {
                            winterDatesList.appendChild(dateItem);
                        }
                    }
                });

                fileInput.value = '';
            };

            reader.readAsText(file);
        }
    });

    function isValidDate(month, day) {
        const validMonths = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'];
        return validMonths.includes(month) && !isNaN(day) && day >= 1 && day <= 31;
    }

    function isSummerMonth(month) {
        // Проверка на летний месяц
        const summerMonths = ['июнь', 'июль', 'август'];
        return summerMonths.includes(month);
    }

    function isWinterMonts(month) {
        const winterMonts = ['декабрь', 'январь', 'февраль']
        return winterMonts.includes(month);
    }
});
