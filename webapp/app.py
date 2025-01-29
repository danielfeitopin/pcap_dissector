from flask import Flask, request, send_file, render_template
import os
from werkzeug.utils import secure_filename
from dissector import process_pcap
from dissector.fields import get_fields

from .config import UPLOAD_FOLDER, OUTPUT_FOLDER, ALLOWED_EXTENSIONS, DEBUG_MODE

app = Flask(__name__)

# Make directories if they do not exist
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config["UPLOAD_FOLDER"] = os.path.join(BASE_DIR, UPLOAD_FOLDER)
app.config["OUTPUT_FOLDER"] = os.path.join(BASE_DIR, OUTPUT_FOLDER)
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        
        if "file" not in request.files:
            return "❌ No se ha subido ningún archivo", 400
        
        file = request.files["file"]

        if file.filename == "":
            return "❌ No se ha seleccionado ningún archivo", 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pcap_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(pcap_path)

            # Generar nombre del CSV de salida
            csv_filename = filename.rsplit(".", 1)[0] + ".csv"
            csv_path = os.path.join(app.config["OUTPUT_FOLDER"], csv_filename)
            print(f"Exporting to: {csv_path}")

            # Procesar el PCAP
            process_pcap(pcap_path, get_fields(), csv_path)

            # Enviar el CSV como respuesta
            return send_file(csv_path, as_attachment=True)

    return render_template("index.html")

def run_web():
    """Función para iniciar el servidor Flask"""
    print("🚀 Servidor web en http://127.0.0.1:5000")
    app.run(debug=DEBUG_MODE)

if __name__ == "__main__":
    run_web()