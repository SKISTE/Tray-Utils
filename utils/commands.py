import os
import subprocess
import importlib

# temp = ''

class Defs_for_all():
    def __init__(self) -> None:
        self.run_cmd = self._run_cmd
    def _run_cmd(self,cmd):
        subprocess.run(cmd, shell=True)
    def _stop_all(self):
        global STOP
        STOP = True
        pass

class AllCommands():
    def __init__(self, config) -> None:
        self.config = config
        self.all_files = os.listdir('commands')
        # print(self.all_files)
        self.commands = []

    def get_commands_list(self):
        temp = []
        for x in self.all_files:
            if x != '__pycache__':
                temp.append(x[:-3])
        return temp
    
    def _init_all_commands(self):
        # global temp
        for module in self.all_files:
            if module != '__pycache__':
                
                temp = True
                name = module[:-3]
                try:
                    if self.config['Imports'][name] == '0':
                        temp = False
                except KeyError:
                    temp = False 
                if temp:
                    exec(f'from commands.{name} import {name}')
                    cls = eval(name)
                    self.commands.append(cls)
            pass

        # for filename in os.listdir('commands'):
        #     if filename != '__pycache__':
        #         module = importlib.import_module(f'commands.{os.path.splitext(filename)[0]}')
        #         # print(module)
        #         # Итерируемся по атрибутам модуля
        #         for attr_name in dir(module):
        #             # Проверяем, является ли атрибут классом
        #             attr = getattr(module, attr_name)
        #             # print('===')
        #             # print(attr)
        #             # print('---')
        #             # print(attr_name)
        #             # print('===')
        #             if isinstance(attr, type):
        #                 # Добавляем класс в список команд
        #                 if attr_name != 'Defs_for_all':
        #                     self.commands.append(attr)
        # print(self.commands)

    
