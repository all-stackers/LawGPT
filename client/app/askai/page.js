"use client";
import React, { useState, useRef, useEffect } from "react";
import { useParams } from "next/navigation";

const Chat = () => {
  const params = useParams();

  const [chatMessages, setChatMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const chatContainerRef = useRef(null);
  const id = parseInt(params.chatId);
  // console.log(params.chatId);

  useEffect(() => {
    // Scroll to the bottom when chatMessages change
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [chatMessages]);
  const onEnterPress = async (event) => {
    if (event.key === "Enter") {
      handleSendMessage();
    }
  };

  const handleSendMessage = () => {
    if (inputMessage.trim() === "") return;
    const newMessage = {
      message: inputMessage,
      sender: "user",
    };
    setChatMessages([...chatMessages, newMessage]);
    setInputMessage("");

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
      "question": inputMessage,
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };

    fetch("http://localhost:5000/askai", requestOptions)
      .then(response => response.json())
      .then(result => {
        const newMessage2 = {
          message: result.data,
          sender: "agent",
        };
        setChatMessages([...chatMessages, newMessage, newMessage2]);
      })
      .catch(error => console.log('error', error));

  };

  return (
    <div className="h-screen flex flex-col">
      <div
        ref={chatContainerRef}
        className="flex-1 pb-[150px] bg-[#fdfdfd] overflow-y-auto"
      >
        {chatMessages.length >0 && chatMessages.map((message, index) => (
          <div
            key={message.message}
            className={` py-8 w-[100%] border border-[#e5e5e5] border-solid flex flex-row ${
              index % 2 === 0
                ? "bg-white text-gray-800 font-medium"
                : "bg-[#f7f7f8] text-gray-800"
            }`}
          >
            <div className="w-[750px] mx-auto flex flex-row">
              {index % 2 === 0 ? (
                <>
                  <div className="w-[30px] mr-[20px] h-[30px]  text-[white]">
                    <img src="/assets/icon/user.png" />
                  </div>
                  <div className="flex w-[90%] flex-row justify-between	">
                    <div className="w-[95%]"> {message.message}</div>
                  </div>
                </>
              ) : (
                <>
                  <div className="w-[30px] mr-[20px] h-[30px] ">
                    <img src="/assets/icon/brain.png" />
                  </div>
                  <div className="flex w-[90%] flex-row justify-between	">
                    <div className="w-[95%]"> {message.message}</div>
                    <div>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="grey"
                        class="w-[18px] h-[18px]"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M15.666 3.888A2.25 2.25 0 0013.5 2.25h-3c-1.03 0-1.9.693-2.166 1.638m7.332 0c.055.194.084.4.084.612v0a.75.75 0 01-.75.75H9a.75.75 0 01-.75-.75v0c0-.212.03-.418.084-.612m7.332 0c.646.049 1.288.11 1.927.184 1.1.128 1.907 1.077 1.907 2.185V19.5a2.25 2.25 0 01-2.25 2.25H6.75A2.25 2.25 0 014.5 19.5V6.257c0-1.108.806-2.057 1.907-2.185a48.208 48.208 0 011.927-.184"
                        />
                      </svg>
                    </div>
                  </div>
                </>
              )}
            </div>
          </div>
        ))}
      </div>
      {chatMessages.length == 0 && (
        <div className="grid grid-cols-2 gap-4 w-[750px] pb-[90px]  mx-auto">
          <div className="p-[5px] px-4 rounded-[12px] border-[1px] border-gray-300 hover:bg-[#ececf1]">
            <h1 className="text-[#40414f] text-[14px] font-bold">
              Named Entity Recognition (NER)
            </h1>
            <p className="text-[#40414f] text-[14px] opacity-[0.5] font-medium text-[12px]">
              Identify and tag entities such as names of people, organizations,
              dates, and locations
            </p>
          </div>
          <div className="p-[5px] px-4 rounded-[12px] border-[1px] border-gray-300 hover:bg-[#ececf1]">
            <h1 className="text-[#40414f] text-[14px] font-bold">
              Automated Document Summarization
            </h1>
            <p className="text-[#40414f] text-[14px] opacity-[0.5] font-medium text-[12px]">
              Condense lengthy legal documents into concise summary to grasp the
              main points of a case.
            </p>
          </div>
        </div>
      )}
      <div className="fixed w-[750px] bottom-[20px] left-1/2 transform -translate-x-1/3 bg-transparent flex items-center">
        <input
          className="flex-1 px-4 py-2 rounded-l-[10px] w-[700px] h-[50px] border border-gray-300 focus:outline-none focus:shadow-outline-blue drop-shadow-2xl"
          type="text"
          placeholder="Type your message..."
          value={inputMessage}
          onKeyDown={onEnterPress}
          onChange={(e) => setInputMessage(e.target.value)}
        />
        <button
          className="bg-white text-white px-4 py-2 h-[50px] border-[1px] rounded-r-[10px] hover:bg-gray-200"
          onClick={handleSendMessage}
        >
          <img
            className="h-[20px]"
            src={`/assets/icon/send.svg`}
            alt="navicon"
          />
        </button>
      </div>
    </div>
  );
};

export default Chat;
