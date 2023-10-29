import fitz  # PyMuPDF
import re
import os
import dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import langchain
from md2pdf.core import md2pdf
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

dotenv.load_dotenv(".env")

template = """
You are a multi-lingual law expert and assistant. Translate this text to English :
{text}
"""
prompt = PromptTemplate(
    template=template,
    input_variables=[
        "text"
    ],
)

llm = ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo-16k")

translation_chain = LLMChain(prompt=prompt, llm=llm)

# translated_text = translation_chain.run(
#     text = "El procedimiento penal contra el demandante en relación con estas declaraciones"
# )
# print(translated_text)

def translate(chunk, src_lang):
  print("Translate", chunk)
  translated_text = translation_chain.run(
      text = chunk
  )
  return translated_text


SAMPLE_PDFS = "sample_pdfs"
OUT_DIR = "output_pdfs"


def split_into_paragraphs(text, max_paragraph_length=300):
    # Define the regular expression pattern to match sentences.
    sentence_pattern = r'(?<=[.!?])\s+'

    # Split the text into sentences.
    sentences = re.split(sentence_pattern, text)

    # Initialize variables to track paragraph length and store paragraphs.
    current_paragraph = ''
    paragraphs = []

    for sentence in sentences:
        # Add the current sentence to the current paragraph.
        current_paragraph += sentence

        # If the paragraph length exceeds the maximum allowed length, start a new paragraph.
        if len(current_paragraph) >= max_paragraph_length:
            # Start a new paragraph and add the current sentence to it.
            paragraphs.append(current_paragraph)
            current_paragraph = ''

        # If the sentence is the last one, or if it's the last sentence in the text, add the current paragraph.
        elif sentence == sentences[-1]:
            paragraphs.append(current_paragraph)

    return '\n<br/><br/><br/>\n'.join(paragraphs)

def create_pdf_from_markdown(markdown_text, pdf_file_path):
  md2pdf(
    pdf_file_path,
    md_content=markdown_text,
    css_file_path="style.css",
  )
  return pdf_file_path

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def split_text(text, max_size=2000):
  chunks = []
  start_idx = 0
  while start_idx < len(text):
    end_idx = min(start_idx + max_size, len(text))
    chunk = text[start_idx:end_idx]
    chunks.append(chunk)
    start_idx = end_idx
  return chunks

def merge_chunks(chunks):
  merged_text = ""
  for chunk in chunks:
    merged_text += chunk
  return merged_text

def translate_chunks(chunks, src_lang):
  translated_chunks = []
  cid=0
  for chunk in chunks:
    if cid % 5 == 0:
        print(f"Processed {cid} chunks")
    cid = cid+1
    translation = translate(chunk, src_lang)
    print("Translation -")
    print(translation)
    translated_chunks.append(translation)
  return translated_chunks

def process_pdf(pdf_path, out_path, src_lang):
  text = extract_text_from_pdf(pdf_path)
  # Save the extracted text to a file.
  with open("extracted_text.txt", "w", encoding="utf-8") as f:
      f.write(text)
        
  chunks = split_text(text)
  print(f"Divided into {len(chunks)} chunks")
    
  translated_chunks = translate_chunks(chunks, src_lang)
  print(f"Translated chunks")
    
  translated_text = merge_chunks(translated_chunks)
  translated_text = split_into_paragraphs(translated_text)
    
  # Save the translated text to a file.
  with open("translated_text.txt", "w", encoding="utf-8") as f:
      f.write(translated_text)
  print(f"Translated text: {len(translated_text)} chars")

  translated_pdf_path = create_pdf_from_markdown(translated_text, out_path)
  print(f"PDF saved to {translated_pdf_path}")

data = [
    {"name": "AFFAIRE Aak turkiye.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE AVCIOgLU c turkiye.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE CP ET MN c FRANCE.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE JALOUD c PAYS-BAS.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE KARACSONY ET AUTRES c HONGRIE.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE KHAMTOKHU ET AKSENCHIK c RUSSIE.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE KOILOVA ET BABULKOVA c BULGARIE.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE MARGUS c CROATIE.pdf", "lang": "fr_XX"},
    {
        "name": "AFFAIRE POMUL SRL ET SUBERVIN SRL c REPUBLIQUE DE MOLDOVA.pdf",
        "lang": "fr_XX",
    },
    {"name": "AFFAIRE STOIANOGLO c REPUBLIQUE DE MOLDOVA.pdf", "lang": "fr_XX"},
    {"name": "AFFAIRE ZUBAC c CROATIE.pdf", "lang": "fr_XX"},
    {"name": "CASE OF ANAGNOSTAKIS v GREECE.pdf", "lang": "en_XX"},
    {"name": "CASE OF BIAO v DENMARK.pdf", "lang": "en_XX"},
    {"name": "CASE OF CREDIT EUROPE LEASING IFN SA v ROMANIA.pdf", "lang": "en_XX"},
    {"name": "CASE OF HOVHANNISYAN AND KARAPETYAN v ARMENIA.pdf", "lang": "en_XX"},
    {
        "name": "CASE OF INTERNATIONALE HUMANITARE HILFSORGANISATION E Vs GERMANY.pdf",
        "lang": "en_XX",
    },
    {"name": "CASE OF KURT v AUSTRIA.pdf", "lang": "en_XX"},
    {"name": "CASE OF MURTAZALIYEVA v RUSSIA.pdf", "lang": "en_XX"},
    {"name": "CASE OF PERINCEK vs SWITZERLAND - spanish.pdf", "lang": "es_XX"},
    {"name": "CASE_OF_FRAGOSO_DACOSTAvSPAIN_spansish.pdf", "lang": "es_XX"},
]

for item in data:
    if item["lang"] != "en_XX" and item["lang"] != "fr_XX":
        pdf_name = item["name"]
        pdf_path = os.path.join(SAMPLE_PDFS, pdf_name)
        out_path = os.path.join(OUT_DIR, pdf_name)

        print(f"Process {pdf_path}({item['lang']}) -> {out_path}")
        process_pdf(
            pdf_path,
            out_path,
            item['lang']
        )
    else :
        print(f"Ignore {item['name']}")