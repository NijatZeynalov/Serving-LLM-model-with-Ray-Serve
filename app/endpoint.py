import ray

class Endpoint:
    def __init__(self, chat_handle, translate_en_az_handle, translate_az_en_handle):
        self.chat_handle = chat_handle
        self.en_az_handle = translate_en_az_handle
        self.az_en_handle = translate_az_en_handle

    def get_response(self, user_input: str):
        history = []
        translated_input_handle = self.az_en_handle.get_response.remote(user_input)
        translated_input = ray.get(translated_input_handle)
        response_en_handle = self.chat_handle.get_response.remote(translated_input, history)
        response_en = ray.get(response_en_handle)
        translated_response_handle = self.en_az_handle.get_response.remote(response_en)
        translated_response = ray.get(translated_response_handle)
        return translated_response
