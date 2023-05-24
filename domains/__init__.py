from importlib import import_module

list = ['Domain1', 'Domain2']

dm = {} # список объектов проверки

for name in list:
    module = import_module(__package__+'.'+name)
    klass = getattr(module, name)
    dm[name] = klass()




