import asyncio
import logging

from config import TG_BOT_TOKEN


logging.basicConfig(
    level=logging.INFO
)


print("==============================")
print(" POLYMARKET BOT V3 START ")
print("==============================")


async def main():

    print(
        "Config loaded"
    )


    if TG_BOT_TOKEN:

        print(
            "Telegram token detected"
        )

    else:

        print(
            "TG_BOT_TOKEN missing"
        )


    print(
        "Scanner waiting..."
    )


    while True:

        await asyncio.sleep(60)



if __name__ == "__main__":

    asyncio.run(
        main()
    )
