def new_collection(initial_docs):
    new_list = initial_docs.copy()
    def inner_func(str):
        new_list.append(str)
        return new_list

    return inner_func
