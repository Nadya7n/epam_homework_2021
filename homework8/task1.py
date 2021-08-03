class KeyValueStorage:
    storage = {}

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        with open(path_to_file) as fh:
            for line in fh:
                line = line.strip().split("=")
                key, value = line[0], line[1]
                if key.isdigit():
                    raise ValueError(
                        f"Value - {key} - cannot be assigned to an attribute"
                    )
                else:
                    self.storage[key] = value

    def __getitem__(self, item):
        return self.storage[item]

    def __getattr__(self, item):
        return self.storage[item]
