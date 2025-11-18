def args_logger(*args, **kwargs):
    for ind, arg in sorted(enumerate(args)):
        print(f"{ind + 1}. {arg}")
    for kwarg in sorted(kwargs):
        print(f"* {kwarg}: {kwargs[kwarg]}")
    return 0
