import os
from app.app import app, db

port = os.environ["PORT"]
app.run(debug=True , host="0.0.0.0", port = int(port))