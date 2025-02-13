import subprocess
from datetime import datetime

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def public():
    # Obtener la fecha y hora actual
    now = datetime.now()
    
    # Formatear la fecha en formato dd/mm/yyyy hh:mm
    fecha_hora = now.strftime('%d/%m/%Y %H:%M')
    
    # Ejecutar la subida de fotos en git con el mensaje que incluye la fecha y hora
    command = f'git add . && git commit -m "public {fecha_hora}" && git push -u origin main'
    response = execute_command(command)
    print(response)

if __name__ == "__main__":
    public()
