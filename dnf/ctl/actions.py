from . import keys
from . import logger

class Actions:
    def __init__(self):
        lg = logger.Logger()
        self.kb = keys.Keys(lg)


    def up(self):
        self.kb

