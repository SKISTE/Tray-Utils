from time import sleep
from utils import pystray
from PIL import Image
import configparser
import tkinter as tk

from utils.exceptions import *
from utils.commands import AllCommands
from utils.templater import Templater
from utils.load_lang import Language
from utils.module_switcher import ModuleDialog

STOP = False

import os

class main_thread():
    def __init__(self) -> None:
        # Icon for tray
        self.image = Image.open('ico.ico')  

        # Загрузка настроек
        self.config = None 
        self.load_settings()
        self.settings = self.config['Settings']

        # Загрузка языка
        self._lang = Language(self.settings['lang'])
        self.lang = self._lang.lang_dict

        # Загрузка всех комманд
        self.commands = AllCommands(self.config)
        self.commands._init_all_commands()

        self.menu = None
        self.create_menu()

        self.tray = pystray.Icon('Утилиты', self.image, menu=self.menu)
        pass

    def load_settings(self):
        self.config = configparser.ConfigParser()
        self.config.read('setting.ini')
        if self.config.sections() == []:
            open('setting.ini','w',encoding='utf-8').write(Templater.settings())
            raise SettingsFileNotFinded('Settings file not finded, created template "setting.ini", please restart the app')
        
    def menu_module_switch(self):
        root = tk.Tk()
        root.geometry('800x600+100+100')

        module_names = self.commands.get_commands_list()
        temp = []
        for x in module_names:
            try:
                self.config['Imports'][x]
                if self.config['Imports'][x] == '0':
                    temp.append({x:False})
                else:
                    temp.append({x:True})
            except KeyError:
                temp.append({x:False})
        root.withdraw()
        dialog = ModuleDialog(root, temp,self.lang)

        root.wait_window(dialog)
        if dialog.result != "STOP" and dialog.result != None:
            self.config['Imports'] = {}
            for x in dialog.result.keys():
                key = x
                value = dialog.result[key]
                if value:
                    value = '1'
                else:
                    value = '0'
                self.config['Imports'][str(key)] = value
                with open('setting.ini', 'w') as configfile:
                    self.config.write(configfile)
        root.destroy()

        self._restart()

    def menu_exit(self):
        global STOP
        STOP = True
        self.tray.stop()

    def _restart(self):
        self.tray.stop()
        self.tray = None


    def create_menu(self):
        all_items = ()
        for x in self.commands.commands:
            temp = x(self.config)

            try:    name = temp.name
            except: raise NameForCommandNotFound(self.lang, temp.__name__)

            try:    subname = temp.subname
            except: subname = ''

            try:    name = self.lang[name]
            except: name = name

            try:    submenu = temp.submenu
            except: submenu = False

            if submenu:
                classes = temp.methods
                temp_submenu = ()
                for x in classes:
                    
                    try:    method_name = x.name
                    except: raise NameForCommandNotFound(self.lang, x.__name__)

                    try:    method_name = self.lang[method_name]
                    except: pass

                    try:    method_subname = x.subname
                    except: method_subname = ''
                    print(method_name)
                    print(method_subname)
                    temp_submenu = temp_submenu + (pystray.MenuItem(method_name+method_subname, x.run),)
                all_items = all_items + (pystray.MenuItem(name+subname,pystray.Menu(temp_submenu)),)
            else:
                all_items = all_items + (pystray.MenuItem(name+subname, temp.run),)
        # print(all_items)
        # self.menu = pystray.Menu((pystray.MenuItem('gg', lambda: print('gg'))))
        all_items = all_items + (pystray.MenuItem(self.lang['ModuleSwitch'], self.menu_module_switch),)
        all_items = all_items + (pystray.MenuItem(self.lang['exit'], self.menu_exit),)
        # all_items = all_items + (pystray.MenuItem('restart', self._restart),)
        self.menu = pystray.Menu(all_items)
            

    def run(self):
        self.tray.run()

while True:
    if not STOP:
        x = main_thread()
        x.run()
    else:
        break
