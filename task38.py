# todo: Реализовать две сопрограммы. Первая с заданной периодичность(раз в 2,3 сек) пишет в файл и выводит результат.
# другая делает запрос к БД на выборку  билета и отображает поочередно  название билета (раз в 2,3 сек)

# Bonus:
В качестве бонуса можно реализовать Telegtram - бота который в виде викторины задает
вопросы. Вопросы можно взять из тестовой системы. После вывода бот принимает вариант ответа.
В конце викторины выводит кол-во правильных и неправильных ответов и приз в случае успеха.
В качестве библиотеки можно взять  библиотеку telebot. Описание по разработки и примеры найти
в многочисленных статьях в Internet.

# todo: Реализовать две сопрограммы. Первая с заданной периодичность(раз в 2,3 сек) пишет в файл и выводит результат.
# другая делает запрос к БД на выборку  билета и отображает поочередно  название билета (раз в 2,3 сек)

import asyncio
import aiofiles
import aiopg


async def file_io():
    for i in list(range(5)):
        async with aiofiles.open("text.txt", mode='at', encoding="utf-8") as f:
            await f.write(str(i+1)+"_string"+"\n")
            print("*")
            # await asyncio.sleep(1)
        async with aiofiles.open("text.txt", mode='r', encoding="utf-8") as f:
            # await asyncio.sleep(2)
            print("***")
            async for line in f:
                print(line)
            await f.close()


async def out_ofdb():
    dsn = 'dbname=postgres user=postgres password=mercury1960 host=localhost'
    pool = await aiopg.create_pool(dsn)
    async with pool.acquire() as conn:
        # await asyncio.sleep(2)
        async with conn.cursor() as cur:
            await cur.execute("SELECT theme FROM test;")
            # await asyncio.sleep(1)
            lst = []
            async for row in cur:
                lst.append(row)
                print("**", lst)
    await conn.close()
    pool.close()


async def main():
    await asyncio.gather(file_io(), out_ofdb())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()



