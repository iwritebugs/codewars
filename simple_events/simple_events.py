"""
Your goal is to write an Event constructor function, which can be used to make
event objects.

An event object should work like this:

    it has a .subscribe() method, which takes a function and stores it as its
    handler

    it has an .unsubscribe() method, which takes a function and removes it from
    its handlers

    it has an .emit() method, which takes an arbitrary number of arguments and
    calls all the stored functions with these arguments

As this is an elementary example of events, there are some simplifications:

    all functions are called with correct arguments (e.g. only functions will be
    passed to unsubscribe)

    you should not worry about the order of handlers' execution

    the handlers will not attempt to modify an event object (e.g. add or remove
    handlers)

    the context of handlers' execution is not important

    each handler will be subscribed at most once at any given moment of time.
    It can still be unsubscribed and then subscribed again

Also see an example test fixture for suggested usage

"""


class Event:

    def __init__(self):
        self._handlers = set()

    def subscribe(self, handler):
        self._handlers.add(handler)

    def unsubscribe(self, handler):
        try:
            self._handlers.remove(handler)
        except KeyError:
            pass

    def emit(self, *args, **kwargs):
        for handler in self._handlers:
            handler(*args, **kwargs)


event = Event()


class Testf:
    def __init__(self):
        self.calls = 0
        self.args = []

    def __call__(self, *args):
        self.calls += 1
        self.args += args


def test_sanity():
    test_function_object = Testf()

    event.subscribe(test_function_object)
    event.emit(1, 'foo', True)

    assert test_function_object.calls == 1  # calls a handler
    assert test_function_object.args == [1, 'foo', True]  # passes arguments

    event.unsubscribe(test_function_object)
    event.emit(2)

    assert test_function_object.calls == 1  # no second call
