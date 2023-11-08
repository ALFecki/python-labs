const partners = document.querySelectorAll('.partner');

function handleScroll() {
    const windowHeight = window.innerHeight;
    const windowCenter = windowHeight / 2;

    partners.forEach((partner) => {
        const partnerRect = partner.getBoundingClientRect();
        const partnerTop = partnerRect.top;

        if (partnerTop <= windowCenter) {
            partner.classList.add('animated');
        } else {
            partner.classList.remove('animated');
        }
    });
}


window.addEventListener('scroll', handleScroll);

handleScroll();
