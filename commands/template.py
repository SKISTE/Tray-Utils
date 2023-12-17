from utils.commands import Defs_for_all


# Template for 1 menu item

class template(Defs_for_all):
    def __init__(self, config):
        self.name = 'NAME'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        self.subname = 'SUBNAME'    # Name + subname, you can delete this, if wantn't
        
    def run(self):
        # You'r code there
        print('Work')
        return True
    
# Methods for menu item with submenu

class method1(Defs_for_all):
    def __init__(self, config) -> None:
        self.name = 'NAME'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        self.subname = 'SUBNAME'
    def run(self):
        print('method1')
        return True
class method2(Defs_for_all):
    def __init__(self, config) -> None:
        self.name = 'NAME'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        self.subname = 'SUBNAME'
    def run(self):
        print('method2')
        return True

# Menu item with submenu pattern

class submenu_template(Defs_for_all):
    def __init__(self, config):
        self.name = 'NAME_OF_GROUP'
        self.subname = 'subname'    # Also with classic template

        # IMPORTANT
        # If you want submenu group, make this bool
        self.submenu = True
        self.methods = [method1(config),method2(config)]
