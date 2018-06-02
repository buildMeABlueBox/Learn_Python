def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

var_args("Jean Carlos", description="golanger", feedback=None)

