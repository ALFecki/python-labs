// Автоматическая смена элемента
setInterval(function () {
    carouselSlide('next');
}, 5000);

// Подключение обработчиков событий для кнопок
document.querySelector('.carousel-control.prev').addEventListener('click', function () {
    carouselSlide('prev');
});

document.querySelector('.carousel-control.next').addEventListener('click', function () {
    carouselSlide('next');
});

// Функция для сдвига карусели
function carouselSlide(direction) {
    const carouselItems = document.querySelector('.carousel-items');
    const itemWidth = document.querySelector('.carousel-item').offsetWidth;
    const currentPosition = carouselItems.style.transform ? parseFloat(carouselItems.style.transform.match(/-?\d+/)[0]) : 0;

    if (direction === 'prev') {
        carouselItems.style.transform = `translateX(${currentPosition + itemWidth}px)`;
    } else if (direction === 'next') {
        if (currentPosition === -(itemWidth * (carouselItems.childElementCount - 1))) {
            carouselItems.style.transform = `translateX(0)`;
            return;
        } 
        carouselItems.style.transform = `translateX(${currentPosition - itemWidth}px)`;
    }
}