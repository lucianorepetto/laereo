//node build/public.js

function public(){
    //ejecutamos la subida de fotos en git
    var execProcess = require("./exec_process.js");
    execProcess.result("git add . && git commit -m \"public src\" && git push -u origin main", function(err, response){
        if(!err){
            console.log(response);
        }else {
            console.log(err);
        }
    });
}

public();