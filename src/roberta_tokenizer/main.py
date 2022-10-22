from .tokenizer import JapaneseTokenizer

class AutoTokenizer:
    def from_pretrained(lang="ja", version=None):
        kwargs = {}
        if version is not None:
            kwargs["version"] = version

        if lang == "ja":
            return JapaneseTokenizer(**kwargs)

        assert False, f"\"{lang}\" is not supported."
