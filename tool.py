class Tool:
    def __init__(self, name, description, func, parameters=None):
        self.name = name
        self.description = description
        self.func = func
        self.parameters = parameters

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)
