
class ToBend:
    """Расчет изгибающего напряжения(sigma) и относительной деформации при изгибе(Е).
        Параметры образца вводятся в миллиметрах"""
    __length = 0  # расстояние между опорами, мм
    __width = 0  # ширина испытуемого образца, мм
    __height = 0  # толщина образца, мм
    __F = 289.5
    __S = 1

    def __init__(self, length=64.0, width=13.0, height=4.0):
        self.__length = length
        self.__width = width
        self.__height = height

    # @property
    # def get_length(self):
    #     return self.__length
    #
    # @property
    # def get_width(self):
    #     return self.__width
    #
    # @property
    # def get_height(self):
    #     return self.__height
    #
    # @property
    # def get_F(self):
    #     return self.__F

    @property
    def get_sigma(self):
        return round((3 * self.__F * self.__length) / (2 * self.__width * self.__height ** 2), 2)

    @property
    def get_E(self):
        return (600 * self.__S * self.__height) / self.__length

    @property
    def get_anoter_E(self):
        pass

class Break(ToBend):
    def __init__(self, *args, **kwargs):
        super(Break, self).__init__(*args, **kwargs)


b = ToBend()

print(b.get_sigma)
