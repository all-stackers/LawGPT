"use client"
import React, { useState } from 'react';


const Chat = () => {
    const [chatMessages, setChatMessages] = useState([

    ]);
    const [inputMessage, setInputMessage] = useState('');

    const handleInputChange = (e) => {
        setInputMessage(e.target.value);
    };

    const handleSendMessage = () => {
        if (inputMessage.trim() === '') return;
        const newMessage = { id: chatMessages.length + 1, text: inputMessage, sender: 'user' };
        setChatMessages([...chatMessages, newMessage]);
        setInputMessage('');
    };

    return (
        <div className="h-screen flex flex-col">
            <div className="bg-gray-200  flex-1 overflow-y-auto">
                {chatMessages.map((message, index) => (
                    <div
                        key={message.id}
                        className={` py-8 px-[20%] w-[100%] border border-[#e5e5e5] border-solid flex flex-row ${index % 2 === 0 ? 'bg-white text-gray-800 font-medium' : 'bg-[#f7f7f8] text-gray-800'}`}
                    >
                        {index % 2 === 0 ? (
                                <div className='w-[30px] mr-[20px] h-[30px]  text-[white]'>
                                    <img src="/assets/icon/user.png" />
                                </div>
                            ) :               
                                <div className='w-[30px] mr-[20px] h-[30px] '>
                                    <img src="/assets/icon/brain.png" />
                                </div>
                        }
<div className='w-[90%]'>  {message.text}</div>
                       
                    </div>
                ))}
            </div>

            <div className="bg-blue-500 bg-opacity-10 py-4 px-[10%] flex items-center">
                <input
                    className="flex-1 px-4 py-2 rounded-[10px] h-[50px] border border-gray-300 focus:outline-none focus:shadow-outline-blue"
                    type="text"
                    placeholder="Type your message..."
                    value={inputMessage}
                    onChange={handleInputChange}
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
