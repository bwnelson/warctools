
from hanzo.warctools.record import ArchiveRecord, ArchiveParser
from hanzo.warctools.warc import WarcParser
from hanzo.warctools.arc import ArcParser


class MixedRecord(ArchiveRecord):
    @classmethod
    def make_parser(self):
        return MixedParser()

class MixedParser(ArchiveParser):
    def __init__(self):
        self.arc = ArcParser()
        self.warc = WarcParser()

    def parse(self, stream, offset=None, line=None):
        if line is None:
            line = stream.readline()

        while line:
            if line.startswith(b'WARC'):
                return self.warc.parse(stream, offset, line=line)
            elif line not in (b'\n',b'\r\n',b'\r'):
                return self.arc.parse(stream, offset, line=line)

            line = stream.readline()
        return None, (), offset


