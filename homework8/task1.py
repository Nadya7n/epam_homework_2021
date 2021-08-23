class KeyValueStorage:
    def __init__(self, path_to_file, storage=None):
        self.path_to_file = path_to_file
        self.storage = storage or dict()

        with open(path_to_file) as fh:
            for line in fh:
                key, value = line.strip().split("=")
                if key in self.storage:
                    raise ValueError(f"Value - {key} - already in storage")
                else:
                    self.storage[key] = value

    def __getitem__(self, item):
        return self.storage[item]

    def __getattr__(self, item):
        return self.storage[item]
