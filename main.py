import asyncio
import logging

from tg_bot.bot import start_bot


logging.basicConfig(
    level=logging.INFO
)


print("==============================")
print(" POLYMARKET BOT V3 START ")
print("==============================")


async def main():

    app = start_bot()


    if not app:

        print(
            "Telegram failed"
        )

        return


    print(
        "Telegram online"
    )


    await app.initialize()

    await app.start()

    await app.updater.start_polling()


    print(
        "Bot running..."
    )


    while True:

        await asyncio.sleep(60)



if __name__ == "__main__":

    asyncio.run(main())
