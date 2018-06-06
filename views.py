from aiohttp import web
import aiohttp


async def handler(request):
    return web.Response(
        text='Hello'
    )


async def vs_heandler(request):
    vs = web.WebSocketResponse()
    await vs.prepare(request)
    async for msg in vs:
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == 'close':
                await vs.close()
            else:
                await vs.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('exeption')
    return vs