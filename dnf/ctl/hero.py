import keys


class summoner:

    def __init__(self):
        keyBord = keys.Keys()
        keyWork = keys.KeysWorker(keyBord)
        keyWork.sendKey(keyBord.dk['UP'])
