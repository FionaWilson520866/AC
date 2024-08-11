from aiohttp import web

BotzPW = web.RouteTableDef()

@BotzPW.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://t.me/Techshyam_auto_caption_bot")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(BotzPW)
    return web_app
