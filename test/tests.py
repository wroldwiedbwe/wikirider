from wikirider import WikiRider


def test_wiki_url():
    test_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    is_url_valid = WikiRider.valid_url(test_url)
    assert is_url_valid is True


def test_non_wiki_url():
    test_url = 'https://www.google.com'
    is_url_valid = WikiRider.valid_url(test_url)
    assert is_url_valid is False


def test_is_returning_acurate_quantity_of_links():
    rider = WikiRider('https://en.wikipedia.org/wiki/Python_(programming_language)', 5)
    results = []
    results += rider.run()
    assert len(results) is 5
