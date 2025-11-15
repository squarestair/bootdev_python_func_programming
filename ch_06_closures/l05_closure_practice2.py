import copy #for copy.deepcopy() function

def css_styles(initial_styles):
    new_styles = copy.deepcopy(initial_styles)
    def add_styles(selector,property,value):
        if selector not in new_styles:
            new_styles[selector] = { property:value }
        else:
            new_styles[selector][property] = value
        return new_styles

    return add_styles
