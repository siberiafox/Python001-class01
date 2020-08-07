from abc import ABCMeta, abstractproperty


class Animal(metaclass=ABCMeta):
    _Kind_Zone = ('herb', 'pred')
    _Body_Zone = ('small', 'medium', 'big', 'huge')
    _Nature_Zone = ('soft', 'common', 'tough')

    @abstractproperty
    def kind(self):
        "子类需实现该属性"

    @abstractproperty
    def body(self):
        "子类需实现该属性"

    @abstractproperty
    def nature(self):
        "子类需实现该属性"

    @abstractproperty
    def is_beast(self):
        "子类需实现该属性"



class Cat(Animal):
    Yelling = 'miaomiaomiao'

    def __init__(self, name, kind, body, nature, is_pet=False):
        self.kind = kind
        self.body = body
        self.nature = nature

        self.name = name
        self.is_pet = is_pet

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if value not in self._Kind_Zone:
            raise ValueError(f'kind value must be one of {self._Kind_Zone}')
        self._kind = value

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if value not in self._Body_Zone:
            raise ValueError(f'kind value must be one of {self._Body_Zone}')
        self._body = value

    @property
    def nature(self):
        return self._nature

    @nature.setter
    def nature(self, value):
        if value not in self._Nature_Zone:
            raise ValueError(f'kind value must be one of {self._Nature_Zone}')
        self._nature = value

    @property
    def is_beast(self):
        mask = (self.kind == 'pred') & (
            self.body != 'small') & (self.nature == 'tough')

        if mask:
            self.__is_beast = True
        else:
            self.__is_beast = False
        return self.__is_beast

# 单例模式
class Zoo:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name
        self.__animal_types = ()

    def add_animal(self, animal):
        if type(animal) == ABCMeta:
            raise TypeError('动物必须是实例对象！')

        if isinstance(animal, Animal):
            if animal.__class__.__name__ not in self.__animal_types:
                self.__animal_types += (animal.__class__.__name__,)
            else:
                print(f'该动物类型已登记在 {self.name} 内!')

        else:
            print('该动物是外星物种，禁止添加入园！')

    def __getattr__(self, value):
        if value in self.__animal_types:
            return True
        if str(value).startswith('__'):
            return None
        return False

    def get_zoo_animal_types(self):
        return self.__animal_types


# # module test
if __name__ == '__main__':

    zoo = Zoo('Just Only One The ZooTopiA City In World')

    print(zoo.name)

    kitty = Cat('Kitty', 'herb', 'small', 'soft', is_pet=True)
    tom = Cat('Tom', 'pred', 'medium', 'tough')

    zoo.add_animal(kitty)

    print(zoo.get_zoo_animal_types())

    zoo.add_animal(tom)

    print(zoo.get_zoo_animal_types())

    zoo.add_animal(123456)

    print(getattr(zoo, 'Cat'))
    print(getattr(zoo, 'Dog'))

    print(kitty.is_beast)
    print(tom.is_beast)
