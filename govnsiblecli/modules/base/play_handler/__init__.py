from govnsiblecli.modules.base import PlayBase
from govnsiblecli.modules.base.utils import display

logger = display.get_logger('root')


class PlayHandler(PlayBase):
    def __init__(self, play_contents, *args):
        super(PlayHandler, self).__init__(*args)
        self.play_contents = play_contents
        self.get_host()

    # set_facts_from_play - sets facts from play defenition
    def set_facts_from_play(self):
        facts_to_set = self.play_contents.get('vars')
        for k, v in facts_to_set.items():
            self.set_fact(k, v)
        logger.info(self.play_facts)

    def get_host(self):
        self.host_exec_group = self.play_contents.get('hosts')
        self.connection = self.play_contents.get('connection')
        if self.connection:
            logger.info('Connection param is set to local, sending all tasks to executor type: local')


