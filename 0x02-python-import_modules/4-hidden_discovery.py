#!/usr/bin/python3.8.x
if __name__ == '__main__':
    import hidden_4

    var_names = [name for name in dir(hidden_4) if name.isidentifier()]

    print(var_names)
