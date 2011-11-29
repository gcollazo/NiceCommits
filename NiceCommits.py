class CommitExtractor:
    def __init__(self, commit_text):
        self.commit_text = commit_text
    
    def get_title(self):
        full_title = self.commit_text.split("\n")[0].rstrip().lstrip()
        if len(full_title) > 50:
            return "%s..." % full_title[:47].rstrip()
        else:
            return full_title
    
    def get_body(self):
        return "\n".join(self.commit_text.split("\n")[1:]).rstrip().lstrip()
    
    def as_dict(self):
        return {'title': self.get_title(), 'body': self.get_body()}


class InvalidCommitText(Exception):
    def __str__(self):
        return "Reference: http://git.io/VjMyoQ"
