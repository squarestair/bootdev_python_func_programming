def create_markdown_image(alt_text):
    def inner_func(url):
        nalt = f"![{alt_text}]"
        nurl = f'({url.replace("(","%28").replace(")","%29")}'
        # print("PRINT:",nalt," and ",nurl)
        def inner_func2(title=None):
            print(title)
            if title != None:
                return f'{nalt+nurl} "{title}")'
            else:
                return f"{nalt+nurl})"
        return inner_func2
    return inner_func
