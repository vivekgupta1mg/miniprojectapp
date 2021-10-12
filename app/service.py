
# from sanic import Sanic
# from .routes import blueprint_group
# from databases import Database
# from environs import Env
# from app.settings import Settings




# app = Sanic(__name__)
# app.blueprint(blueprint_group)





# def setup_database():
#     app.db = Database(app.config.DB_URL)

#     @app.listener('after_server_start')
#     async def connect_to_db(*args, **kwargs):
#         await app.db.connect()

#     @app.listener('after_server_stop')
#     async def disconnect_from_db(*args, **kwargs):
#         await app.db.disconnect()


# def init():
#     env = Env()
#     env.read_env()

#     app.config.from_object(Settings)
#     setup_database()

#     app.run(
#         host=app.config.HOST,
#         port=app.config.PORT,
#         debug=app.config.DEBUG,
#         auto_reload=app.config.DEBUG,
#     )




# if __name__ == "__main__":
#     app.run()


from torpedo import Host

from .listeners import listeners
from .routes import blueprint_group




if __name__ == "__main__":

    # register combined blueprint group here. these blueprints are defined in the routes directory and has to be
    # collected in init file otherwise route will end up with 404 error.
    Host._listeners = listeners
    Host._blueprint_group = blueprint_group

    Host.run()
