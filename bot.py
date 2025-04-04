import logging, asyncio
from loader import *

import handlers.users.start
import handlers.users.info
import handlers.users.registration
import handlers.admin.start_reg
import handlers.admin.start_game
import handlers.admin.end_reg
import handlers.users.cancel

async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())