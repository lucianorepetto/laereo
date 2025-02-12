$(document).ready(function() {
// Hacer una solicitud AJAX para obtener el archivo JSON
    $.ajax({
        url: './assets/banners/imagenes.json', // Ruta del archivo JSON generado por Python
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log(data);
            // Verificar si la propiedad 'imagenes' existe en el JSON
            if (data.imagenes && data.imagenes.length > 0) {
                // Recorrer la lista de imágenes y agregar cada una al div .galeria
                data.imagenes.forEach(function(imagen) {
                    var imgElement = $('<img>').attr('src', imagen).addClass('imagen-banner');
                    $('.galeria').append(imgElement);
                });
            } else {
                console.log('No se encontraron imágenes en el JSON.');
            }
        },
        error: function() {
            console.log('Error al cargar el archivo JSON.');
        }
    });
});