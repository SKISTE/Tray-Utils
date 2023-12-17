from utils.commands import Defs_for_all

# Template for 1 menu item

class template(Defs_for_all):
    def __init__(self, config):
        self.name = 'clean_bin'          # Name for you func in menu, you can write ID and append in language file or hardcore write name
        # self.subname = 'SUBNAME'    # Name + subname, you can delete this, if wantn't
        
    def run(self):
        # You'r code there
        print('Work')
        return True