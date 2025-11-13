def list_files(parent_directory, current_filepath=""):
    if not parent_directory:
        return current_filepath

    fl = []
    for key in parent_directory.keys():
        if parent_directory[key] == None:
            # print("INSIDE NONE: "+current_filepath+"/"+key)
            fl.append((f"{current_filepath}/{key}"))
        else:
            # print("RECURSE AND FOUND LIST :",parent_directory[key])
            fl.extend(list_files(parent_directory[key],f"{current_filepath}/{key}"))
    return fl
