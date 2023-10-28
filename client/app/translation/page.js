"use client";
import React, { useState } from "react";

const FileUploadDiv = () => {
  const [pdfFile, setPdfFile] = useState(null);
  const [fileInputValue, setFileInputValue] = useState("");

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setPdfFile(selectedFile);
      setFileInputValue(selectedFile.name);
    }
  };

  const uploadPdfFormData = () => {
    if (pdfFile) {
      const formData = new FormData();
      formData.append("pdfFile", pdfFile);
    }
  };

  return (
    <div className=" h-[100%] w-[100%] flex flex-col justify-center items-center">
      <div className="w-[40%] h-[60%] border-[3px] border-dotted border-gray-300 rounded-lg bg-gray-100 text-center flex flex-col justify-center items-center ">
        <h2 className="text-xl font-semibold ">File Upload</h2>
        <label className="flex flex-col justify-center items-center mt-10 ">
          <div className="cursor-pointer border-2 border-dotted h-[100%] w-[100%] border-gray-400 px-4 rounded-lg bg-white py-[30px]">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-16 w-16 mx-auto text-gray-500"
              height="24"
              fill="gray"
              viewBox="0 -960 960 960"
              stroke="currentColor"
            >
              <path d="M260-160q-91 0-155.5-63T40-377q0-78 47-139t123-78q25-92 100-149t170-57q117 0 198.5 81.5T760-520q69 8 114.5 59.5T920-340q0 75-52.5 127.5T740-160H520q-33 0-56.5-23.5T440-240v-206l-64 62-56-56 160-160 160 160-56 56-64-62v206h220q42 0 71-29t29-71q0-42-29-71t-71-29h-60v-80q0-83-58.5-141.5T480-720q-83 0-141.5 58.5T280-520h-20q-58 0-99 41t-41 99q0 58 41 99t99 41h100v80H260Zm220-280Z" />
            </svg>
            <p className="text-gray-500 mt-2">Choose a file or drag it here</p>
            <input
              className=" hidden"
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
            />
          </div>
        </label>
        <div className="w-[100%]"></div>
      </div>
      <button
        className=" mt-[20px] w-[15%] px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
        onClick={uploadPdfFormData}
      >
        Upload
      </button>
    </div>
  );
};

export default FileUploadDiv;
