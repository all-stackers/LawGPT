import requests
import json
from models.pdf import PDF as PDFModel


pdf_info_list = [
  {
    "pdf_name": "AFFAIRE Aak turkiye.pdf",
    "original_file_cid": "bafkreieiem4ocrfock2s54ypzuz3zns5jh3ti6ivjldsd3qfv4msz4veoq",
    "original_file_url": "https://bafkreieiem4ocrfock2s54ypzuz3zns5jh3ti6ivjldsd3qfv4msz4veoq.ipfs.dweb.link",
    "translated_file_cid": "bafkreiccn74vexqlat2kz32i4zo75cd34ihkgaanatrppnjl6l42z46cuy",
    "translated_file_url": "https://bafkreiccn74vexqlat2kz32i4zo75cd34ihkgaanatrppnjl6l42z46cuy.ipfs.dweb.link",
    "chat_id": 7347
  },
  {
    "pdf_name": "AFFAIRE AVCIOgLU c turkiye.pdf",
    "original_file_cid": "bafkreigl6l72msewitak7n37r22c7hnfa5zeg3njtb7aqbyldo72paxyoi",
    "original_file_url": "https://bafkreigl6l72msewitak7n37r22c7hnfa5zeg3njtb7aqbyldo72paxyoi.ipfs.dweb.link",
    "translated_file_cid": "bafkreidpnjl6tjnm3qp3ioomeuogn3iz6yxkvkebn3z6fqba5fprpwzxyu",
    "translated_file_url": "https://bafkreidpnjl6tjnm3qp3ioomeuogn3iz6yxkvkebn3z6fqba5fprpwzxyu.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE CP ET MN c FRANCE.pdf",
    "original_file_cid": "bafkreic4gm7xowxytmdxhn3pjul42bkuivlgdde2qm5dw7fehv3xoaa7ha",
    "original_file_url": "https://bafkreic4gm7xowxytmdxhn3pjul42bkuivlgdde2qm5dw7fehv3xoaa7ha.ipfs.dweb.link",
    "translated_file_cid": "bafkreihpxixaroko6d3v2sahepmedwfmdh6pgyqxen3ymickfjoywcegja",
    "translated_file_url": "https://bafkreihpxixaroko6d3v2sahepmedwfmdh6pgyqxen3ymickfjoywcegja.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE JALOUD c PAYS-BAS.pdf",
    "original_file_cid": "bafkreid2ss5w4jwhkcgwbtkjsybqolvhqmtajnz2ebl4fp6ci3xcm3an74",
    "original_file_url": "https://bafkreid2ss5w4jwhkcgwbtkjsybqolvhqmtajnz2ebl4fp6ci3xcm3an74.ipfs.dweb.link",
    "translated_file_cid": "bafybeia63ip4ttysxev4k7ssfzixgagrq6vdkycvboi2qfeb2kgznskdwi",
    "translated_file_url": "https://bafybeia63ip4ttysxev4k7ssfzixgagrq6vdkycvboi2qfeb2kgznskdwi.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE KARACSONY ET AUTRES c HONGRIE.pdf",
    "original_file_cid": "bafkreictkwmw7noxnp3mbalu6affzwi7vuusamzv4nldaxckpmc2y2hndy",
    "original_file_url": "https://bafkreictkwmw7noxnp3mbalu6affzwi7vuusamzv4nldaxckpmc2y2hndy.ipfs.dweb.link",
    "translated_file_cid": "bafybeieniv354d3tnakc2tp2cu2ih5ujarahlhh3unyucjufprczhtj2ci",
    "translated_file_url": "https://bafybeieniv354d3tnakc2tp2cu2ih5ujarahlhh3unyucjufprczhtj2ci.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE KHAMTOKHU ET AKSENCHIK c RUSSIE.pdf",
    "original_file_cid": "bafkreianrpfzjneke3qxkuymzlcjl3pkc2y7bezo5d2kacal5ec77te3ba",
    "original_file_url": "https://bafkreianrpfzjneke3qxkuymzlcjl3pkc2y7bezo5d2kacal5ec77te3ba.ipfs.dweb.link",
    "translated_file_cid": "bafybeig7f4a4hongv6o4s77yhly6bmexs464jlgmkdhedd75wenyptoziu",
    "translated_file_url": "https://bafybeig7f4a4hongv6o4s77yhly6bmexs464jlgmkdhedd75wenyptoziu.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE KOILOVA ET BABULKOVA c BULGARIE.pdf",
    "original_file_cid": "bafkreifev6opw5d32xk53atrw4ct3xomwakk4z2qk2sgzxnyd6lxkburke",
    "original_file_url": "https://bafkreifev6opw5d32xk53atrw4ct3xomwakk4z2qk2sgzxnyd6lxkburke.ipfs.dweb.link",
    "translated_file_cid": "bafkreiaxvelb7g6465rbg77tebql3nt4wkqorcjmu37jm4rbagwzdxoiza",
    "translated_file_url": "https://bafkreiaxvelb7g6465rbg77tebql3nt4wkqorcjmu37jm4rbagwzdxoiza.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE MARGUS c CROATIE.pdf",
    "original_file_cid": "bafkreidwi24dhkdutetta2rd2gkkbs55n7hun7zrj24lep65gevm6yglty",
    "original_file_url": "https://bafkreidwi24dhkdutetta2rd2gkkbs55n7hun7zrj24lep65gevm6yglty.ipfs.dweb.link",
    "translated_file_cid": "bafybeidjic67dp3wmc7dbepj26ty6otbbr4thqc6tfb2fqezc6odpq225u",
    "translated_file_url": "https://bafybeidjic67dp3wmc7dbepj26ty6otbbr4thqc6tfb2fqezc6odpq225u.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE POMUL SRL ET SUBERVIN SRL c REPUBLIQUE DE MOLDOVA.pdf",
    "original_file_cid": "bafkreif7jnhieuw7vzm6657kcesjrlw2oopdjcnzmvc2ztlj4jefqfneue",
    "original_file_url": "https://bafkreif7jnhieuw7vzm6657kcesjrlw2oopdjcnzmvc2ztlj4jefqfneue.ipfs.dweb.link",
    "translated_file_cid": "bafkreieqyq6sbmbhmxm2azsewlss5sqkgagit4y2edaqbxye4ubux2gzpe",
    "translated_file_url": "https://bafkreieqyq6sbmbhmxm2azsewlss5sqkgagit4y2edaqbxye4ubux2gzpe.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE STOIANOGLO c REPUBLIQUE DE MOLDOVA.pdf",
    "original_file_cid": "bafkreibjcjvartvcvyzlaghiauq6oigsbof2cwqbbcmyb7bkfwkllrj6zq",
    "original_file_url": "https://bafkreibjcjvartvcvyzlaghiauq6oigsbof2cwqbbcmyb7bkfwkllrj6zq.ipfs.dweb.link",
    "translated_file_cid": "bafkreieryc5qumfryg36ruqlnyvemd2h6ab3sg4buwbxnauodlct6ezufa",
    "translated_file_url": "https://bafkreieryc5qumfryg36ruqlnyvemd2h6ab3sg4buwbxnauodlct6ezufa.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "AFFAIRE ZUBAC c CROATIE.pdf",
    "original_file_cid": "bafkreib43ikgat5xfuxh5evbx35plx6h2tfkovaytewhaeblqfn42gcscq",
    "original_file_url": "https://bafkreib43ikgat5xfuxh5evbx35plx6h2tfkovaytewhaeblqfn42gcscq.ipfs.dweb.link",
    "translated_file_cid": "bafybeie6dq2wayabz7jyh6eojo7hz4bu6zxp53waqrim5tvquq4nqnye7m",
    "translated_file_url": "https://bafybeie6dq2wayabz7jyh6eojo7hz4bu6zxp53waqrim5tvquq4nqnye7m.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF ANAGNOSTAKIS v GREECE.pdf",
    "original_file_cid": "bafkreibjmr4sb3iycrjyvzibufrddsqklcj5n6h43fh3l6sacfpqktex3m",
    "original_file_url": "https://bafkreibjmr4sb3iycrjyvzibufrddsqklcj5n6h43fh3l6sacfpqktex3m.ipfs.dweb.link",
    "translated_file_cid": "bafkreibjmr4sb3iycrjyvzibufrddsqklcj5n6h43fh3l6sacfpqktex3m",
    "translated_file_url": "https://bafkreibjmr4sb3iycrjyvzibufrddsqklcj5n6h43fh3l6sacfpqktex3m.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF BIAO v DENMARK.pdf",
    "original_file_cid": "bafkreidw53kmxelududk72a55gt6afnumbfsht62st26vokzsjyisouv6y",
    "original_file_url": "https://bafkreidw53kmxelududk72a55gt6afnumbfsht62st26vokzsjyisouv6y.ipfs.dweb.link",
    "translated_file_cid": "bafkreidw53kmxelududk72a55gt6afnumbfsht62st26vokzsjyisouv6y",
    "translated_file_url": "https://bafkreidw53kmxelududk72a55gt6afnumbfsht62st26vokzsjyisouv6y.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF CREDIT EUROPE LEASING IFN SA v ROMANIA.pdf",
    "original_file_cid": "bafkreifguew2zcr5ifhwi5467wecka4qbzvbtp7dtaw3d4cfruaqlvnema",
    "original_file_url": "https://bafkreifguew2zcr5ifhwi5467wecka4qbzvbtp7dtaw3d4cfruaqlvnema.ipfs.dweb.link",
    "translated_file_cid": "bafkreifguew2zcr5ifhwi5467wecka4qbzvbtp7dtaw3d4cfruaqlvnema",
    "translated_file_url": "https://bafkreifguew2zcr5ifhwi5467wecka4qbzvbtp7dtaw3d4cfruaqlvnema.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF HOVHANNISYAN AND KARAPETYAN v ARMENIA.pdf",
    "original_file_cid": "bafkreifbejqrovosbor4xulduvqkirfbsfhsh5gec46m3f3ilcur2arxpi",
    "original_file_url": "https://bafkreifbejqrovosbor4xulduvqkirfbsfhsh5gec46m3f3ilcur2arxpi.ipfs.dweb.link",
    "translated_file_cid": "bafkreifbejqrovosbor4xulduvqkirfbsfhsh5gec46m3f3ilcur2arxpi",
    "translated_file_url": "https://bafkreifbejqrovosbor4xulduvqkirfbsfhsh5gec46m3f3ilcur2arxpi.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF INTERNATIONALE HUMANITARE HILFSORGANISATION E Vs GERMANY.pdf",
    "original_file_cid": "bafkreiez24fnpmktkair6o5q567rrgkezxszuh6n4ld3nf3n2ewvjfxnqe",
    "original_file_url": "https://bafkreiez24fnpmktkair6o5q567rrgkezxszuh6n4ld3nf3n2ewvjfxnqe.ipfs.dweb.link",
    "translated_file_cid": "bafkreiez24fnpmktkair6o5q567rrgkezxszuh6n4ld3nf3n2ewvjfxnqe",
    "translated_file_url": "https://bafkreiez24fnpmktkair6o5q567rrgkezxszuh6n4ld3nf3n2ewvjfxnqe.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF KURT v AUSTRIA.pdf",
    "original_file_cid": "bafkreiek76dqaeiygf6y5w2eqlezhcfvzickspkfj4qyzha56dq27y77qq",
    "original_file_url": "https://bafkreiek76dqaeiygf6y5w2eqlezhcfvzickspkfj4qyzha56dq27y77qq.ipfs.dweb.link",
    "translated_file_cid": "bafkreiek76dqaeiygf6y5w2eqlezhcfvzickspkfj4qyzha56dq27y77qq",
    "translated_file_url": "https://bafkreiek76dqaeiygf6y5w2eqlezhcfvzickspkfj4qyzha56dq27y77qq.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE OF MURTAZALIYEVA v RUSSIA.pdf",
    "original_file_cid": "bafkreia7sgtreshmugcbyr4yo7m7lnvh726ph244mpbzb3i3olsn4yyigm",
    "original_file_url": "https://bafkreia7sgtreshmugcbyr4yo7m7lnvh726ph244mpbzb3i3olsn4yyigm.ipfs.dweb.link",
    "translated_file_cid": "bafkreia7sgtreshmugcbyr4yo7m7lnvh726ph244mpbzb3i3olsn4yyigm",
    "translated_file_url": "https://bafkreia7sgtreshmugcbyr4yo7m7lnvh726ph244mpbzb3i3olsn4yyigm.ipfs.dweb.link",
    "chat_id": 8742
  },
  {
    "pdf_name": "CASE OF PERINCEK vs SWITZERLAND - spanish.pdf",
    "original_file_cid": "bafybeify66pae7rvlbebaxgr4af36qeaefa5y25pvji3grcjojngipziq4",
    "original_file_url": "https://bafybeify66pae7rvlbebaxgr4af36qeaefa5y25pvji3grcjojngipziq4.ipfs.dweb.link",
    "translated_file_cid": "bafybeib4ivt5qaxvcij5ohjhkjnbroaaj5v6jp3rygsqbam34awx4kn6im",
    "translated_file_url": "https://bafybeib4ivt5qaxvcij5ohjhkjnbroaaj5v6jp3rygsqbam34awx4kn6im.ipfs.dweb.link",
    "chat_id": 0
  },
  {
    "pdf_name": "CASE_OF_FRAGOSO_DACOSTAvSPAIN_spansish.pdf",
    "original_file_cid": "bafkreihxq3ioghhz444wx2nnobubilwt6rzzvb6wghqpocsyjvgthxwxga",
    "original_file_url": "https://bafkreihxq3ioghhz444wx2nnobubilwt6rzzvb6wghqpocsyjvgthxwxga.ipfs.dweb.link",
    "translated_file_cid": "bafkreicaswhsdxlh5oz4mf4w57c26irkhxxxkvwoo3l3afy3knehkvivnu",
    "translated_file_url": "https://bafkreicaswhsdxlh5oz4mf4w57c26irkhxxxkvwoo3l3afy3knehkvivnu.ipfs.dweb.link",
    "chat_id": 0
  }
]



def generate_pdfs():
    # Now, pdf_info_list contains the array of PDF information as a Python list of dictionaries
    for pdf_info in pdf_info_list:
        print("PDF Name:", pdf_info["pdf_name"])
        print("Original File CID:", pdf_info["original_file_cid"])
        print("Original File URL:", pdf_info["original_file_url"])
        print("Translated File CID:", pdf_info["translated_file_cid"])
        print("Translated File URL:", pdf_info["translated_file_url"])
        print("Chat ID:", pdf_info.get("chat_id", "N/A"))
        print()
            
        created = PDFModel.add(pdf_info["pdf_name"], pdf_info["original_file_cid"], pdf_info["original_file_url"], pdf_info["translated_file_cid"], pdf_info["translated_file_url"], pdf_info["chat_id"])
        print(created)