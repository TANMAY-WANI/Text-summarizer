from textSummarizer.config.configuration import configuration_manager
from transformers import AutoTokenizer
from transformers import pipeline


class prediction_pipeline:
    def __init__(self) -> None:
        self.config = configuration_manager().get_evaluation_config()

    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)
        return output