def interpret_inset(inset):
    """Run the instructions in a virtual machine and
       get the directions to build a path."""

    def make_dir(byte):
        if byte < 64:
            return (-1, 0)
        elif byte < 128:
            return (0, -1)
        elif byte < 192:
            return (1, 0)
        else:
            return (0, 1)

    # TODO: run the machine
    return tuple(map(make_dir, inset))
