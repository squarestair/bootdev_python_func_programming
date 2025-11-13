def zipmap(keys, values):
    if not keys or not values:
        return {}
    a = zipmap(keys[1:],values[1:])
    a[keys[0]] = values[0]
    return a
