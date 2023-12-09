import asyncio
import json
import datetime
import aiohttp
import argparse
import re


class Client:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.url = 'http://' + self.host + ':' + str(self.port) + '/labs'
        self.session = None
        self.reg_for_post = r'\bpost\b:\s*http://localhost:8080/labs\s*{.*}\s*'
        self.reg_for_patch = r'\s*\bpatch\b:\s*http://\b\w*\b:\d{1,4}'

    async def run_session(self):
        self.session = aiohttp.ClientSession()
        try:
            while True:
                await self.input_to_req()
        except EOFError:
            await self.session.close()
            print("Сессия завершена успешно")
            exit(0)
        except Exception as e:
            print(e)
            await self.session.close()
            exit(-1)

    async def input_to_req(self):
        input_text = "Введите запрос: \n"
        req_string = input(input_text).removeprefix(input_text)
        if re.fullmatch(self.reg_for_post, req_string):
            params_string = re.findall(r'{.*}', req_string)[0]
            params_dict = json.loads(params_string)
            if 'name' not in params_string or 'date' not in params_string:
                print("Для отправки запроса обязательно нужно ввести параметры name и date")
                return
            if len(params_dict) > 2:
                print("Все параметры, кроме name и date, будут проигнорированы")
            async with self.session.post(self.url, params=params_dict) as resp:
                print(resp.url)
                print(await resp.text())
        elif re.fullmatch(self.reg_for_patch, req_string):
            pass
        else:
            print("Запрос введён некорректно")



print("Пожалуйста, введите запрос согласно шаблону: \n"
      "{тип запроса}: {URL-адрес сервера:порт} {параметры запроса в формате json} \n"
      "Пример: post: http://localhost:8080/labs {\'name\': \'nak\', \'date\': \'12.12.2021\'}\n"
      "Для завершения сессии нажмите CTRL+E")


asyncio.run(Client().run_session())

