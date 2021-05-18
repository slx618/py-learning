from . import keys
from . import logger

class Actions:
    def __init__(self):
        lg = logger.Logger()
        self.kb = keys.Keys(lg)


    def moveUp(self):
        self.kb

