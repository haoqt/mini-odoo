class Registry:
    def __init__(self):
        self.modules = {}

    def load_modules(self, addons_path):
        # Phase 0: discovery only
        for path in addons_path:
            # placeholder for addon scanning
            pass
