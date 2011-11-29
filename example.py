from NiceCommits import CommitExtractor

commit_message = """Just made this commit title the longest in the history of the world to try to pass 50 chars
This is the first line of the body.
And this is the second line of the body which can be of any length, even if it's ridiculously long.
"""
ce = CommitExtractor(commit_message)

print "%(title)s\n%(body)s" % ce.as_dict()
