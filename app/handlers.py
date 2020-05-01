from aiohttp import web
from config.base import Config
import logging


async def tamtam_handler(r):
    try:
        body = await r.json()
        logging.info(body)
        user_id = body["message"]["sender"]["user_id"]
    except Exception as e:
        logging.error(str(e))
        return web.json_response({"error": str(e)}, status=500)
    session = r.app["aiohttp_session"]
    base_url, access_token = Config.base_url, Config.access_token
    data = {"text": f"Your user_id={user_id}"}
    resp = await session.post(f"{base_url}/messages?access_token={access_token}&user_id={user_id}", json=data)
    logging.debug(str(resp))
    return web.json_response({"status": "ok"})


async def healthcheck_handler(r):
    return web.json_response({"health": "green"})