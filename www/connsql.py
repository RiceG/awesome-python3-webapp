import orm,asyncio
from models import User, Blog, Comment

async def test_user(loop):
    await orm.create_pool(loop = loop, user = 'root', password = 'root', db = 'awesome')
    u = User(name='faner', email='591865888@qq.com', passwd='wangu2008', image='about:blank')
    await u.save()
    await orm.destory_pool()

async def insert_blog(loop):
    await orm.create_pool(loop = loop, user = 'root', password = 'root', db = 'awesome')
    b = Blog(name='faner', email='591865888@qq.com', passwd='wangu2008', image='about:blank')
    await b.save()
    await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(insert_blog(loop))
loop.close()