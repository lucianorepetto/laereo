//node build/public.js
const execProcess = require("./exec_process.js");

function runCommand(command, callback) {
    execProcess.result(command, function (err, response) {
        if (err) {
            console.log(`Error ejecutando "${command}":`, err);
        } else {
            console.log(`Salida de "${command}":`, response);
        }
        callback(err);
    });
}

function public() {
    runCommand("git add index.html", (err) => {
        if (err) return;
        runCommand("git add .\\assets\\", (err) => {
            if (err) return;
            runCommand("git add .\\styles\\", (err) => {
                if (err) return;
                runCommand('git commit -m "public"', (err) => {
                    if (err) return;
                    runCommand("git push -u origin main", (err) => {
                        if (err) console.log("Error al hacer push:", err);
                    });
                });
            });
        });
    });
}

public();
