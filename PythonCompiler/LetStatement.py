class LetStatement:
    def __init__(self, identifier, value, is_mutable=False):
        self.identifier = identifier
        self.value = value
        self.is_mutable = is_mutable

    def __repr__(self):
        return f"let {self.identifier} = {self.value}, mutable={self.is_mutable}"
