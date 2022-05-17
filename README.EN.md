# Jaa.py

**Jaa.py** - minimalistic one-file plugin framework with no dependencies.
All you need is root file "jaa.py"

#### Main functions
- run all plugins files from "plugins" folder, based on filename (Plugin filename must start with "plugin_")
- save plugin options in "options" folder in JSON text files for further editing

Must be in root folder due to plugin path calculation

### Plugins
* must located in plugins/ folder
* (usually) must start with "plugin_" prefix
* must have "start(core)" function, that returns manifest dict
* manifest must contain keys "name" and "version"
* manifest can contain "default_options"
  * if contain - options will be saved in "options" folder, are editable, and will load next time
  * if contain - "start_with_options(core,manifest)" function will run with manifest with "options" key
* manifest will be processed in "core.process_plugin_manifest" function. If you wanna - override it

### Options (for plugins)
* are saved under "options" folder in JSON format
* created at first run plugin with "default_options"
* updated when plugin change "version"

### Example usage
```
from jaa import JaaCore

class VoiceAssCore(JaaCore): # class must override JaaCore
    def __init__(self):
        JaaCore.__init__(self)
  ...

main = VoiceAssCore()
main.init_plugins(["core"]) # 1 param - first plugins to be initialized
                            # Good if you need some "core" options/plugin to be loaded before others
                            # not necessary starts with "plugin_" prefix

also can be run like

main.init_plugins()
```
### Requirements
Python 3.5+ (due to dict mix in final_options calc), can be relaxed
