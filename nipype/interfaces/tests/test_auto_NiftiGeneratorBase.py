# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dcmstack import NiftiGeneratorBase


def test_NiftiGeneratorBase_inputs():
    input_map = dict()
    inputs = NiftiGeneratorBase.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
