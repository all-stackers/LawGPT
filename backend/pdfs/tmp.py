import re

def split_into_paragraphs(text, max_sentences_per_paragraph=3):
    # Split the text into sentences using regular expressions
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Initialize variables
    paragraphs = []
    current_paragraph = ""

    # Iterate through sentences and group them into paragraphs
    for sentence in sentences:
        current_paragraph += sentence + " "

        # Check if the current paragraph has reached the desired sentence count
        if sentence.endswith('.') and len(current_paragraph.split()) >= max_sentences_per_paragraph:
            paragraphs.append(current_paragraph.strip())
            current_paragraph = ""

    # Add any remaining text as the last paragraph
    if current_paragraph:
        paragraphs.append(current_paragraph.strip())

    return paragraphs

def merge_paragraphs(paragraphs):
    # Merge the paragraphs into a single text.
    merged_text = '\n<br/><br/><br/>\n'.join(paragraphs)
    return merged_text

# Example usage:
long_text = """In the case of Fragoso Dacosta v. Spain, the European Court of Human Rights (Section Fifth), composed of: Georges Ravarani, President Mārtiņš Mits, Stéphanie Mourou-Vikström, Lado Chanturia, María Elósegui, Mattias Guyomar, Kateřina Šimáčková, Judges, and Martina Keller, Secretary of the Associate Section, Taking into account: the application No. 27926/21 brought against the Kingdom of Spain on 14 May 2021 before the Court, pursuant to Article 34 of the Convention for the Protection of Human Rights and Fundamental Freedoms ("the Convention"), by a Spanish citizen, Mr Pablo Fragoso Dacosta ("the plaintiff"), the decision to inform the Spanish Government ("the Government"), the observations of the parties, After deliberating closed-door on 4 April and 9 May 2023,It was noted that the complainant's statements were made publicly in the presence of military personnel with the intention of showing contempt or offence, and pointed out that at meetings held a few days earlier, the military authorities expressly asked the complainant to “reduce” the tone of his protest during the solemn ceremony. He added that, although a section of the doctrine is in favour of dismissing this offence in question, judges are subject to criminal law whenever the aforementioned elements occur. He condemned the complainant to a fine of 1,260 euros, which could be replaced by deprivation of liberty in the event of deprivation of liberty. 10. The complainant appealed to the Provincial Court of A Coruña, alleging disproportionate interference with the right to ideological freedom and freedom of expression. 11. On 8 February 2018, the ProvincialThey consider the contested judgments that those expressions, pronounced by the repeated speaker at the door of the military arsenal in Ferrol during the solemn ceremony of the izado of the national flag, constitute insults to the Spanish flag, carried out with publicity, which cannot be interpreted as infringed on freedom of expression, unlike what happened with other slogans that were shouted at concentrations held in previous days, which took place at the same place, at the same time and on the occasion of the same act. It is based on the judgments that the defendant acted with the intention of undermining or exceeding, since the expressions pronounced constituted his specific response to a prior request by the military authority to the trade union representatives of workers to reduce the tone of protests they had been making months before the military establishment during the izado of the national flag (...). However, theIn the case of cars, the context is very different, since it is not in the sphere of a conflict between independent states, in the context of an anti-monetary concentration and a protest for the visit of kings to a city, as happened in the valued case of Stern Taulats and Roura Capellera against Spain,[no 51168/15 and 51186/15, of 13 March 2018] but rather of an objectively offensive expression of a feeling of intolerance and exclusion that is projected with its affirmation to all those citizens who see the flag as one of their own symbols of national identity. (...) It was not, therefore, a criticism towards people who, for their role, are subject to a special citizen scrutiny, in the context of an anti-monetary concentration and a protest for the visit of kings to a city, as happened in the valued case of Stern TaulatThe Committee notes with concern that the State party has failed to provide adequate information on the situation of women and girls in the State party, particularly in relation to the implementation of the Convention on the Elimination of All Forms of Discrimination against Women and the Convention on the Rights of the Child on the sale of children, child prostitution and child pornography.The Committee notes with appreciation the State party's report on the implementation of the Convention on the Elimination of All Forms of Discrimination against Women (CRC/C/15/Add.2) and the State party's report on the implementation of the Convention on the Elimination of All Forms of Discrimination against Women (CRC/C/15/Add.2).The Committee notes with concern that the State party has failed to provide adequate information on the situation of women and girls in the State party, particularly in relation to the implementation of the Convention on the Elimination of All Forms of Discrimination against Women.The Committee notes with appreciation that the State party has ratified the Optional Protocol to the Convention on the Rights of the Child on the sale of children, child prostitution and child pornography and the Optional Protocol to the Convention on the Rights of the Child on the sale of children, child prostitution and child pornography.In the present case, although the Provincial Court stated that the military personnel had experienced “an intense feeling of humiliation” (see paragraph 10 above), the fact is that the plaintiff’s statements were not directed at a person or a collective. The Court also notes that the plaintiff’s statements did not cause any personal or material damage, the criminal proceedings were initiated solely at the initiative of the Ministry of Justice (the institution which, in the proceedings before the Constitutional Court, requested the admission of an appeal) and that no civil action was brought in relation to the plaintiff’s statements (see Fuentes Bobo, cited above, § 48). 31. The Court cannot accept the Government and the Constitutional Court’s claim that the plaintiff’s statements had nothing to do with the protests.In the light of the circumstances of the case, the Tribunal is not convinced that the national authorities have achieved a fair balance between the relevant interests at stake in convincing the plaintiff and imposing an excessive penalty on him."""

max_paragraph_length = 200

paragraphs = split_into_paragraphs(long_text, max_paragraph_length)
merged_text = merge_paragraphs(paragraphs)

# Print the merged text.
print(merged_text)
