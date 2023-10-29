"use client";
import { useEffect, useState } from "react";

const Home = () => {
  const [myDocuments, setMyDocuments] = useState([])

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/pdf`)
      .then(response => response.json())
      .then(result => {
        setMyDocuments(result.data);
        console.log(result.data[0]);
      })
      .catch(error => console.log('error', error));

  }, [])
  // const myDocuments = [
  //   {
  //     chat_id: 1,
  //     pdf_name: "Jhon and Mary Case File",
  //     language: "English",
  //     original_file_url: "<link>",
  //   },
  //   {
  //     id: 2,
  //     name: "Legal Brief for Smith vs. Johnson",
  //     language: "English",
  //     pdfLink: "<link>",
  //   },
  //   {
  //     id: 3,
  //     name: "Family Will and Testament",
  //     language: "English",
  //     pdfLink: "<link>",
  //   },
  //   {
  //     id: 4,
  //     name: "Property Deed for 123 Main Street",
  //     language: "English",
  //     pdfLink: "<link>",
  //   },
  //   {
  //     id: 5,
  //     name: "Corporate Contract Agreement",
  //     language: "English",
  //     pdfLink: "<link>",
  //   },
  //   {
  //     id: 6,
  //     name: "Estate Planning Guide",
  //     language: "English",
  //     pdfLink: "<link>",
  //   },
  // ];

  return (
    <div className="pb-10" style={{ overflow: "auto", maxHeight: "100vh" }}>
      <section className="w-[100%] mx-auto">
        <div>
          <div
            style={{
              background: "linear-gradient(to right, #dfdfdf, #767676)", // Adjust gradient colors as needed
            }}
            class="bg-blue-500 h-40 w-full"
          ></div>
          <div class="mt-[-70px] ml-[40px] border-white border-4 w-[150px] overflow-hidden h-[150px] bg-gray-500 rounded-full">
            <img src={"/assets/images/profile.png"} alt="hhh" />
          </div>

          <div class="flex mt-[-30px] justify-end mr-10">
            <button class="bg-white border border-blue-500 border-2 text-blue-600 px-4 py-1 rounded-full">
              Profile Settings
            </button>
          </div>
          <h1 className="ml-[40px] text-3xl text-gray-800 font-bold">
            Jhenil Parihar
          </h1>
        </div>
        <div className="px-[40px] mt-[30px] w-full flex flex-col">
          <h1 className="text-5xl text-gray-700 font-bold mx-auto ">
            My Documents
          </h1>
          <div className="mt-10 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {myDocuments.map((document, idx) => (
              <div
                key={document.chat_id+"_"+idx}
                className="bg-white rounded-lg p-4 shadow-md border border-gray-200"
              >
                <h2 className="text-xl font-semibold mb-2">{document.pdf_name}</h2>
                {/* <p className="text-gray-600 mb-2">
                  Language: English
                </p> */}
                <a
                  href={`view-pdf/${document.original_file_cid}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 hover:underline"
                >
                  View PDF
                </a>
                <br/>
                <a
                  href={`view-pdf/${document.translated_file_cid}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 hover:underline"
                >
                  View Translated PDF
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};
export default Home;
