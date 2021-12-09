# Demo 0

# start function
def start(core):
    manifest = {
        "name": "Demo 1 cmd",
        "version": "1.0",

        "cmds": {
            "hello": run_hello,
        }
    }
    return manifest

def run_hello(core,params):
    print("Hello, world!")