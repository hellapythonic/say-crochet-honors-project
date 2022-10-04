class PatternError(Exception):
    """Thrown when a Pattern cannot be completely parsed."""
    malformed_pattern_error = "Malformed pattern. Check the pattern specification at \
        https://github.com/hellapythonic/say-crochet-honors-project for information on how to properly format \
        the JSON code for a say-crochet pattern."

    def __init__(self, message=malformed_pattern_error):
        self.message = message
        super().__init__(self.message)
