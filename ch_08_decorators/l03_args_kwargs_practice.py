def configure_plugin_decorator(func):
    def wrapper(*args):
        # args is e.g. (("path", "~/duplicates"), ("prefix", "duplicate_"))
        config_dict = dict(args)
        return func(**config_dict)

    return wrapper
