from typing import *

def init_modules() -> bool:
    init_funcs: List[Callable[[], int]] = [
        init_orbis_user_service,
        init_orbis_save_data3
    ]

    for init_func in init_funcs:
        if init_func() != 0:
            return False
    return True


def jailbreak() -> bool:
    module_id = sceKernelLoadStartModule("/app0/sce_module/libjbc.sprx", 0, None, 0, None, None)
    if module_id == 0:
        return False
    jailbreak : Callable[[],bool] = None
    sceKernelDlsym(module_id, "Jailbreak", AddressOf(jailbreak))
    if jailbreak == None:
        return False
    return jailbreak()


def main() -> int:
    setvbuf(stdout, None, _IONBF, 0)
    
    setup_funcs : List[Callable[[], int] = 
            init_modules,
            jailbreak
    ]
    
    for setup_func in setup_funcs:
        if not setup_func():
            # This is invalid for some PS4 applications,
            # Need to make special exception 
            return -1
    return 0 
