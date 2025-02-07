//node build/public.js

function public() {
    // Obtener la fecha y hora actual
    var now = new Date();

    // Formatear la fecha en formato dd/mm/yyyy hh:mm
    var day = String(now.getDate()).padStart(2, '0');
    var month = String(now.getMonth() + 1).padStart(2, '0'); // Los meses van de 0 a 11
    var year = now.getFullYear();
    var hours = String(now.getHours()).padStart(2, '0');
    var minutes = String(now.getMinutes()).padStart(2, '0');

    var fechaHora = `${day}/${month}/${year} ${hours}:${minutes}`;

    // Ejecutamos la subida de fotos en git con el mensaje que incluye la fecha y hora
    var execProcess = require("./exec_process.js");
    execProcess.result(`git add . && git commit -m "public ${fechaHora}" && git push -u origin main`, function(err, response){
        if(!err){
            console.log(response);
        }else {
            console.log(err);
        }
    });
}

public();
