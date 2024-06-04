import ray
from typing import Dict
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from fastapi import Request
import json

class Chat:
    def __init__(self, model: str):
        self._tokenizer = AutoTokenizer.from_pretrained(model)
        self._model = AutoModelForSeq2SeqLM.from_pretrained(model).to(0)

    async def __call__(self, request: Request) -> Dict:
        data = await request.json()
        data = json.loads(data)
        return {'response': self.get_response(data['user_input'], data['history']) }

    def get_response(self, user_input: str, history: list[str]) -> str:
        history.append(user_input)
        inputs = self._tokenizer('</s><s>'.join(history), return_tensors='pt').to(0)
        reply_ids = self._model.generate(**inputs, max_new_tokens=500)
        response = self._tokenizer.batch_decode(reply_ids.cpu(), skip_special_tokens=True)[0]
        return response
