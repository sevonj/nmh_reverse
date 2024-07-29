# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )


class NmhGm2(KaitaiStruct):
    """Grasshopper Manufacture
    No More Heroes world chunk
    GMF - Grasshopper Model File?
    Japanese text encoding.
    """

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x47\x4D\x46\x32":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x47\x4D\x46\x32", self.magic, self._io, "/seq/0"
            )
        self.version = self._io.read_u4le()
        if not self.version == 2:
            raise kaitaistruct.ValidationNotEqualError(
                2, self.version, self._io, "/seq/1"
            )
        self._unnamed2 = self._io.read_bytes(16)
        if (
            not self._unnamed2
            == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        ):
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed2,
                self._io,
                "/seq/2",
            )
        self.num_objects = self._io.read_u2le()
        self.num_textures = self._io.read_u2le()
        self._unnamed5 = self._io.read_bytes(2)
        if not self._unnamed5 == b"\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00", self._unnamed5, self._io, "/seq/5"
            )
        self.num_materials = self._io.read_u2le()
        self.unk_4 = self._io.read_u4le()
        self.unk_5 = self._io.read_u4le()
        self._unnamed9 = self._io.read_bytes(4)
        if not self._unnamed9 == b"\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00", self._unnamed9, self._io, "/seq/9"
            )
        self.unk_7 = self._io.read_u4le()
        self.unk_8 = self._io.read_u4le()
        self.unk_9 = self._io.read_u4le()
        self._unnamed13 = self._io.read_bytes(16)
        if (
            not self._unnamed13
            == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        ):
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed13,
                self._io,
                "/seq/13",
            )
        self._unnamed14 = self._io.read_bytes(16)
        if (
            not self._unnamed14
            == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        ):
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed14,
                self._io,
                "/seq/14",
            )
        self._unnamed15 = self._io.read_bytes(16)
        if (
            not self._unnamed15
            == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        ):
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed15,
                self._io,
                "/seq/15",
            )
        self._unnamed16 = self._io.read_bytes(8)
        if not self._unnamed16 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x00\x00\x00\x00\x00\x00\x00\x00",
                self._unnamed16,
                self._io,
                "/seq/16",
            )
        self.textures = []
        for i in range(self.num_textures):
            self.textures.append(NmhGm2.Texture(self._io, self, self._root))

        self.materials = []
        for i in range(self.num_materials):
            self.materials.append(NmhGm2.Material(self._io, self, self._root))

        self.world_objects = []
        for i in range(self.num_objects):
            self.world_objects.append(NmhGm2.WorldObject(self._io, self, self._root))

    class WorldObject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)
            ).decode("SHIFT-JIS")
            self.unk_0 = self._io.read_u4le()
            self.off_i_buf = self._io.read_u4le()
            self.unk_2 = self._io.read_u4le()
            self.unk_3 = self._io.read_u4le()
            self.unk_4 = self._io.read_u4le()
            self.unk_5 = self._io.read_u4le()
            self.offset_surf_list = self._io.read_u4le()
            self._unnamed8 = self._io.read_bytes(4)
            if not self._unnamed8 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00",
                    self._unnamed8,
                    self._io,
                    "/types/world_object/seq/8",
                )
            self._unnamed9 = self._io.read_bytes(4)
            if not self._unnamed9 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00",
                    self._unnamed9,
                    self._io,
                    "/types/world_object/seq/9",
                )
            self.unk_7 = self._io.read_u4le()
            self.origin = NmhGm2.FlVector(self._io, self, self._root)
            self.unkf_a = self._io.read_f4le()
            self.unk_b = self._io.read_u4le()
            self.unkf_c = self._io.read_f4le()
            self.unkf_d = self._io.read_f4le()
            self.unkf_e = self._io.read_f4le()
            self.unkf_f = self._io.read_f4le()
            self.unkf_10 = self._io.read_f4le()
            self.unkf_11 = self._io.read_f4le()
            self.offset_c = self._io.read_u4le()
            self.unkf_13 = self._io.read_f4le()
            self.unkf_14 = self._io.read_f4le()
            self.unkf_15 = self._io.read_f4le()
            self.unkf_16 = self._io.read_f4le()
            self.unkf_17 = self._io.read_f4le()
            self.unkf_18 = self._io.read_f4le()
            self.unkf_19 = self._io.read_f4le()
            self.unkf_1a = self._io.read_f4le()

        class Surface(KaitaiStruct):
            """Headers are in a linked list."""

            def __init__(self, off_buf_b, data_c, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.off_buf_b = off_buf_b
                self.data_c = data_c
                self._read()

            def _read(self):
                self.prev_offset = self._io.read_u4le()
                self.next_offset = self._io.read_u4le()
                self.data_offset = self._io.read_u4le()
                self.unk_3 = self._io.read_u4le()
                self.unk_4 = self._io.read_u2le()
                self.num_i = self._io.read_u2le()
                self._unnamed6 = self._io.read_bytes(4)
                if not self._unnamed6 == b"\x00\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(
                        b"\x00\x00\x00\x00",
                        self._unnamed6,
                        self._io,
                        "/types/world_object/types/surface/seq/6",
                    )
                self.unk_6 = self._io.read_u2le()
                self.unk_7 = self._io.read_u2le()
                self.unk_8 = self._io.read_u2le()
                self.unk_9 = self._io.read_u2le()

            class BufA(KaitaiStruct):
                def __init__(self, off_buf_b, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.off_buf_b = off_buf_b
                    self._read()

                def _read(self):
                    self.data_size = self._io.read_u4be()
                    self.num_v_smthn_total = self._io.read_u2be()
                    self.unk_2 = self._io.read_u2be()
                    self._unnamed3 = self._io.read_bytes(8)
                    if not self._unnamed3 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                        raise kaitaistruct.ValidationNotEqualError(
                            b"\x00\x00\x00\x00\x00\x00\x00\x00",
                            self._unnamed3,
                            self._io,
                            "/types/world_object/types/surface/types/buf_a/seq/3",
                        )
                    self._unnamed4 = self._io.read_bytes(16)
                    if (
                        not self._unnamed4
                        == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    ):
                        raise kaitaistruct.ValidationNotEqualError(
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
                            self._unnamed4,
                            self._io,
                            "/types/world_object/types/surface/types/buf_a/seq/4",
                        )
                    self.vs = []
                    i = 0
                    while True:
                        _ = NmhGm2.WorldObject.Surface.Face(
                            self.off_buf_b, self._io, self, self._root
                        )
                        self.vs.append(_)
                        if _.unk_0 == 0:
                            break
                        i += 1

            class Face(KaitaiStruct):
                def __init__(self, off_buf_b, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self.off_buf_b = off_buf_b
                    self._read()

                def _read(self):
                    self.unk_0 = self._io.read_u2be()
                    if self.unk_0 == 153:
                        self.num_smthn = self._io.read_u2be()

                    if self.unk_0 == 153:
                        self.unk_1 = []
                        for i in range(self.num_smthn):
                            self.unk_1.append(
                                NmhGm2.WorldObject.Surface.Face.V(
                                    self.off_buf_b, self._io, self, self._root
                                )
                            )

                class V(KaitaiStruct):
                    def __init__(self, off_buf_b, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self.off_buf_b = off_buf_b
                        self._read()

                    def _read(self):
                        self.idx = self._io.read_u2be()
                        self.unk = self._io.read_bytes(9)

                    @property
                    def data_b(self):
                        if hasattr(self, "_m_data_b"):
                            return self._m_data_b

                        io = self._root._io
                        _pos = io.pos()
                        io.seek((self.off_buf_b + (self.idx * 6)))
                        self._m_data_b = io.read_bytes(6)
                        io.seek(_pos)
                        return getattr(self, "_m_data_b", None)

            @property
            def buf_a(self):
                if hasattr(self, "_m_buf_a"):
                    return self._m_buf_a

                io = self._root._io
                _pos = io.pos()
                io.seek(self.data_offset)
                self._m_buf_a = NmhGm2.WorldObject.Surface.BufA(
                    self.off_buf_b, io, self, self._root
                )
                io.seek(_pos)
                return getattr(self, "_m_buf_a", None)

            @property
            def buf_b(self):
                if hasattr(self, "_m_buf_b"):
                    return self._m_buf_b

                io = self._root._io
                _pos = io.pos()
                io.seek(self.off_buf_b)
                self._m_buf_b = []
                for i in range(self.num_i):
                    self._m_buf_b.append(io.read_bytes(6))

                io.seek(_pos)
                return getattr(self, "_m_buf_b", None)

        @property
        def data_c(self):
            if hasattr(self, "_m_data_c"):
                return self._m_data_c

            if self.offset_c != 1065353216:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset_c)
                self._m_data_c = io.read_bytes(6)
                io.seek(_pos)

            return getattr(self, "_m_data_c", None)

        @property
        def surfaces(self):
            if hasattr(self, "_m_surfaces"):
                return self._m_surfaces

            if self.offset_surf_list != 0:
                io = self._root._io
                _pos = io.pos()
                io.seek(self.offset_surf_list)
                self._m_surfaces = []
                i = 0
                while True:
                    _ = NmhGm2.WorldObject.Surface(
                        self.off_i_buf, self.data_c, io, self, self._root
                    )
                    self._m_surfaces.append(_)
                    if _.next_offset == 0:
                        break
                    i += 1
                io.seek(_pos)

            return getattr(self, "_m_surfaces", None)

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

    class Material(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)
            ).decode("SHIFT-JIS")
            self.unk_0 = self._io.read_u4le()
            self.unk_2 = self._io.read_u4le()
            self.unk_3 = self._io.read_u4le()
            self.offset = self._io.read_u4le()
            self._unnamed5 = self._io.read_bytes(4)
            if not self._unnamed5 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00",
                    self._unnamed5,
                    self._io,
                    "/types/material/seq/5",
                )
            self._unnamed6 = self._io.read_bytes(4)
            if not self._unnamed6 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00",
                    self._unnamed6,
                    self._io,
                    "/types/material/seq/6",
                )

        class MaterialData(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self._unnamed0 = self._io.read_bytes(4)
                if not self._unnamed0 == b"\x00\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(
                        b"\x00\x00\x00\x00",
                        self._unnamed0,
                        self._io,
                        "/types/material/types/material_data/seq/0",
                    )
                self._unnamed1 = self._io.read_bytes(4)
                if not self._unnamed1 == b"\x00\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(
                        b"\x00\x00\x00\x00",
                        self._unnamed1,
                        self._io,
                        "/types/material/types/material_data/seq/1",
                    )
                self.unk_2 = self._io.read_u4le()
                self.unk_3 = self._io.read_u4le()
                self.unkf_4 = self._io.read_f4le()
                self.unkf_5 = self._io.read_f4le()
                self.unkf_6 = self._io.read_f4le()
                self.unkf_7 = self._io.read_f4le()
                self.unkf_8 = self._io.read_f4le()
                self.unkf_9 = self._io.read_f4le()
                self.unkf_a = self._io.read_f4le()
                self.unkf_b = self._io.read_f4le()

        @property
        def data(self):
            if hasattr(self, "_m_data"):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._m_data = NmhGm2.Material.MaterialData(io, self, self._root)
            io.seek(_pos)
            return getattr(self, "_m_data", None)

    class FlVector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()

    class Texture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (
                KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)
            ).decode("SHIFT-JIS")
            self.unk_0 = self._io.read_u4le()
            self.unk_1 = self._io.read_u4le()
            self.offset = self._io.read_u4le()
            self._unnamed4 = self._io.read_bytes(4)
            if not self._unnamed4 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x00\x00\x00\x00",
                    self._unnamed4,
                    self._io,
                    "/types/texture/seq/4",
                )
            self.size = self._io.read_u4le()
            self.unk_5 = self._io.read_u4le()

        @property
        def data_magic(self):
            """Just to be extra sure."""
            if hasattr(self, "_m_data_magic"):
                return self._m_data_magic

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._m_data_magic = io.read_bytes(4)
            io.seek(_pos)
            return getattr(self, "_m_data_magic", None)

        @property
        def data(self):
            """GHM in-house texture format."""
            if hasattr(self, "_m_data"):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._m_data = io.read_bytes(self.size)
            io.seek(_pos)
            return getattr(self, "_m_data", None)
