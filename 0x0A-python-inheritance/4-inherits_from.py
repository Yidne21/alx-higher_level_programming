#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    This method returns true if obj is the instance of a_class or it the instance it's subclass
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
