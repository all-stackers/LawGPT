"use client";
import React, { useState, useRef, useEffect } from "react";

const Chat = () => {
  const [chatMessages, setChatMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const chatContainerRef = useRef(null);

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
      id: chatMessages.length + 1,
      text: inputMessage,
      sender: "user",
    };
    setChatMessages([...chatMessages, newMessage]);
    setInputMessage("");
  };

  return (
    <div className="h-screen flex flex-col">
      <div
        ref={chatContainerRef}
        className="flex-1 pb-[150px] bg-[#fdfdfd] overflow-y-auto"
      >
        {chatMessages.map((message, index) => (
          <div
            key={message.id}
            className={` py-8 px-[20%] w-[100%] border border-[#e5e5e5] border-solid flex flex-row ${
              index % 2 === 0
                ? "bg-white text-gray-800 font-medium"
                : "bg-[#f7f7f8] text-gray-800"
            }`}
          >
            {index % 2 === 0 ? (
              <div className="w-[30px] mr-[20px] h-[30px]  text-[white]">
                <img src="/assets/icon/user.png" />
              </div>
            ) : (
              <div className="w-[30px] mr-[20px] h-[30px] ">
                <img src="/assets/icon/brain.png" />
              </div>
            )}
            <div className="w-[90%]"> {message.text}</div>
          </div>
        ))}
      </div>
      <div className="fixed bottom-[10px] left-1/2 transform -translate-x-1/3 bg-transparent flex items-center">
        <input
          className="flex-1 px-4 py-2 rounded-[10px] w-[700px] h-[50px] border border-gray-300 focus:outline-none focus:shadow-outline-blue shadow-lg"
          type="text"
          placeholder="Type your message..."
          value={inputMessage}
          onKeyDown={onEnterPress}
          onChange={(e) => setInputMessage(e.target.value)}
        />
        <button
          className="ml-4 bg-blue-500 text-white px-4 py-2 h-[40px] rounded-[10px] hover:bg-blue-600"
          onClick={handleSendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;
