import aiohttp
import asyncio


async def ws_client():
    session = aiohttp.ClientSession()
    async with session.ws_connect('http://0.0.0.0:8080/msg') as ws:
        await promt(ws)
        async for msg in ws:
            print('Recive from server: ', msg.data)


async def promt(ws):
    msg = input('Type message: ')
    await ws.send_str(msg)

asyncio.get_event_loop().run_until_complete(ws_client())
