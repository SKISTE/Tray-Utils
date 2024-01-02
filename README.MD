# EN
A small utility with modular commands  
### Info
A program that is added to the system tray. Loads downloaded commands and adds them to itself for quick use
### Usage
Add this program to startup, download the commands you need, turn them on and enjoy life  
[`How to create custom commands`](#Custom)
### Features
 - Support languages
 - Fully modular system
 - Ability to add custom commands
### Preview
#### General view
![image info](preview/en_show.gif)
#### Module Switch
![image info](preview/en_module_switch.gif)

# RU
Небольшая утилита с модульными командами  
### Информация
Программа, которая добавляется в системный трей. Загружает скачанные команды и добавляет их к себе для быстрого использования.
### Использование
Добавьте эту программу в авто загрузку, скачайте нужные вам команды, включите их и наслаждайтесь жизнью  
[`Как создавать пользовательские команды`](#Custom)
### Особенности
 - Поддержка языков
 - Полностью модульная система
 - Возможность добавления пользовательских команд
### Предварительный просмотр
#### Общий вид
![image info](preview/en_show.gif)
#### Переключатель модулей
![image info](preview/en_module_switch.gif)
# Custom
### How to create custom command?
#### Preset for command without submenu features
```py
from utils.commands import Defs_for_all
class template(Defs_for_all):
    def __init__(self, config):
        self.name = 'NAME'
        self.subname = 'SUBNAME' 
        
    def run(self):
        # You'r code there
        print('Work')
        return True
```
**name** (str) - name in list, you can change lang file and write here ID of you name  
Example:  
_en.txt_  
`name_of_your_func=name`
and they will take this name

**subname** (optional) - Second name, name+subname

`run` function will be executed after pressing in the list

#### Preset for command with submenu

```py
class method1(Defs_for_all):
    def __init__(self, config) -> None:
        self.name = 'NAME'name
        self.subname = 'SUBNAME'
    def run(self):
        print('method1')
        return True
class method2(Defs_for_all):
    def __init__(self, config) -> None:
        self.name = 'NAME'
        self.subname = 'SUBNAME'
    def run(self):
        print('method2')
        return True


class submenu_template(Defs_for_all):
    def __init__(self, config):
        self.name = 'NAME_OF_GROUP'
        self.subname = 'subname' 

        # IMPORTANT
        # If you want submenu group, make this bool
        self.submenu = True

        self.methods = [method1(config),method2(config)]
```
name and subname like previous example.  
For create submenu, make bool value `submenu` to `True` and create list of methods in this submenu

**IMPORTANT**  
The name of the file should be named the same as the name of the class  
template.py == class template  
