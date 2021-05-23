from govnsiblecli.modules.base.utils.yaml_handler import load_file


class InventoryBase(object):
    def __init__(self, inventory_file):
        self.inventory_file = inventory_file
        self.groups = []

    def init_inventory(self):
        inventory = load_file(self.inventory_file)
        children_inventory = inventory.get('all').get('children')
        group_list = []
        for group_name,v in children_inventory.items():
            group_facts = {'group': group_name}
            host_list = []
            for host,j in v.items():
                host_facts = {}
                for host_fact,k in j.items():
                    host_facts[host_fact] = k
                host_list.append(host_facts)
            group_facts['hosts'] = host_list
            group_list.append(group_facts)
        self.groups = group_list
