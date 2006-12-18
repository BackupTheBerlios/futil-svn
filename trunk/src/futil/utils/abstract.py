"""

 Trick to create abstract classes (raises error when instatiate)

 http://www.lychnis.net/index/programming/python-abstract-methods-3.lychnis

 Example: definition of an abstract class called "MyAbstractClass" with
  a virtual method called "getSomething"

 class MyAbstractClass(object):
     __metaclass__ = Metaclass
     getSomething = AbstractMethod('getSomething')

 
"""

class AbstractMethod (object):
    def __init__(self, func):
        self._function = func
                
    def __get__(self, obj, type):
        return self.AbstractMethodHelper(self._function, type)

    class AbstractMethodHelper (object):
        def __init__(self, func, cls):
            self._function = func
            self._class = cls

        def __call__(self, *args, **kwargs):
            raise TypeError('Abstract method `' + self._class.__name__ \
                            + '.' + self._function + '\' called')

class Metaclass (type):
    def __init__(cls, name, bases, *args, **kwargs):
        type.__init__(cls, name, bases, *args, **kwargs)
        cls.__new__ = staticmethod(cls.new)
        
        ancestors = list(cls.__mro__)
        ancestors.reverse()  # Start with __builtin__.object
        abstractmethods = []
        for ancestor in ancestors:
            for clsname, clst in ancestor.__dict__.items():
                if isinstance(clst, AbstractMethod):
                    abstractmethods.append(clsname)
                else:
                    if clsname in abstractmethods:
                        abstractmethods.remove(clsname)

        abstractmethods.sort()
        setattr(cls, '__abstractmethods__', abstractmethods)

    def new(self, cls):
        if len(cls.__abstractmethods__):
            raise NotImplementedError('Can\'t instantiate class `' + \
                                      cls.__name__ + '\';\n' + \
                                      'Abstract methods: ' + \
                                      ", ".join(cls.__abstractmethods__))
        
        return object.__new__(self)
