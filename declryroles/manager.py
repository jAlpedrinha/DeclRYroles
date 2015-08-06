from scholrroles import registry
from scholrroles.models import Role, Permission

class PermissionManager(object):
    _permissions = None

    def __init__(self, user, request = None):
        self.roles = {}
        for role in Role.objects.all():
            role_manager = registry.get_role(role.name)(user,request)
            if role_manager.has_role():
                self.roles[role.name] = role_manager
        self._permissions = Permission.objects.filter(roles__name__in = self.roles.keys()).values_list('pk', flat=True)
    
    @property
    def permissions(self):
        print self._permissions
        return Permission.objects.filter(pk__in=self._permissions)
    
    def has_role(self, name, obj = None):
        if not isinstance(name, list):
            name = [name]
        for name in name:
            has_role = name in self.roles and self.roles[name].has_role_for(obj)
            if has_role:
                return True
        return False

    def get_role_ids(self, name):
        if name in self.roles:
            return self.roles[name].ids
        return []

    def has_perm(self, perm, obj =None):
        print perm
        try:
            split = perm.split('_')
            app_label, model, perm_name = split[0], split[1], '_'.join(split[2:])
            perm = self.permissions.get(name=perm_name, content_type__app_label = app_label, content_type__model=model, instance_perm = obj != None)
            if obj:
                for role in perm.roles.all():
                    if role.name in self.roles:
                        role_manager = self.roles[role.name]
                        if role_manager.has_role_for(obj) and role_manager.can_apply_permission(obj, perm):
                            return True
                return False
            else:
                return True
        except Exception as e:
            print e
            return False
