#!/usr/bin/python3.8.x
if __name__ == '__main__':
    import hidden_4

    var_names = [name for name in dir(hidden_4) if not name.startswith('__') 
            and not callable(getattr(hidden_4, name)) ]

    print(var_names)
