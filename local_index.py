import os
from app.app import app, db

# Para Heroku
port = os.environ["PORT"]
db.create_all()
#app.run(debug=True , host="0.0.0.0", port = int(port))
# Para local
app.run(debug=True , host="0.0.0.0")