def is_valid_walk(walk):
    back_to_start = (walk.count("n")==walk.count("s") and walk.count("w")==walk.count("e"))
    if len(walk)==10 and back_to_start:
        return True
    else:
        return False
