import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from subprocess import run
# run(["llamafactory-cli", "webchat", "--model_name_or_path", "models/Qwen2-0.5B-Medical-MLX", "--template", "qwen"])
run(["llamafactory-cli", "webui"])