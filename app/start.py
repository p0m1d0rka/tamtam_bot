from aiohttp import web, ClientSession
from app.handlers import healthcheck_handler, tamtam_handler
from app.logger import create_logger
from config.base import Config



async def on_shutdown(app):
    app["logger"].debug("on_shutdown begin")
    await app["aiohttp_session"].close()
    app["logger"].debug("on_shutdown end")


async def init_app():
    app = web.Application()
    app["logger"] = create_logger("app")
    app["logger"].debug("creatine app")
    app.add_routes([
        web.get("/healthcheck", healthcheck_handler),
        web.get("/tamtam_handler", tamtam_handler),
        web.post("/tamtam_handler", tamtam_handler)
    ])
    session = ClientSession()
    app["aiohttp_session"] = session
    app.on_shutdown.append(on_shutdown)
    return app


def main():
    app = init_app()
    web.run_app(app, host=Config.host, port=Config.port)


if __name__ == "__main__":
    main()

