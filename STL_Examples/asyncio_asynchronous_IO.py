# asyncio -- Asynchronous I/O belong to networking and interprocess Communication

# asyncio is used as a foundation for multiple Python asynchronous frameworks that
# provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

import asyncio

async def good_morning():
    print('Good...')
    await asyncio.sleep(3)
    print('... Morning!')

asyncio.run(good_morning())