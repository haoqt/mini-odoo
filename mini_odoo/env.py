class Env:
    """
    Central execution context.
    Equivalent to odoo.api.Environment.
    """

    def __init__(self, config, registry, db):
        self.config = config
        self.registry = registry
        self.db = db
        self.context = {}

    def with_context(self, **kwargs):
        new = self.__class__(
            config=self.config,
            registry=self.registry,
            db=self.db,
        )
        new.context = {**self.context, **kwargs}
        return new
