# Jaa.py

**Jaa.py** - minimalistic one-file plugin framework with no dependencies.
All you need is root file "jaa.py"

## Known usages

- [Irene voice assistant (Russian)](https://github.com/janvarev/Irene-Voice-Assistant)
- [OneRingTranslator](https://github.com/janvarev/OneRingTranslator) - Simple REST service to translate texts with plugins. Automatic calculate BLEU/COMET metrics of translation quality.
- [chain-img-processor](https://github.com/janvarev/chain-img-processor) - Image/video processor with plugins

[Continue in English](/README.EN.md)

**Jaa.py** - минималистичный однофайловый плагинный фреймворк без зависимостей.
Нужен только корневой файл "jaa.py"


#### Основные функции и решаемые задачи
- запускает все плагины из папки "plugins", базируясь на имени (Имя файла плагина должно начинаться с "plugin_")
- сохраняет настройки плагина в папке "options" в JSON формате для дальнейшего редактирования. 
- отвечает за слияние настроек при изменении версии плагина:
  - при изменении версии
  - дефолтовые настройки будут слиты с уже имеющимися в options пользовательскими
  - пользовательские будут иметь приоритет
  - **крайне полезно**, когда вы добавляете новые настройки в плагин, т.к. сохраняются настройки, уже сделанные пользователем

~~jaa.py должен находится в корневой папке для корректного вычисления путей.~~ (устарело с версии 1.6)

**С версии 1.7**

Предоставляет допфункцию load_options, которая делает идентичное слияние настроек, но
для одного файла. Пример в `rundemojaa2file.py`

```python
from jaa import load_options

default_options={
    "pizza": "pepperoni",
    "place": "New-York",
}
options = load_options(py_file=__file__,default_options=default_options)
# alt way
#options = load_options(options_file="rundemojaa2file.json",default_options=default_options)

# опции теперь доступны для правки в rundemojaa2file.json

print("Current options: deliver {0} pizza to {1}".format(options["pizza"],options["place"]))

``` 

**С версии 2.0**

Предоставляет веб-интерфейс для управления настроками (требует установки gradio)

Пример:
```python
if __name__ == "__main__":
    cmd_core = VACore()
    cmd_core.init_with_plugins()
    print("Settings manager for VoiceAssistantCore.")

    gr_int = cmd_core.gradio_render_settings_interface()
    gr_int.launch()
```


### Плагины
* должны находиться в папке plugins/
* (обычно) начинаются с префикса "plugin_"
* ДОЛЖНЫ иметь функцию "start(core)", возвращающую манифест (словарь)
* манифест ДОЛЖЕН содержать ключи "name" и "version"
* манифест МОЖЕТ содержать "default_options"
  * если содержит - настройки будут сохранены в папке "options", их можно отредактировать, и они будут загружены в следующий раз
  * если содержит - "start_with_options(core,manifest)" функция будет запущена, причем манифест будет содержать ключ "options" (уже пользовательские настройки)
* манифест будет обработан в функции "core.process_plugin_manifest". Если хотите - переопределите её.

### Настройки (для плагинов)
* сохраняются в папке "options" в JSON format
* создаются при первом запуске плагина из "default_options"
* обновляются, когда плагин изменяет "version" путем слияния
"default_options" и options/<plugin>.json (последний - в приоритете) 

### Пример использования
```
from jaa import JaaCore

class VoiceAssCore(JaaCore): # class must override JaaCore
    def __init__(self):
        JaaCore.__init__(self,__file__)
  ...

main = VoiceAssCore()
main.init_plugins(["core"]) # 1 param - first plugins to be initialized
                            # Good if you need some "core" options/plugin to be loaded before others
                            # not necessary starts with "plugin_" prefix

also can be run like

main.init_plugins()
```
### Требования
Python 3.5+ (due to dict mix in final_options calc), can be relaxed
