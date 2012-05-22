from NiceCommits import CommitExtractor

commit_message = """This is the title string
This is the first line of the body.
And this is the second line of the body
"""
commit_title = "This is the title string"
commit_body = """This is the first line of the body.
And this is the second line of the body"""

long_commit_message = """This is the title string which can be of any length, even if it's ridiculously long.
This is the first line of the body.
"""
long_commit_title = "This is the title string which can be of any le..."

# Create instance
ce = CommitExtractor(commit_message)


def test_commit_extractor_get_title():
    assert ce.get_title() == commit_title


def test_commit_extractor_get_body():
    assert ce.get_body() == commit_body


def test_commit_extractor_as_dict():
    assert type(ce.as_dict()) is dict
    assert ce.as_dict()['title'] == commit_title
    assert ce.as_dict()['body'] == commit_body


def test_title_should_trucate_at_fifty_chars():
    ce2 = CommitExtractor(long_commit_message)
    assert len(ce2.get_title()) == 50
    assert ce2.get_title() == long_commit_title
