from . import keys, logger


class Summoner:

    def __init__(self):
        lg = logger.Logger()
        kb = keys.Keys(lg)
        kb.directKey('space')
        kb.parseKeyString('left,-120,up,-120,right,-120,space')
        kb.parseKeyString('q,-220,w,-220,e,-220,t,-220,a,-220,s,-220,d,-220,f')
        kb.parseKeyString('right,-220,up,-220,right,-220,z')
        kb.parseKeyString('right,-220,up,-220,right,-220,space')
        kb.parseKeyString('left,-220,up,-220,left,-220,space')
        kb.parseKeyString('up,-220,down,-220,space')
        self.kb = kb

