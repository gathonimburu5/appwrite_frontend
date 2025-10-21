from flask import Flask

def application_run():
    app = Flask(__name__)
    app.app_context().push()

    if app.config["DEBUG"] == "production":
        app.config.from_object("application.config.DevelopmentConfig")
    else:
        app.config.from_object("application.config.ProductionConfig")

    from application.controllers.dashboard_controller import dashboard_router
    app.register_blueprint(dashboard_router, url_prefix="/")

    from application.controllers.todo_controller import todo_router
    app.register_blueprint(todo_router, url_prefix="/todo")

    from application.controllers.auth_controller import auth_router
    app.register_blueprint(auth_router, url_prefix="/auth")

    return app