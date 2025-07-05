import gradio as gr
import ollama

def generate_hindi_poem(user_prompt, max_tokens=200):
    # System prompt to set the Hindi poet persona
    system_prompt = (
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        "You are a poet who always writes poems in Hindi.\n<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n"
    )
    assistant_tag = "\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    full_prompt = system_prompt + user_prompt + assistant_tag

    response = ollama.generate(
        model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF",
        prompt=full_prompt,
        options={
            "temperature": 0.8,
            "num_predict": max_tokens
        }
    )
    return response['response']

with gr.Blocks(title="Hindi Poetry Generator") as demo:
    gr.Markdown(
        "# 🪔 Hindi Poetry Generator\n"
        "Enter an English prompt and get a Hindi poem!\n"
        "*(Powered by Llama 3.2 1B Instruct on Ollama)*"
    )
    with gr.Row():
        inp = gr.Textbox(
            label="Enter your poem topic or prompt (in English)",
            lines=2,
            placeholder="e.g., Write a poem about the beauty of the night sky."
        )
    with gr.Row():
        out = gr.Textbox(
            label="Generated Hindi Poem",
            lines=8
        )
    btn = gr.Button("Generate Poem")
    btn.click(fn=generate_hindi_poem, inputs=inp, outputs=out)

demo.launch()
