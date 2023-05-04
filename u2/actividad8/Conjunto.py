from collections.abc import Iterable


class Conjunto:

    def __init__(self, e0):
        self.__elem = []
        if isinstance(e0, Iterable):
            for e in e0:
                if e not in self.__elem:
                    self.__elem.append(e)
        else:
            self.__elem.append(e0)

    def __add__(self, o):
        v = self.__elem.copy()
        v.extend([e for e in o.__elem if e not in v])
        return Conjunto(v)

    def __sub__(self, o):
        v = [x for x in self.__elem if x not in o.__elem]
        return Conjunto(v)

    def __eq__(self, ot):
        rtn = False
        if len(self.__elem) == len(ot.__elem):
            i = 0
            while i < len(self.__elem) and self.__elem[i] in ot.__elem:
                i += 1
            rtn = i == len(self.__elem)
        return rtn

    def __str__(self):
        rtn = ""
        if len(self.__elem) > 10:
            rtn = f"{self.__elem[:10]}"
        else:
            rtn = f"{self.__elem}"
        return rtn
