# -*- encoding: utf-8 -*-


# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#
# s = Student()
# s.birth = 1222
# print(s.birth)


class Student(object):

    # def __init__(self, score, name):
    #     self.__score = score
    #     self.__name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be in 0 ~ 100')
        self._score = value


s = Student()
s.score = 20
print(s.score)