import importlib, pkgutil
import govnsiblecli.modules.base.utils.display

class ExecutorBase(object):
    def __init__(self, executor_type, executor_params=None):
        self.executor_type = executor_type
        self.executor_params = executor_params
        self.logger = govnsiblecli.modules.base.utils.display.get_logger('root')
        self.module_list = []
        self.index_modules()

    def send_msg(self,msg):
        return self.logger.info(msg)

    def index_modules(self):
        from govnsiblecli.modules import general
        module_list = [modname for importer, modname, ispkg in
                       pkgutil.walk_packages(path=general.__path__, prefix=general.__name__ + '.')]
        for modname in module_list:
            # Try to import the package
            module = importlib.import_module(modname)
            mod_info = module.mod_info()
            print(mod_info)
            mod_dict = {'mod_name': mod_info.get('module_name'), 'mod_py_name': modname}
            self.module_list.append(mod_dict)

def scan_executor():
    executor_list = []
    from govnsiblecli.modules import executor
    module_list = [modname for importer, modname, ispkg in
                   pkgutil.walk_packages(path=executor.__path__, prefix=executor.__name__ + '.')]
    for modname in module_list:
        module = importlib.import_module(modname)
        mod_info = module.mod_info()
        print(mod_info)
        mod_dict = {'executor_name': mod_info.get('module_name'), 'executor_py_name': modname}
        executor_list.append(mod_dict)



