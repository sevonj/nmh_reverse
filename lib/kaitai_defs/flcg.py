# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )


class Flcg(KaitaiStruct):
    """FLCG
    No More Heroes World Collisions
    One distance unit appears to be 10m.
    """

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
        self.unk_1 = self._io.read_u4be()
        self.unk_2 = self._io.read_u4be()
        self.unk_3 = self._io.read_u4be()
        self._unnamed8 = self._io.read_bytes(4)
        if not self._unnamed8 == b"\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00", self._unnamed8, self._io, "/seq/8"
            )
        self._unnamed9 = self._io.read_bytes(16)
        if (
            not self._unnamed9
            == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        ):
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed9,
                self._io,
                "/seq/9",
            )
        self._unnamed10 = self._io.read_bytes(16)
        if (
            not self._unnamed10
            == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        ):
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed10,
                self._io,
                "/seq/10",
            )
        self.materials = []
        for i in range(self.num_materials):
            self.materials.append(Flcg.Material(self._io, self, self._root))

        self.areas = []
        for i in range(self.num_areas):
            self.areas.append(Flcg.Area(self._io, self, self._root))

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
            self._unnamed2 = self._io.read_bytes(4)
            if not self._unnamed2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00",
                    self._unnamed2,
                    self._io,
                    "/types/material/seq/2",
                )
            self._unnamed3 = self._io.read_bytes(16)
            if (
                not self._unnamed3
                == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            ):
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                    self._unnamed3,
                    self._io,
                    "/types/material/seq/3",
                )

    class Area(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)
            ).decode("utf-8")
            self.unkf_0 = self._io.read_f4be()
            self.unk_1 = self._io.read_u4be()
            self._unnamed3 = self._io.read_bytes(8)
            if not self._unnamed3 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00\x00\x00\x00\x00",
                    self._unnamed3,
                    self._io,
                    "/types/area/seq/3",
                )
            self.unk_2 = self._io.read_u4be()
            self.unk_3 = self._io.read_u4be()
            self.origin = Flcg.FlVector(self._io, self, self._root)
            self._unnamed7 = self._io.read_bytes(4)
            if not self._unnamed7 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00", self._unnamed7, self._io, "/types/area/seq/7"
                )
            self.unkf_4 = self._io.read_f4be()
            self._unnamed9 = self._io.read_bytes(4)
            if not self._unnamed9 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00", self._unnamed9, self._io, "/types/area/seq/9"
                )
            self.off_data = self._io.read_u4be()
            self._unnamed11 = self._io.read_bytes(4)
            if not self._unnamed11 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00", self._unnamed11, self._io, "/types/area/seq/11"
                )
            self._unnamed12 = self._io.read_bytes(16)
            if (
                not self._unnamed12
                == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            ):
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                    self._unnamed12,
                    self._io,
                    "/types/area/seq/12",
                )

        class AreaData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.off_data1 = self._io.read_u4be()
                self.off_colmesh = self._io.read_u4be()
                self.num_data1 = self._io.read_u4be()
                self.num_col_tris = self._io.read_u4be()
                self.unk_vec_a = Flcg.FlVector(self._io, self, self._root)
                self.unk_vec_b = Flcg.FlVector(self._io, self, self._root)

            class Data1(KaitaiStruct):
                """Contains references to collision tris."""

                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.off_a = self._io.read_u4be()
                    self.off_b = self._io.read_u4be()
                    self.off_col_tri = self._io.read_u4be()
                    self.unk_3 = self._io.read_u4be()
                    self.unkf_0 = self._io.read_f4be()
                    self.unkf_1 = self._io.read_f4be()
                    self.unkf_2 = self._io.read_f4be()
                    self.unkf_3 = self._io.read_f4be()

            class ColTri(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.off_next = self._io.read_u4be()
                    self._unnamed1 = self._io.read_bytes(4)
                    if not self._unnamed1 == b"\x00\x00\x00\x00":
                        raise kaitaistruct.ValidationNotEqualError(
                            b"\x00\x00\x00\x00",
                            self._unnamed1,
                            self._io,
                            "/types/area/types/area_data/types/col_tri/seq/1",
                        )
                    self.unk_3 = self._io.read_u4be()
                    self.v0 = Flcg.FlVector(self._io, self, self._root)
                    self.v1 = Flcg.FlVector(self._io, self, self._root)
                    self.v2 = Flcg.FlVector(self._io, self, self._root)

            @property
            def data1(self):
                if hasattr(self, "_m_data1"):
                    return self._m_data1

                io = self._root._io
                _pos = io.pos()
                io.seek(self.off_data1)
                self._m_data1 = []
                for i in range(self.num_data1):
                    self._m_data1.append(Flcg.Area.AreaData.Data1(io, self, self._root))

                io.seek(_pos)
                return getattr(self, "_m_data1", None)

            @property
            def col_mesh(self):
                if hasattr(self, "_m_col_mesh"):
                    return self._m_col_mesh

                io = self._root._io
                _pos = io.pos()
                io.seek(self.off_colmesh)
                self._m_col_mesh = []
                for i in range(self.num_col_tris):
                    self._m_col_mesh.append(
                        Flcg.Area.AreaData.ColTri(io, self, self._root)
                    )

                io.seek(_pos)
                return getattr(self, "_m_col_mesh", None)

        @property
        def data(self):
            if hasattr(self, "_m_data"):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.off_data)
            self._m_data = Flcg.Area.AreaData(io, self, self._root)
            io.seek(_pos)
            return getattr(self, "_m_data", None)
