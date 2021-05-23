import os


class PlayBase(object):
    def __init__(self, playbook_path, inventory=None):
        self.play_facts = {
            'managed_by': 'GOVNO'
        }
        self.playbook_path = playbook_path
        self.inventory_path = inventory
        self.govnsible_pwd = os.getcwd()
        self.host_exec_group = None
        self.connection = None

    def set_fact(self, fact_name, fact_value):
        self.play_facts[fact_name] = fact_value
        return self.play_facts

    def get_fact(self, fact_name):
        return self.play_facts[fact_name]


