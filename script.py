class Script:

    def __init__(self, scriptname: str, range_start: int, range_end: int):
        self.scriptname = scriptname
        self.range_start = range_start
        self.range_end = range_end
        #range = unicode range

    def contains(self, char: str) -> bool:
        return self.range_start <= ord(char) <= self.range_end