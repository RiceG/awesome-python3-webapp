import orm
from models import User, Blog, Comment

async def test():
    await orm.create_pool({'user':'root', 'password':'root', 'database':'awesome'})

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

test()
