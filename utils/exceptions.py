
class LanguageNotFinded(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(f'Language "{message}" not finded, try to check this lang in langs dir, or change to def value "en"')

class SettingsFileNotFinded(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class NameForCommandNotFound(Exception):
    def __init__(self,lang, name) -> None:
        super().__init__(lang['NameForCommandNotFound']+f'"{name}"')