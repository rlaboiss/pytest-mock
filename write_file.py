class WriteFile:
    def __init__ (self, filename):
        self.filename = filename

    def write (self, content):
        with open(self.filename, "w") as f:
            return f.write(content)
