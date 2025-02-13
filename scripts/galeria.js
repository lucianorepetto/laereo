function fullScreenGallery(images, clickedSrc) {
    let currentIndex = images.indexOf(clickedSrc);
    
    let overlay = $('<div>', { class: 'sliderFullScreen-overlay' }).appendTo('body');
    let prevBtn = $('<div>', { class: 'sliderFullScreen-nav sliderFullScreen-prev', text: '<' }).appendTo(overlay);
    let carousel = $('<div>', { class: 'sliderFullScreen-carousel invisible-scroll' }).appendTo(overlay);
    
    images.forEach(src => {
        $('<img>', { class: 'sliderFullScreen-carousel-img' }).attr('src', src).appendTo(carousel);
    });
    
    let nextBtn = $('<div>', { class: 'sliderFullScreen-nav sliderFullScreen-next', text: '>' }).appendTo(overlay);
    let closeBtn = $('<div>', { class: 'sliderFullScreen-close', text: '×' }).appendTo(overlay);
    
    function updatePosition() {
        $('.sliderFullScreen-carousel-img').removeClass('active');
        $('.sliderFullScreen-carousel-img').eq(currentIndex).addClass('active');
        
        // Desplazamos el carrusel para hacer que la imagen activa esté centrada
        carousel.scrollLeft($('.sliderFullScreen-carousel-img').eq(currentIndex)[0].offsetLeft);
    }
    
    updatePosition();
    
    prevBtn.click(function () {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updatePosition();
    });
    
    nextBtn.click(function () {
        currentIndex = (currentIndex + 1) % images.length;
        updatePosition();
    });
    
    closeBtn.click(function () {
        overlay.remove();
    });
    
    overlay.click(function (e) {
        if ($(e.target).hasClass('sliderFullScreen-overlay')) {
            overlay.remove();
        }
    });
    
    // Manejo del desplazamiento con la rueda del mouse
    carousel.on('wheel', function (e) {
        if (e.originalEvent.deltaY > 0) {
            currentIndex = (currentIndex + 1) % images.length; // Next image
        } else {
            currentIndex = (currentIndex - 1 + images.length) % images.length; // Previous image
        }
        updatePosition();
        e.preventDefault(); // Prevenir el comportamiento por defecto del scroll
    });

    let resize = function() {
        if ($(window).width() < 768) {
            prevBtn.hide();
            nextBtn.hide();
            carousel.css('width', '100vw');
        } else {
            prevBtn.show();
            nextBtn.show();
            carousel.css('width', '');  // Aquí puedes definir el valor original si lo necesitas
        }
    }

    // Hide arrows on mobile
    $(window).resize(()=>{resize()});
    resize()
}
