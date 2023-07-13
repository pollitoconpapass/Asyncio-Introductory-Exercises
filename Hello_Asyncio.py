import asyncio #-> ONLY ONE THING CAN HAPPEN AT THE EXACT SAME TIME

async def main():
    print("Hello")
    task = asyncio.create_task(foo("Hey"))
    await task #-> wait for the task to finish executing and then...
    print("finished") #-> print finished

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
