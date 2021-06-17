from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
# import tensorflow as tf

def get_token(path):
    load_token = GPT2Tokenizer.from_pretrained(path)
    return load_token


def load_model(path):
    load_model = TFGPT2LMHeadModel.from_pretrained(path)
    # load_model = tf.keras.models.load_model('/model')
    return load_model


def make_predictions(scentence):
    tokenizer = get_token('./tokenizer')
    tokens = tokenizer.encode(scentence, return_tensors='tf')
    model = load_model('./model')
    output = model.generate(tokens,
                            max_length=1000,
                            top_k=30,
                            num_beams=5)
    actual_scentence = output
    return actual_scentence


def get_prediction(scentence):
    answer = make_predictions(scentence)
    return answer
