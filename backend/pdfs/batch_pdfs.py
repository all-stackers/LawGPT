import os
import json
import dotenv
import w3storage

dotenv.load_dotenv(".env")
w3 = w3storage.API(token=os.environ.get('WEB3STORAGE_API_KEY'))

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

ORIGINAL_DIR = "sample_pdfs"
OUTPUT_DIR = "output_pdfs"

def cid_to_url(cid):
    return f"https://{cid}.ipfs.dweb.link"

result = []

with open('pdfs.json', 'w') as f:
    json.dump(result, f)

for pdf in data:
    pdf_name = pdf["name"]

    orignal_pdf_path = os.path.join(ORIGINAL_DIR, pdf_name)
    translated_pdf_path = os.path.join(OUTPUT_DIR, pdf_name)

    original_file_cid = w3.post_upload((pdf_name, open(orignal_pdf_path, 'rb')))
    original_file_url = cid_to_url(original_file_cid)
    # print(original_file_url)

    translated_file_cid = w3.post_upload((pdf_name, open(translated_pdf_path, 'rb')))
    translated_file_url = cid_to_url(translated_file_cid)
    # print(translated_file_url)

    result.append({
        'pdf_name': pdf_name,
        'original_file_cid': original_file_cid,
        'original_file_url': original_file_url,
        'translated_file_cid': translated_file_cid,
        'translated_file_url': translated_file_url
    })

print(result)
with open('pdfs.json', 'w') as f:
    json.dump(result, f)