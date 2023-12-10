import asyncio
import json
import aiohttp
import re
import csv


class Client:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.url = 'http://' + self.host + ':' + str(self.port) + '/labs'
        self.session = None
        self.reg_for_post = r'\bpost\b:\s*http://localhost:8080/labs\s*{.*}\s*'
        self.reg_for_patch = r'\bpatch\b:\s*http://localhost:8080/labs/\b\w+\b\s*{.*}\s*'
        self.reg_for_get_all = r'\bget\b:\s*http://localhost:8080/labs\s*'
        self.reg_for_get_lab = r'\bget\b:\s*http://localhost:8080/labs/\b\w+\b'
        self.reg_for_delete_lab = r'\bdelete\b:\s*http://localhost:8080/labs/\b\w+\b'
        self.sub_reg_for_params = r'{.*}'
        self.sub_reg_for_url = r'http://localhost:8080/labs/\b\w+\b'

        self.file_name = 'labs_info.csv'
        self.fieldnames = [' ']

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
            print("Создание лабораторной работы")
            params_string = re.findall(self.sub_reg_for_params, req_string)[0]
            params_dict = json.loads(params_string)
            async with self.session.post(self.url, params=params_dict) as resp:
                await self.process_resp(resp.status, resp)

        elif re.fullmatch(self.reg_for_patch, req_string):
            print("Изменение лабораторной работы")
            params_url = re.findall(self.sub_reg_for_url, req_string)[0]
            params_string = re.findall(self.sub_reg_for_params, req_string)[0]
            params_dict = json.loads(params_string)
            async with self.session.patch(params_url, params=params_dict) as resp:
                await self.process_resp(resp.status, resp)

        elif re.match(self.reg_for_get_lab, req_string):
            print("Получение данных о лабораторной работе")
            params_url = re.findall(self.sub_reg_for_url, req_string)[0]
            async with self.session.get(params_url) as resp:
                await self.process_resp(resp.status, resp, flag_write_in_file=True)

        elif re.match(self.reg_for_get_all, req_string):
            print("Получение данных о всех лабораторных работах")
            async with self.session.get(self.url) as resp:
                await self.process_resp(resp.status, resp, flag_write_in_file=True)

        elif re.match(self.reg_for_delete_lab, req_string):
            print("Удаление лабораторной работы")
            params_url = re.findall(self.sub_reg_for_url, req_string)[0]
            async with self.session.delete(params_url) as resp:
                await self.process_resp(resp.status, resp)

        else:
            print("Запрос введён некорректно")

    async def process_resp(self, status, response, flag_write_in_file=False):
        print(status)
        if status not in range(200, 299):
            print(await response.text())
            return

        # если вернулся хороший код
        d = json.loads(await response.text())
        d.pop('status', None)
        print(d)
        if "Location" in d:
            print(d["Location"])
            return

        if flag_write_in_file is True:
            await self.write_in_csv(d)

    async def write_in_csv(self, d):
        for lab_name in d:
            if lab_name not in self.fieldnames:
                self.fieldnames.append(lab_name)
        with open(self.file_name, 'a+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            # writer.writeheader()
            for lab_name in d:
                lab_params_dict = json.loads(d[lab_name])
                print(lab_name, lab_params_dict)




print("Пожалуйста, введите запрос согласно шаблону: \n"
      "{тип запроса}: {URL-адрес сервера:порт} {параметры запроса в формате json} \n"
      "Примеры:\n"
      "post: http://localhost:8080/labs {\"name\": \"lab1\", \"date\": \"12.12.2021\"}\n"
      "post: http://localhost:8080/labs {\"name\": \"lab2\", \"date\": \"23.12.2021\"}\n"
      "patch: http://localhost:8080/labs/lab1 {\"description\" : \"lala\", \"add_students\" : \"Kira, Dima\"}\n"
      "patch: http://localhost:8080/labs/lab1 {\"description\" : \"lala\", \"delete_students\" : \"Dima\"}\n"
      "get: http://localhost:8080/labs\n"
      "get: http://localhost:8080/labs/lab1\n"
      "delete: http://localhost:8080/labs/lab1\n"
      "Для завершения сессии нажмите CTRL+E")


asyncio.run(Client().run_session())

