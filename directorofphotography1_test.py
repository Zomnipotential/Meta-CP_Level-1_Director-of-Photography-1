import pytest
import directorofphotography1 as dop

def test_getArtisticPhotographCount(nr_cells, positions, min_dist, max_dist, nr_photographs):
    assert dop.getArtisticPhotographCount(nr_cells, positions, min_dist, max_dist) == nr_photographs

test_getArtisticPhotographCount(5, 'APABA', 1, 2, 1)
test_getArtisticPhotographCount(5, 'APABA', 2, 3, 0)
test_getArtisticPhotographCount(8, '.PBAAP.B', 1, 3, 3)
