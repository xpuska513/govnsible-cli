import importlib

import paramiko

from . import ExecutorBase

MOD_INFO = {
    'module_name': 'local',
    'module_type': 'executor',
    'module_description': 'Local executor to execute commands locally'
}

def mod_info():
    return MOD_INFO

class GovnsibleExecutor(ExecutorBase):
    def __init__(self,host_ip, host_port, username, password):
        super(GovnsibleExecutor, self).__init__('ssh')
        self.connection_type = 'ssh'
        self.host_ip = host_ip
        self.host_port = host_port
        self.username = username
        self.password = password

    def init_env(self):
        #test connection to host
        ssh = paramiko.SSHClient()
        try:
            ssh.connect(f"{self.host_ip}:{self.host_port}", username=self.username, password=self.password)
        except Exception as e:
            print(e)
            return False
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo test')
        if ssh_stdout == "test":
            return True
        else:
            return False


    def execute_task(self, module_name, module_params):
        module = [item for item in self.module_list if item['mod_name'] == module_name]
        print(module)
        mod_py_name = module[0].get('mod_py_name')
        print(mod_py_name)
        dynamic_module = importlib.import_module(mod_py_name)
        mod_handler = dynamic_module.GovnsibleModule(module_params)
        mod_handler.execute_task()
        result = mod_handler.result
        return result
