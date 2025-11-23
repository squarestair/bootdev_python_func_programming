def replacer(old, new):
    def replace_func(decorator):
        def wrapper(text):
            a = text.replace(old, new)
            # print("debug :", a, text, old, new)
            return decorator(a)

        return wrapper

    return replace_func


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
