from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from ocr import cleaned_text
import torch

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
question_answer = pipeline("question-answering", model="deepset/roberta-base-squad2")

model_name = "facebook/bart-large-cnn"

model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
quantized_model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)

text = cleaned_text()
summary = quantized_model(text, max_length=130, min_length=30, do_sample=False)

print(summary[0])
# summary = summarizer(text, max_length=130, min_length=30, do_sample=False)


# print("Summary: ", summary[0]["summary_text"])


# context = summary[0]["summary_text"]

# question = "What is the name of the person in the document?"

# answer = question_answer(question=question, context=context)


# print("Answer: ", answer["answer"])


