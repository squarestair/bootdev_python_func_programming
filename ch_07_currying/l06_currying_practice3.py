def new_resizer(max_width, max_height):
    def inner_func(min_width=0,min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        def inner2(width,height):
            if width > max_width:
                width = min(width,max_width)
            elif width < min_width:
                width = max(width,min_width)

            if height > max_height:
                height = min(height,max_height)
            elif height < min_height:
                height = max(height,min_height)
            return width, height
        return inner2
    return inner_func
