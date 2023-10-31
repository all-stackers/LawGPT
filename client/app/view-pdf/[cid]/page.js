"use client";
import { useState } from "react";
import { useParams } from "next/navigation";
import { ScaleLoader } from "react-spinners";

const PDFViewer = () => {
  const params = useParams();
  const [chatMessages, setChatMessages] = useState("");
  const [inputMessage, setInputMessage] = useState("");
  const [askingAI, setAskingAI] = useState(false);
  const cid = params.cid;

  const cid_to_url = (cid) => `https://${cid}.ipfs.dweb.link`
  console.log(cid_to_url(cid));


  const onEnterPress = async (event) => {
    if (event.key === "Enter") {
      handleSendMessage();
    }
  };

  const handleSendMessage = () => {
    if (inputMessage.trim() === "") return;
    setChatMessages("");
    setAskingAI(true);

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      question: "Explain this legal phrase in simple term: " + inputMessage,
    });

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow",
    };

    fetch("http://localhost:5000/askai", requestOptions)
      .then((response) => response.json())
      .then((result) => {
        setChatMessages(result.data);
        setAskingAI(false);
      })
      .catch((error) => console.log("error", error));
  };

  return (
    <div className="flex flex-wrap">
      <div className="w-full md:w-7/12 p-4 h-full">
        <iframe
          src={cid_to_url(cid)}
          width="100%"
          style={{
            height: "95vh",
          }}
          frameBorder="0"
          scrolling="no"
        />
      </div>

      {/* Right side (Text content) */}
      <div className="w-full md:w-5/12 p-4 flex flex-col">
        <h1 className="text-2xl font-bold mb-4">PDF Information</h1>
        <p>
          Here you can display text content, information, or any additional
          details related to the PDF you can display text content, information,
          or any additional details related to the .
        </p>
        <hr className="my-4" />
        <h1 className="text-xl font-medium">Simplify Legal Phrases</h1>
        <input
          type="text"
          className="h-[50px] w-full rounded-[10px] border-[1px] border-gray-200 px-[30px] box-border text-[#000000] outline-none my-[20px] focus:border-blue-300 focus:border-2"
          placeholder="Enter Text Here..."
          value={inputMessage}
          onKeyDown={onEnterPress}
          onChange={(e) => setInputMessage(e.target.value)}
        />
        <div
          style={{
            overflow: "auto",
            maxHeight: "230px",
          }}
          className="bg-gray-100 h-[230px] p-4 rounded-lg shadow-md flex"
        >
          {askingAI && (
            <div className="mt-4 ml-auto mr-auto">
              <ScaleLoader color="#7C3AED" />
              Hold on!
            </div>
          )}
          {chatMessages}
        </div>
      </div>
    </div>
  );
};

export default PDFViewer;


