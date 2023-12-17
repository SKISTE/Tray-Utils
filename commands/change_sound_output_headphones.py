from utils.commands import Defs_for_all

class change_sound_output_headphones(Defs_for_all):
    def __init__(self, config):
        self.name = 'change_sound_output'
        self.subname = 'Наушники'
        self.path = config['Settings']['dir_to_nircmd']

    def run(self):
        self._run_cmd(f'start {self.path} setdefaultsounddevice "Уши" 1')
        self._run_cmd(f'start {self.path} setdefaultsounddevice "Уши" 2')
        return True