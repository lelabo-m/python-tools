from operator import attrgetter


def normalize(dictionary):
    if not dictionary:
        return dictionary
    maximum = max(dictionary.values())
    minimum = min(dictionary.values())
    if maximum == minimum:
        return dictionary
    for key, value in dictionary.iteritems():
        dictionary[key] = float(value - minimum) / float(maximum - minimum)
    return dictionary


def normalize_by_key(dictionary, key):
    if not dictionary or not key:
        return dictionary
    maximum = getattr(max(dictionary.values(), key=attrgetter(key)), key)
    minimum = getattr(min(dictionary.values(), key=attrgetter(key)), key)
    if maximum == minimum:
        return dictionary
    for value in dictionary.values():
        newval = float(getattr(value, key) - minimum) / float(maximum - minimum)
        setattr(value, key, newval)
    return dictionary


def sort(dictionary, **kwargs):
    if not dictionary:
        return []
    return sorted(dictionary.iteritems(), key=lambda item: item[1], **kwargs)


def sort_by_key(dictionary, key, **kwargs):
    if not dictionary or not key:
        return []
    return sorted(dictionary.iteritems(), key=lambda item: getattr(item[1], key), **kwargs)


def mean(dictionary):
    if not dictionary:
        return 0.0
    return float(sum([value for value in dictionary.values()])) / float(len(dictionary))


def mean_by_key(dictionary, key):
    if not dictionary or not key:
        return 0.0
    return float(sum([getattr(value, key) for value in dictionary.values()])) / float(len(dictionary))


def filter_by_condition(dictionary, condition):
    if not dictionary:
        return dictionary
    return {k: v for k, v in dictionary.iteritems() if condition(k, v)}