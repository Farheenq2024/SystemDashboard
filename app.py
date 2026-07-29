from flask import Flask, render_template
import psutil
import platform
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return render_template(
        "index.html",
        cpu=cpu,
        ram=ram,
        disk=disk,
        os=platform.system(),
        current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(debug=True)