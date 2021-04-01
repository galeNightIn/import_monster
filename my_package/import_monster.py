from types import ModuleType
from typing import List, Optional, Union, Callable
import importlib


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    methods_list = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Ahctung! it is neither the str nor the module")
            met = getattr(mod, method_name, None)
            if met and met.__call__:
                methods_list.append(met)
        except ImportError:
            continue
    return methods_list


my_list = methods_importer("func3", ["my_mod", "my_mod2"])
print(my_list)
