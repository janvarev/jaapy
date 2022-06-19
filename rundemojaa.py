import traceback

from jaa import JaaCore

class CmdCore(JaaCore):
    def __init__(self):
        JaaCore.__init__(self,__file__)

        # if your file is in same folder with Jaa.py you can use short version
        #JaaCore.__init__(self)

        self.commands = {}

    # ----------- process plugins functions ------
    def process_plugin_manifest(self,modname,manifest):
        res = manifest

        # adding commands from plugin manifest
        if "cmds" in res: # process commands
            for cmd in res["cmds"].keys():
                self.commands[cmd] = res["cmds"][cmd]

    # -------- main function ----------
    def execute(self,command):
        try:
            for keyall in self.commands.keys():
                if command.startswith(keyall):
                    params = command[(len(keyall)+1):]
                    self.commands[keyall](self,params)
                    return True
                else:
                    pass

            # if command not founded
            return False
        except Exception as err:
            print(traceback.format_exc())

# ------------------- main loop ------------------
if __name__ == "__main__":
    cmd_core = CmdCore()
    cmd_core.jaaOptionsPath = "options"
    # cmd_core.jaaShowTracebackOnPluginErrors = True # if you uncomment this, traceback on error plugin will also be shown
    cmd_core.init_plugins()

    print("*"*80)
    print("This is JAA example usage - command interpreter.")
    print("Try use commands 'hello', 'pizza1', 'pizza2', 'exit'.")
    print("*"*80)
    while True:
        cmd = input("Enter command> ")
        if cmd == "exit":
            break

        res = cmd_core.execute(cmd)
        if not res:
            print("Unknown command, try another")