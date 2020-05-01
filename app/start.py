from aiohttp import web, ClientSession
from config.base import Config
from app.handlers import healthcheck_handler, tamtam_handler
import logging
import argparse


async def on_shutdown(app):
    logging.debug("on_shutdown")
    await app["aiohttp_session"].close()


async def init_app():
    app = web.Application()
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
    parser = argparse.ArgumentParser(description="tamtam bot")
    parser.add_argument("--port")
    args = parser.parse_args()
    logging.basicConfig(level=Config.log_level)
    app = init_app()
    web.run_app(app, host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    main()

