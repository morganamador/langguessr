from script import Script
from signclues import SignClue

def test_scripttest():
    armenian = Script("Armenian", 0x0530, 0x058F)
    assert armenian.contains("Ա") is True
    assert armenian.contains("A") is False


def test_signcluestest():
    Dur = SignClue("DUR", "Turkiye")
    assert Dur.cluematch("DUR") is True
    assert Dur.cluematch("stop") is False
    assert Dur.region == "Turkiye"