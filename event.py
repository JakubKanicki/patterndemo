
SHUTDOWN = 'shutdown'

events = {}


def add_observer(name, callback):
    if name in events:
        if callback not in events[name]:
            events[name].append(callback)
    else:
        events[name] = [callback]


def trigger_event(name, args=()):
    if name not in events:
        return

    for callback in events[name]:
        callback(*args)
