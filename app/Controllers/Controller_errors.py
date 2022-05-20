from app import app

@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada...', 404