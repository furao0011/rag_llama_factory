# from modelscope import snapshot_download
# local_dir = './models/Qwen2-0.5B-Medical-MLX'
# model_dir = snapshot_download('maple77/Qwen2-0.5B-Medical-MLX', local_dir=local_dir)
# print(f"Model downloaded to {model_dir}")
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("models/Qwen2-0.5B-Medical-MLX")
model = AutoModelForCausalLM.from_pretrained("models/Qwen2-0.5B-Medical-MLX", device_map={"":0})

prompt = "医生您好，我最近脖子疼。"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
device = 'cuda'
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate( model_inputs.input_ids, max_new_tokens=512)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)