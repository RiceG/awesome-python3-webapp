import orm,asyncio
from models import User, Blog, Comment

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

async def test(loop):

    await orm.create_pool(loop = loop, user = 'root', password = 'root', db = 'awesome')
    u = User(name='fan', email='591865888@qq.com', passwd='wgiyq', image='about:blank')
    await u.save()
    await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()