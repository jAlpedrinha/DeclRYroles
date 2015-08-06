from collections import defaultdict
from .utils import get_value_from_accessor

class RoleBehaviour(object):
    ids = []
    object_accessors = {}

    def __init__(self, user, request):
        self.user = user
        self.request = request

    def has_role(self):
        return False

    def has_role_for(self, obj):
        if self.has_role() and self.ids and obj:
            if self.role in obj.role_accessors:
                return get_value_from_accessor(obj, obj.role_accessors[self.role]) in self.ids
        return True

    def can_apply_permission(self, obj, perm):
        method = 'has_{}_{}_permission'.format(self.role, perm.name)
        if hasattr(obj, method):
            function = getattr(obj, method)
            if callable(function):
                return function(self.user)
        return True

class UserBehaviour(RoleBehaviour):
    role= 'user'
    def has_role(self):
        return True

def role_behaviour_factory():
    return RoleBehaviour
    
class RoleBehaviourRegistry(object):
    _registry = defaultdict(role_behaviour_factory)
    def register(self, cls):
        self._registry[cls.role] = cls

    def get_role(self, role):
        return self._registry[role]

registry = RoleBehaviourRegistry()