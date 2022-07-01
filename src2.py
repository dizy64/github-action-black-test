class InvalidClassName:
    def test(self):
        pass

    def internationalization_translate_method(
        self, internationalization_code: str, internationalization_message: str
    ) -> str:
        return internationalization_code + internationalization_message
