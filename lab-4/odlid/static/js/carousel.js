let intervalId;

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

document.querySelector('.carousel-control.prev').addEventListener('click', function () {
    carouselSlide('prev');
});

document.querySelector('.carousel-control.next').addEventListener('click', function () {
    carouselSlide('next');
});

if (document.getElementById('update-interval')) {
    document.getElementById('update-interval').addEventListener('click', function (e) {
        e.preventDefault();
        const newInterval = document.getElementById('interval').value * 1000;
        clearInterval(intervalId);
        intervalId = setInterval(function () {
            carouselSlide('next');
        }, newInterval);
    });
}

intervalId = setInterval(function () {
    carouselSlide('next');
}, 5000);


window.addEventListener('focus', function () {
    const newInterval = document.getElementById('interval').value;
    clearInterval(intervalId);
    intervalId = setInterval(function () {
        carouselSlide('next');
    }, newInterval);
});

window.addEventListener('blur', function () {
    clearInterval(intervalId);
});


document.addEventListener('DOMContentLoaded', function () {
    const gridItems = document.querySelectorAll('.grid-item');

    gridItems.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width;
            const y = (e.clientY - rect.top) / rect.height;
            const rotationX = 10 * (0.5 - y);
            const rotationY = 10 * (0.5 - x);
            item.querySelector('.item-content').style.transform = `rotateX(${rotationX}deg) rotateY(${rotationY}deg) scale(1.1)`;
        });

        item.addEventListener('mouseleave', () => {
            item.querySelector('.item-content').style.transform = 'rotateY(0deg) scale(1)';
        });
    });
});
