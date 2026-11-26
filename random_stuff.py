from __future__ import annotations

import asyncio

async def asynclike_test() -> None:
    await asyncio.sleep(2)
    print("Hello World")

async def test_function() -> None:
    task = asyncio.create_task(asynclike_test, name="Test Task")
    if task.cancelled():
        print("Task is cancelled")
    else:
        print("Task is done.")

if __name__ == "__main__":
    asyncio.run(test_function)