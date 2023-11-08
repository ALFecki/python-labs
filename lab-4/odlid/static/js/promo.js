document.addEventListener('DOMContentLoaded', function() {
    const promoForm = document.getElementById('promoForm');
    const inputPromo = document.getElementById('input_promo');
    const btnCheckPromo = document.getElementById('btnCheckPromo');

    btnCheckPromo.addEventListener('click', function() {
        const promoCode = inputPromo.value;

        fetch(`/account/check_promo/${promoCode}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.valid) {
                const discount = data.discount;
                const totalPriceElement = document.querySelector('.num');
                const currentTotalPrice = parseFloat(totalPriceElement.textContent);
                const discountedPrice = currentTotalPrice * (1 - discount / 100);
                totalPriceElement.textContent = discountedPrice.toFixed(2);

                alert(`Промокод применен. Скидка ${discount}%`);
            } else {
                alert('Промокод недействителен.');
            }
        })
        .catch(error => {
            console.error('Ошибка при проверке промокода:', error);
        });
    });
});
