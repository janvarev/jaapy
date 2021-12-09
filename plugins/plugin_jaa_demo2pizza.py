# Demo 2

pizza_type = ""

# start function
def start(core):
    manifest = {
        "name": "Demo 2 order pizza with options",
        "version": "1.0",

        "default_options": {
            "pizza_type": "pepperoni",
            "other_param": "lala",
        },

        "cmds": {
            "pizza1": run_order_pizza1,
            "pizza2": run_order_pizza2,
        }

    }
    return manifest

def start_with_options(core,manifest):
    global pizza_type
    pizza_type = manifest["options"]["pizza_type"]

    #return manifest # manifest can be returned to further process, if you changed it

def run_order_pizza1(core,params):
    print("Ordering pizza 1 ({0})...".format(pizza_type))
    print("(to change pizza type, edit options/plugin_jaa_demo2pizza.json file)")

def run_order_pizza2(core,params):
    # another way to get options
    import os
    modname = os.path.basename(__file__)[:-3] # calculating modname
    options = core.plugin_options(modname)
    print("Ordering pizza 2 ({0})...".format(options["pizza_type"]))

    print("(to change pizza type, edit options/plugin_jaa_demo2pizza.json file)")

