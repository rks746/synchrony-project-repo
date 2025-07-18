### 🔧 Configuration Required
> Before running the project, make sure to update the model path in `test_llm.py`.
This project uses the LLaMA 2 7B Chat GGUF model.

You can download the model from Hugging Face:
👉 TheBloke/LLaMA-2-7B-Chat-GGUF

Recommended file:
llama-2-7b-chat.Q4_K_M.gguf

Edit the line:

```python
llm = Llama(model_path="path/to/your/llama-model.gguf")
