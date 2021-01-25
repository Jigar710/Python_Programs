class Foo:

    def __init__(self, bar):
        self._bar = bar

    @property
    def bar(self):
        """Getter for '_bar'."""
        return self._bar
		
t = Foo(10)
print(t._bar)
t.a = 100