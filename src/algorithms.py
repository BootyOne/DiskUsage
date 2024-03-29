import ctypes
import os
import platform


def get_paths_size(path: str, consider_symbolic_links: bool, filter_type: str, filter_types: list) -> (list, list):
    paths = []
    sums = []
    for d, dirs, files in os.walk(f'{path}'):
        sizes = 0
        paths.append(d.split("\\")[-1])
        for e in files:
            if (consider_symbolic_links and os.path.islink(os.path.join(d, e))) or \
                    (filter_type == "e" and e.split(".")[-1] in filter_types):
                pass
            else:
                if (filter_type == "i" and e.split(".")[-1] in filter_types) \
                        or not filter_types or filter_type == "e":
                    sizes += os.path.getsize(os.path.join(d, e))
        sums.append(sizes)
    return paths, sums


def get_free_space(dirname: str) -> float:
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(
            ctypes.c_wchar_p(dirname),
            None, None, ctypes.pointer(free_bytes))
        return free_bytes.value
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize
