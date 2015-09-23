from kao_command import Commands

commands = Commands(__name__, {'export': 'export.Export',
                               'install': 'install.Install',
                               'update': 'update.Update'})