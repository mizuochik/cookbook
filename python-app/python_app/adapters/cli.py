from ast import parse
import asyncio
from argparse import ArgumentParser

parser = ArgumentParser()


async def _main():
    args = parser.parse_args()
    print("hello cli")


def main() -> None:
    asyncio.run(_main())
