from utils.commands import Defs_for_all


class method1(Defs_for_all):
    def __init__(self, config) -> None:
        self.name = 'explorer_kill'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        # self.subname = 'SUBNAME'
    def run(self):
        self._run_cmd('taskkill /F /IM explorer.exe')
        return True
class method2(Defs_for_all):
    def __init__(self, config) -> None:
        self.name = 'explorer_restart'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        # self.subname = 'SUBNAME'
    def run(self):
        self._run_cmd('taskkill /F /IM explorer.exe')
        self._run_cmd('start explorer.exe')
        return True

# Menu item with submenu pattern

class explorer_utils(Defs_for_all):
    def __init__(self, config):
        self.name = 'explorer_utils'
        # self.subname = 'subname'    # Also with classic template

        # IMPORTANT
        # If you want submenu group, make this bool
        self.submenu = True
        self.methods = [method1(config),method2(config)]