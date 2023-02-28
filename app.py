import uuid
from flask import flask

instance_id = uuid.uuid4().hex
app = flask(__name__)

@app.route("/")
def get_instance_id():
    return f"instance ID: {instance_id}"

if __name__ == "__main__"
    app.run(port=5000, host="0.0.0.0")