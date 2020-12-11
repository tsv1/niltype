from typing import Union

from pytest import raises

from niltype import Nil, Nilable, NilType


def test_nil_str():
    assert str(Nil) == "Nil"


def test_nil_repr():
    assert repr(Nil) == "Nil"


def test_bool():
    assert not Nil


def test_nil_isinstance():
    assert isinstance(Nil, NilType)
    assert not isinstance(Nil, type(None))


def test_nil_type():
    assert type(Nil) is NilType


def test_nil_identity():
    assert Nil is Nil
    assert Nil is not None


def test_nil_eq():
    assert Nil == Nil
    assert (Nil == "Nil") is False


def test_nil_ne():
    assert (Nil != Nil) is False
    assert Nil != "Nil"


def test_setattr():
    with raises(Exception) as e:
        Nil.attr = None
    assert str(e.value) == "'NilType' object has no attribute 'attr'"


def test_call():
    with raises(TypeError) as e:
        Nil()
    assert str(e.value) == "'NilType' object is not callable"


def test_final():
    with raises(TypeError) as e:
        class _NilType(NilType):
            pass
    assert e.type is TypeError


def test_nilable():
    assert Nilable[int] == Union[int, NilType]
