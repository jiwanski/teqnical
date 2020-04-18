from classes.home03 import home0303 as home


def test_band_contains_key():
    assert 'active' in home.band.keys()


def test_new_album_added():
    assert home.band['albums'][-1] == 'Cracks And Lines'


def test_active_reverted():
    assert home.band['active'] is True


def test_sold_albums_incremented():
    assert home.band['albums_sold'] == 15928
