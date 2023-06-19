import asyncio

async def foo():
    print("Foo started")
    await asyncio.sleep(2)
    print("Foo completed")

async def bar():
    print("Bar started")
    await asyncio.sleep(1)
    print("Bar completed")

async def main():
    print("Main started")
    await asyncio.gather(foo(), bar())
    print("Main completed")

asyncio.run(main())