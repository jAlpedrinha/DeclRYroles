
def get_value_from_accessor(instance, accessor):
    if not accessor:
        return None
    elif accessor == 'self':
        return instance

    if '__' in accessor:
        accessors = accessor.split('__')
    else:
        accessors = [accessor]

    accessor = accessors[0]
    if hasattr(instance, accessor):
        instance = getattr(instance,accessor, None)
    else:
        return None
    if len(accessors) > 1:
        instance = get_value_from_accessor(instance, '__'.join(accessors[1:]))
    return instance