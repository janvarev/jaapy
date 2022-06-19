from jaa import load_options

# ------------------- main loop ------------------
if __name__ == "__main__":
    # this options can be adjusted after first run in "rundemojaa2file.json" file

    default_options={
        "pizza": "pepperoni",
        "place": "New-York",
    }

    options = load_options(py_file=__file__,default_options=default_options)
    # alt way
    #options = load_options(options_file="rundemojaa2file.json",default_options=default_options)

    print("*"*80)
    print("This is example of using JAA load_options() function (from file)")
    print("It's the same as for plugins, but direct for one file")
    print("*"*80)

    print("Current options: deliver {0} pizza to {1}".format(options["pizza"],options["place"]))