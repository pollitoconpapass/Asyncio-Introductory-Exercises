import asyncio

async def fetch_data():
    print('start fetching') #-> begins here
    await asyncio.sleep(2) #-> sleeps 2 seconds and pass to the other function...
    print("done fetching") #-> when the 2 seconds are over it retakes here
    return {'data':1}

async def print_numbers():
    for i in range(10): #-> numbers 1-9
        print(i)
        await asyncio.sleep(0.25) #-> sleeps 0.25 to print each number

async def main(): 
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())
