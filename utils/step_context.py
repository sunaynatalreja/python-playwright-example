class StepContext:
    current_step = "no_step"

    @classmethod
    def set_step(cls, name):
        cls.current_step = name.replace(" ", "_")

    @classmethod
    def get_step(cls):
        return cls.current_step
