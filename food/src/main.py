import asyncio

import app
from repository import setup_database


def main() -> None:
    asyncio.run(setup_database())
    app.run()


if __name__ == "__main__":
    main()
