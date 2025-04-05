from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass
import socket

app = Flask(__name__)

@app.route("/htop")
def htop():
    # Full Name
    full_name = "Abhay Pratap Singh Jarial"

    # System Username
    username = getpass.getuser()

    # Server Time (IST)
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # `top` output
    try:
        top_output = subprocess.check_output(["top", "-n", "1", "-b"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    # Format HTML
    return f"""
    <pre>
    Name: {full_name}
    user: {username}
    Server Time (IST): {server_time}
    TOP output:

    {top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
