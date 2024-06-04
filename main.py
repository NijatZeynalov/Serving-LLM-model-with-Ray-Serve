import ray
from ray import serve
from app.chat import Chat
from app.translate import Translate
from app.endpoint import Endpoint

ray.init(num_cpus=16, num_gpus=1)

chat = Chat.bind(model='facebook/blenderbot-400M-distill')
translate_en_az = Translate.bind(src_lang="eng_Latn", trg_lang="azj_Latn")
translate_az_en = Translate.bind(src_lang="azj_Latn", trg_lang="eng_Latn")

en_az_handle = serve.run(translate_en_az, name='en-az')
chat_handle = serve.run(chat, name='basic_chat')
az_en_handle = serve.run(translate_az_en, name='az-en')

endpoint = Endpoint.bind(chat_handle, en_az_handle, az_en_handle)
endpoint_handle = serve.run(endpoint, name='multilingual_chat')

if __name__ == "__main__":
    message = input("Enter your message: ")
    history = []

    endpoint_result = endpoint_handle.get_response.remote(message)
    output = ray.get(endpoint_result)
    print("Response:", output)
