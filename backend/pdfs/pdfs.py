import os
import json
import dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
from md2pdf.core import md2pdf
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

dotenv.load_dotenv(".env")
OUT_PATH = "output_pdfs"

config = cloudinary.config(secure=True, cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"), api_key=os.getenv("CLOUDINARY_API_KEY"), api_secret=os.getenv("CLOUDINARY_API_SECRET"))

def upload_pdf_to_cloudinary(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        response = cloudinary.uploader.upload(f, resource_type="raw")
    return response["secure_url"]

def create_pdf_from_markdown(markdown_text, filename):
  pdf_file_path = os.path.join(OUT_PATH, filename)

  md2pdf(
    pdf_file_path,
    md_content=markdown_text,
    css_file_path="style.css",
  )
  
  return pdf_file_path

def create_multiple_pdfs_from_markdowns(markdowns):
    results = []
    for markdown in markdowns:
        pdf_path = create_pdf_from_markdown(markdown['markdown_text'], markdown['filename'])
        results.append({
            'file': pdf_path,
            'cloudinary_url': upload_pdf_to_cloudinary(pdf_path),
        })
    return results

markdowns = [
    {
        'markdown_text': """---
__Advertisement :)__

- __[pica](https://nodeca.github.io/pica/demo/)__ - high quality and fast image
  resize in browser.
- __[babelfish](https://github.com/nodeca/babelfish/)__ - developer friendly
  i18n with plurals support and easy syntax.

You will like those projects!

---

# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


## Horizontal Rules

___

---

***


## Typographic replacements

Enable typographer option to see result.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,,  -- ---

"Smartypants, double quotes" and 'single quotes'


## Emphasis

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~


## Blockquotes


> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.


## Lists

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar


## Code

Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


Block code "fences"

```
Sample text here...
```

Syntax highlighting

``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


## Links

[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")

Autoconverted link https://github.com/nodeca/pica (enable linkify to see)


## Images

![Minion](https://octodex.github.com/images/minion.png)
![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

![Alt text][id]

With a reference later in the document defining the URL location:

[id]: https://octodex.github.com/images/dojocat.jpg  "The Dojocat"


## Plugins

The killer feature of `markdown-it` is very effective support of
[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).


### [Emojies](https://github.com/markdown-it/markdown-it-emoji)

> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

see [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.


### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)

- 19^th^
- H~2~O


### [\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Inserted text++


### [\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Marked text==


### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)

Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.


### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)

Term 1

:   Definition 1
with lazy continuation.

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

_Compact style:_

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b


### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)

This is HTML abbreviation example.

It converts "HTML", but keep intact partial entries like "xxxHTMLyyy" and so on.

*[HTML]: Hyper Text Markup Language

### [Custom containers](https://github.com/markdown-it/markdown-it-container)

::: warning
*here be dragons*
:::
        """,
        'filename': 'example1.pdf',
    },
    {
        'markdown_text': """**This** is the first paragraph.
This is the second paragraph.

And this is the third paragraph.
* Item 1
* Item 2
        """,
        'filename': 'example2.pdf',
    },
]

# Single PDF
# markdown_text = markdowns[0]['markdown_text']
markdown_text = """In the case of Fragoso Dacosta v. Spain, the European Court of Human Rights (Section Fifth), composed of: Georges Ravarani, President Mārtiņš Mits, Stéphanie Mourou-Vikström, Lado Chanturia, María Elósegui, Mattias Guyomar, Kateřina Šimáčková, Judges, and Martina Keller, Secretary of the Associate Section, Taking into account: the application No. 27926/21 brought against the Kingdom of Spain on 14 May 2021 before the Court, pursuant to Article 34 of the Convention for the Protection of Human Rights and Fundamental Freedoms ("the Convention"), by a Spanish citizen, Mr Pablo Fragoso Dacosta ("the plaintiff"), the decision to inform the Spanish Government ("the Government"), the observations of the parties, After deliberating closed-door on 4 April and 9 May 2023,It was noted that the complainant's statements were made publicly in the presence of military personnel with the intention of showing contempt or offence, and pointed out that at meetings held a few days earlier, the military authorities expressly asked the complainant to “reduce” the tone of his protest during the solemn ceremony. He added that, although a section of the doctrine is in favour of dismissing this offence in question, judges are subject to criminal law whenever the aforementioned elements occur. He condemned the complainant to a fine of 1,260 euros, which could be replaced by deprivation of liberty in the event of deprivation of liberty.
<br/><br/><br/>
10. The complainant appealed to the Provincial Court of A Coruña, alleging disproportionate interference with the right to ideological freedom and freedom of expression. 11. On 8 February 2018, the ProvincialThey consider the contested judgments that those expressions, pronounced by the repeated speaker at the door of the military arsenal in Ferrol during the solemn ceremony of the izado of the national flag, constitute insults to the Spanish flag, carried out with publicity, which cannot be interpreted as infringed on freedom of expression, unlike what happened with other slogans that were shouted at concentrations held in previous days, which took place at the same place, at the same time and on the occasion of the same act. It is based on the judgments that the defendant acted with the intention of undermining or exceeding, since the expressions pronounced constituted his specific response to a prior request by the military authority to the trade union representatives of workers to reduce the tone of protests they had been making months before the military establishment during the izado of the national flag (...). However, theIn the case of cars, the context is very different, since it is not in the sphere of a conflict between independent states, in the context of an anti-monetary concentration and a protest for the visit of kings to a city, as happened in the valued case of Stern Taulats and Roura Capellera against Spain,[no 51168/15 and 51186/15, of 13 March 2018] but rather of an objectively offensive expression of a feeling of intolerance and exclusion that is projected with its affirmation to all those citizens who see the flag as one of their own symbols of national identity.
<br/><br/><br/>
(...) It was not, therefore, a criticism towards people who, for their role, are subject to a special citizen scrutiny, in the context of an anti-monetary concentration and a protest for the visit of kings to a city, as happened in the valued case of Stern TaulatThe Committee notes with concern that the State party has failed to provide adequate information on the situation of women and girls in the State party, particularly in relation to the implementation of the Convention on the Elimination of All Forms of Discrimination against Women and the Convention on the Rights of the Child on the sale of children, child prostitution and child pornography.The Committee notes with appreciation the State party's report on the implementation of the Convention on the Elimination of All Forms of Discrimination against Women (CRC/C/15/Add.2) and the State party's report on the implementation of the Convention on the Elimination of All Forms of Discrimination against Women (CRC/C/15/Add.2).The Committee notes with concern that the State party has failed to provide adequate information on the situation of women and girls in the State party, particularly in relation to the implementation of the Convention on the Elimination of All Forms of Discrimination against Women.The Committee notes with appreciation that the State party has ratified the Optional Protocol to the Convention on the Rights of the Child on the sale of children, child prostitution and child pornography and the Optional Protocol to the Convention on the Rights of the Child on the sale of children, child prostitution and child pornography.In the present case, although the Provincial Court stated that the military personnel had experienced “an intense feeling of humiliation” (see paragraph 10 above), the fact is that the plaintiff’s statements were not directed at a person or a collective.
<br/><br/><br/>
The Court also notes that the plaintiff’s statements did not cause any personal or material damage, the criminal proceedings were initiated solely at the initiative of the Ministry of Justice (the institution which, in the proceedings before the Constitutional Court, requested the admission of an appeal) and that no civil action was brought in relation to the plaintiff’s statements (see Fuentes Bobo, cited above, § 48). 31. The Court cannot accept the Government and the Constitutional Court’s claim that the plaintiff’s statements had nothing to do with the protests.In the light of the circumstances of the case, the Tribunal is not convinced that the national authorities have achieved a fair balance between the relevant interests at stake in convincing the plaintiff and imposing an excessive penalty on him.
"""
pdf_path = create_pdf_from_markdown(markdown_text, "example.pdf")
print(f"PDF saved as {pdf_path}")
cloudinary_url = upload_pdf_to_cloudinary(pdf_path)
print(f"Cloudinary URL: {cloudinary_url}")

# Multiple PDFs
# result = create_multiple_pdfs_from_markdowns(markdowns)
# print(f"PDFs saved as:")
# print(result)