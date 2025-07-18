from llama_cpp import Llama


model_path = "/home/karthik/.cache/huggingface/hub/models--TheBloke--CapybaraHermes-2.5-Mistral-7B-GGUF/snapshots/	8bea614edd9a2d5d9985a6e6c1ecc166261cacb8/capybarahermes-2.5-mistral-7b.Q2_K.gguf"


def get_commit(pr) :
	model = Llama(model_path=model_path, n_ctx=128, n_threads=4,n_batch=32,use_mlock=False,verbose=False)


	prompt = f"""You are an expert software engineer. Based on the following GitHub pull request details, generate a short, clear, and meaningful commit message that summarizes the changes.

Pull Request Title:
{pr['title']}

Pull Request Description:
{pr['body']}

Respond with only the commit message, no extra text.
"""

	output = model(prompt=prompt,max_tokens=256,temperature=0.5,top_k=50,top_p=0.9,stop=["</s>"])
	return output["choices"][0]["text"].strip()