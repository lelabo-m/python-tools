from operator import attrgetter


def normalize(objects):
    if not objects:
        return objects
    maximum = max(objects)
    minimum = min(objects)
    if maximum == minimum:
        return objects
    return [float(value - minimum) / float(maximum - minimum) for value in objects]


def normalize_by_key(objects, key):
    if not objects or not key:
        return
    obj_maximum = max(objects, key=attrgetter(key))
    obj_minimum = min(objects, key=attrgetter(key))
    maximum = getattr(obj_maximum, key)
    minimum = getattr(obj_minimum, key)
    if maximum == minimum:
        return
    for obj in objects:
        value = getattr(obj, key)
        value = float(value - minimum) / float(maximum - minimum)
        setattr(obj, key, value)


def sort_by_key(objects, key):
    if not objects:
        return objects
    return sorted(objects, key=lambda obj: getattr(obj, key))


def mean(objects):
    if not objects:
        return 0.0
    return float(sum([value for value in objects])) / float(len(objects))


def mean_by_key(objects, key):
    if not objects or not key:
        return 0.0
    return float(sum([getattr(obj, key) for obj in objects])) / float(len(objects))


def filter_by_condition(objects, condition):
    if not objects:
        return objects
    return filter(condition, objects)


def first(objects, count):
    if not objects:
        return objects
    return objects[:count]


def last(objects, count):
    if not objects:
        return objects
    if not count:
        return []
    return objects[-count:]


def flatten(objects):
    if not objects:
        return objects
    flattened = [item for sublist in objects if hasattr(sublist, '__iter__') for item in sublist ]
    return flattened if flattened else objects
