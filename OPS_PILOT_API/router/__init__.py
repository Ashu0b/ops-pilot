from .event_router import event_router

def register_routers(app):
    app.register_blueprint(event_router, url_prefix="/")