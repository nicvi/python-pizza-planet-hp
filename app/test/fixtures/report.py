
import pytest

from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string)


import pytest


@pytest.fixture
def report_uri():
    return '/report/'