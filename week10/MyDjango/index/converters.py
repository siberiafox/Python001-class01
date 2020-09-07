class IndexConverter:
    regex = '[a-z.a-z]'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value