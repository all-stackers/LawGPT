"use client"
import React from 'react';

const FileUploadDiv = () => {
  return (
    <div className=' h-[100%] w-[100%] flex flex-col justify-center items-center'>
<div className="w-[40%] h-[60%] border-2 border-dotted border-gray-300 rounded-lg bg-gray-100 text-center flex flex-col justify-center items-center">
      <h2 className="text-xl font-semibold mt-10">File Upload</h2>
      <label className="h-[100%] w-[100%] flex flex-col justify-center items-center">
        <div className="cursor-pointer border-2 border-dotted h-[60%] w-[60%] border-gray-400 p-4 rounded-lg bg-white">
          {/* <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-16 w-16 mx-auto text-gray-500"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M12 4v6m0 0v6m0-6h6m-6 0H6"
            />
          </svg> */}
          <svg xmlns="http://www.w3.org/2000/svg"
            className="h-16 w-16 mx-auto text-gray-500"
            height="24"
            fill="gray"
            viewBox="0 -960 960 960"
            stroke="currentColor"
            >
            <path
              d="M260-160q-91 0-155.5-63T40-377q0-78 47-139t123-78q25-92 100-149t170-57q117 0 198.5 81.5T760-520q69 8 114.5 59.5T920-340q0 75-52.5 127.5T740-160H520q-33 0-56.5-23.5T440-240v-206l-64 62-56-56 160-160 160 160-56 56-64-62v206h220q42 0 71-29t29-71q0-42-29-71t-71-29h-60v-80q0-83-58.5-141.5T480-720q-83 0-141.5 58.5T280-520h-20q-58 0-99 41t-41 99q0 58 41 99t99 41h100v80H260Zm220-280Z" />
          </svg>
          <p className="text-gray-500 mt-2">Choose a file or drag it here</p>
          <input className=" hidden" type="file" />
        </div>
        
      </label>
    </div>
    </div>
    
  );
};

export default FileUploadDiv;

