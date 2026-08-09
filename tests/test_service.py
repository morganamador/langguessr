from app.services import Services
import pytest

def test_id_countries():
    s = Services()
    ranked = s.id_countries('Straße gesperrt')
    assert ranked[0][0] == 'German'
    assert 'ß' in ranked[1][1]['unmatched']

def test_rank_countries():
    s = Services()
    results = s.rank_countries('Straße gesperrt')
    assert results[0][0] == 'Germany'
    assert results[1][0] == 'Austria'
    assert results[4][0] == 'United Kingdom'

def test_id_countries_rejects_numbers():
    s = Services()
    with pytest.raises(AttributeError):
        s.id_countries(1)