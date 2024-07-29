# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )


class NmhGcl(KaitaiStruct):
    """doc"""

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x46\x4C\x43\x47":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x46\x4C\x43\x47", self.magic, self._io, "/seq/0"
            )
        self._unnamed1 = self._io.read_bytes(4)
        if not self._unnamed1 == b"\x01\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x01\x00\x00\x00", self._unnamed1, self._io, "/seq/1"
            )
        self._unnamed2 = self._io.read_bytes(4)
        if not self._unnamed2 == b"\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00", self._unnamed2, self._io, "/seq/2"
            )
        self.num_areas = self._io.read_u2be()
        self.num_materials = self._io.read_u2be()
        self.unk_1 = self._io.read_bytes(48)
        self.materials = []
        for i in range(self.num_materials):
            self.materials.append(NmhGcl.Material(self._io, self, self._root))

        self.area_headers = []
        for i in range(self.num_areas):
            self.area_headers.append(NmhGcl.AreaHeader(self._io, self, self._root))

        self._unnamed8 = NmhGcl.Align(32, self._io, self, self._root)
        self.areas = []
        for i in range(self.num_areas):
            self.areas.append(NmhGcl.Area(self._io, self, self._root))

    class AreaUnknown1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk_0 = self._io.read_u4be()
            self.unk_1 = self._io.read_u4be()
            self.unk_2 = self._io.read_u4be()
            self.unk_3 = self._io.read_u4be()
            self.unkf_0 = self._io.read_f4be()
            self.unkf_1 = self._io.read_f4be()
            self.unkf_2 = self._io.read_f4be()
            self.unkf_3 = self._io.read_f4be()

    class Area(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk4 = self._io.read_u4be()
            self.unk5 = self._io.read_u4be()
            self.num_unknown1s = self._io.read_u4be()
            self.num_unknown2s = self._io.read_u4be()
            self.bbox_min = NmhGcl.FlVector(self._io, self, self._root)
            self.bbox_max = NmhGcl.FlVector(self._io, self, self._root)
            self.unknown1s = []
            for i in range(self.num_unknown1s):
                self.unknown1s.append(NmhGcl.AreaUnknown1(self._io, self, self._root))

            self.unknown2s = []
            for i in range(self.num_unknown2s):
                self.unknown2s.append(NmhGcl.AreaUnknown2(self._io, self, self._root))

    class Align(KaitaiStruct):
        """Byte alignment"""

        def __init__(self, size, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.size = size
            self._read()

        def _read(self):
            self._unnamed0 = self._io.read_bytes(
                ((self.size - self._io.pos()) % self.size)
            )

    class AreaHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)
            ).decode("utf-8")
            self._unnamed1 = self._io.read_bytes(72)

    class Material(KaitaiStruct):
        """These are probably materials:
        The names are usually nondescriptive, but
        "LAMBERT1" sounds like a material.
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)
            ).decode("utf-8")
            self.unk0 = self._io.read_f4be()
            self._unnamed2 = self._io.read_bytes(20)

    class FlVector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4be()
            self.y = self._io.read_f4be()
            self.z = self._io.read_f4be()

    class AreaUnknown2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk_1 = self._io.read_u4be()
            self.unk_2 = self._io.read_u4be()
            self.unk_3 = self._io.read_u4be()
            self.v0 = NmhGcl.FlVector(self._io, self, self._root)
            self.v1 = NmhGcl.FlVector(self._io, self, self._root)
            self.v2 = NmhGcl.FlVector(self._io, self, self._root)
