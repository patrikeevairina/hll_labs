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
        # except EOFError:
        #     await self.session.close()
        #     print("Сессия завершена успешно")
        #     exit(0)
        except Exception as e:
            print(e)
            await self.session.close()
            print("Сессия завершена")
            exit(-1)

    async def input_to_req(self):
        input_text = "Введите запрос: \n"
        req_string = input(input_text).removeprefix(input_text)

        is_post = re.fullmatch(self.reg_for_post, req_string)
        is_patch = re.fullmatch(self.reg_for_patch, req_string)
        is_get = re.match(self.reg_for_get_lab, req_string)
        is_get_all =  re.match(self.reg_for_get_all, req_string)
        is_delete = re.match(self.reg_for_delete_lab, req_string)

        if is_post:
            print("Создание лабораторной работы")
            params_string = re.findall(self.sub_reg_for_params, req_string)[0]
            params_dict = json.loads(params_string)
            async with self.session.post(self.url, params=params_dict) as resp:
                await self.process_create_lab_resp(resp.status, resp)

        elif is_patch:
            print("Изменение лабораторной работы")
            params_url = re.findall(self.sub_reg_for_url, req_string)[0]
            params_string = re.findall(self.sub_reg_for_params, req_string)[0]
            params_dict = json.loads(params_string)
            async with self.session.patch(params_url, params=params_dict) as resp:
                await self.check_resp_is_success(resp.status, resp)

        elif is_get:
            print("Получение данных о лабораторной работе")
            params_url = re.findall(self.sub_reg_for_url, req_string)[0]
            async with self.session.get(params_url) as resp:
                await self.process_get_lab(resp.status, resp)

        elif is_get_all:
            print("Получение данных о всех лабораторных работах")
            async with self.session.get(self.url) as resp:
                await self.process_get_all_labs(resp.status, resp)

        elif is_delete:
            print("Удаление лабораторной работы")
            params_url = re.findall(self.sub_reg_for_url, req_string)[0]
            async with self.session.delete(params_url) as resp:
                await self.check_resp_is_success(resp.status, resp)
        else:
            print("Запрос введён некорректно")

    @staticmethod
    async def check_resp_is_success(status, response) -> bool:
        print(status)
        if status not in range(200, 299):
            print(await response.text())
            return False
        return True

    async def process_create_lab_resp(self, status, response):
        if await self.check_resp_is_success(status, response) is False:
            return
        d = json.loads(await response.text())
        d.pop('status', None)
        print(d)
        if "Location" in d:
            print(d["Location"])
            return
        else:
            print("Отсутствует заголовок \'Location\'")
        
    async def process_get_lab(self, status, response):
        if await self.check_resp_is_success(status, response) is False:
            return
        
        raw_lab_dict = json.loads(await response.text())
        raw_lab_dict.pop('status', None)

        if len(raw_lab_dict) != 1:
            print(raw_lab_dict, "Incorrect lab format")
            return
        
        lab_name = list(raw_lab_dict.keys())[0]
        lab_params_dict = json.loads(raw_lab_dict[lab_name])
        # print(lab_name, lab_params_dict, type(lab_params_dict))

        lab_date = lab_params_dict['deadline']
        lab_descr = lab_params_dict['description']
        lab_students_list = lab_params_dict['students'].replace(" ", "").strip().split(",")

        print(lab_name, lab_date, lab_descr, lab_students_list)
        with open("{}.csv".format(lab_name), 'w', newline='') as csv_file:
            fields = ['students', 'lab_params']
            writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=';')
            writer.writerow({'lab_params': lab_name})
            writer.writerow({'lab_params': lab_date})
            writer.writerow({'lab_params': lab_descr})
            for student in lab_students_list:
                if student != '':
                    writer.writerow({'students': student, 'lab_params': '+'})

    async def process_get_all_labs(self, status, response):
        if await self.check_resp_is_success(status, response) is False:
            return
        
        raw_lab_dict = json.loads(await response.text())
        raw_lab_dict.pop('status', None)

        fields = ['students']
        lab_name_dict = dict()
        lab_date_dict = dict()
        lab_descr_dict = dict()
        lab_all_students_list = list()
        lab_students_dict = dict()
        
        for lab_name in raw_lab_dict.keys():
            fields.append(lab_name)
            lab_params_dict = json.loads(raw_lab_dict[lab_name])
            lab_name_dict[lab_name] = lab_name
            lab_date_dict[lab_name] = lab_params_dict['deadline']
            lab_descr_dict[lab_name] = lab_params_dict['description']
            lab_students_dict[lab_name] = lab_params_dict['students'].replace(" ", "").strip().split(",")
            lab_all_students_list += lab_students_dict[lab_name]

        lab_all_students_set = set(lab_all_students_list)
        
        with open("labs.csv", 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=';')

            writer.writerow(lab_name_dict)
            writer.writerow(lab_date_dict)
            writer.writerow(lab_descr_dict)
            
            for student in [*lab_all_students_set]:
                if student == '':
                    continue
                student_results = dict()
                student_results['students'] = student
                for lab_name in lab_name_dict.keys():
                    if student in lab_students_dict[lab_name]:
                        student_results[lab_name] = "+"
                    else:
                        student_results[lab_name] = "-"
                writer.writerow(student_results)



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

