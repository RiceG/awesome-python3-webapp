import orm,asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop = loop, user = 'root', password = 'root', db = 'awesome')
    u = User(name='faner', email='591865888@qq.com', passwd='wangu2008', image='about:blank')
    await u.save()
    await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()