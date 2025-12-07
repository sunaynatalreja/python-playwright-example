from core.driver_factory.base_browser import BrowserBase

from core.config_loader import load_settings
import importlib

class DriverManager:
    _browser_map = None

    @classmethod
    def _load_map(cls):
        if cls._browser_map is None:
            settings = load_settings()
            cls._browser_map = settings["browsers"]["classes"]
        return cls._browser_map

    @staticmethod
    def _import_from_path(path: str):
        module_name, class_name = path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)

    @classmethod
    def get_browser(cls, browser_name: str, **kwargs) -> BrowserBase:
        browser_map = cls._load_map()

        name = browser_name.lower()

        if name not in browser_map:
            raise ValueError(
                f"Unsupported browser '{browser_name}'. Supported browsers: {list(browser_map.keys())}"
            )

        class_path = browser_map[name]
        browser_cls = cls._import_from_path(class_path)

        return browser_cls(**kwargs)