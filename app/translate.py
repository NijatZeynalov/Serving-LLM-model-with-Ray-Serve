from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translate:
    def __init__(self, src_lang: str, trg_lang: str):
        self.src_lang = src_lang
        self.trg_lang = trg_lang

    def get_response(self, user_input: str) -> str:
        tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", src_lang=self.src_lang)
        model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
        inputs = tokenizer(user_input, return_tensors="pt")
        translated_tokens = model.generate(
            **inputs, forced_bos_token_id=tokenizer.lang_code_to_id[self.trg_lang], max_length=200
        )
        translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        return translation
