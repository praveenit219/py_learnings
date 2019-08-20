#Keyworded Variable Length Arguments in Python | **kwargs

def person(name, **args):
    print(name)
    print(args)
    for k,v in args.items():
        print(k, v)

#person('nani', 30, 'singapore', 96939393)
person('nani', age=30, city='singapore', mobile=9453453)