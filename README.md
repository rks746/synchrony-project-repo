This project is a Smart PR Review Assistant that uses a local large language model (LLM) to generate better commit messages from GitHub Pull Request (PR) descriptions. When a PR is opened or updated, a GitHub Webhook sends the PR data to a local Flask server. The server extracts relevant information from the PR (like title, body, and changed files) and passes it to a lightweight LLM (CapybaraHermes-2.5 Mistral-7B in GGUF format) using the llama-cpp-python library. The LLM then returns a suggested commit message based on the PR content.

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
