def run():
    mi_dict = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    print(mi_dict)
    for c in mi_dict.keys():
        print(c)
    for v in mi_dict.values():
        print(v)
    for c,v in mi_dict.items():
        print(c , v)

    print(len(mi_dict))
    print(mi_dict.get('llave2', None))

if __name__ == '__main__':
    run()
