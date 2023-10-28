"use client";

import Link from "next/link";
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { ScaleLoader } from "react-spinners";

const AllChats = () => {
  const Router = useRouter();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [pdfFile, setPdfFile] = useState(null);
  const [fileInputValue, setFileInputValue] = useState("");
  const [loading, setLoading] = useState(false);
  const [allChats, setAllChats] = useState([]);

  // const allChats = [
  //   {
  //     id: "0f75f3af-9f26-4f9d-9fe8-cabbdee853a8",
  //     title: "Marriage",
  //     tags: ["Marriage", "Relationships", "Family"],
  //     description:
  //       "A case involving a couple planning to get married and seeking legal advice on marriage contracts, prenuptial agreements, and related family matters.",
  //   },
  //   {
  //     id: "1a23b4c5-6d78-9e01-2f3g-4h56i7j8k90l",
  //     title: "Child Custody Battle",
  //     tags: ["Custody", "Divorce", "Children"],
  //     description: "A case involving a custody dispute after a divorce.",
  //   },
  //   {
  //     id: "2mnopq3r-4stu-5vw6x7-yz89a0b1c2",
  //     title: "Employment Discrimination",
  //     tags: ["Employment", "Discrimination", "Workplace"],
  //     description: "An employment discrimination case at a workplace.",
  //   },
  //   {
  //     id: "3d4e56f7g-89hi01-j2klm3no-4pqrs5tu6",
  //     title: "Personal Injury Lawsuit",
  //     tags: ["Personal Injury", "Accident", "Legal"],
  //     description: "A legal case involving personal injury from an accident.",
  //   },
  //   {
  //     id: "4v5w67x8y-9z01a2b3c4-d5e6f7g8h90",
  //     title: "Real Estate Dispute",
  //     tags: ["Real Estate", "Property", "Legal"],
  //     description: "A legal dispute related to real estate and property.",
  //   },
  //   {
  //     id: "5ij6kl7mn-89op01q2r-3s4tu5v6wx7",
  //     title: "Criminal Defense",
  //     tags: ["Criminal Defense", "Legal", "Crime"],
  //     description:
  //       "A legal case involving criminal defense and criminal charges.",
  //   },
  //   {
  //     id: "6yz7ab8cd-9ef01g2hi-3jk4lm5no6p7",
  //     title: "Business Contract Dispute",
  //     tags: ["Business", "Contract", "Legal"],
  //     description: "A legal dispute related to a business contract.",
  //   },
  // ];
  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setPdfFile(selectedFile);
      setFileInputValue(selectedFile.name);
    }
  };

  const uploadPdfFormData = () => {
    setLoading(true);
    if (pdfFile) {
      console.log(loading);

      var formdata = new FormData();
      formdata.append("file", pdfFile, "[PROXY]");

      var requestOptions = {
        method: "POST",
        body: formdata,
        redirect: "follow",
      };

      fetch("http://localhost:5000/chat?create=True", requestOptions)
        .then((response) => response.json())
        .then((result) => {
          console.log(result?.data?.index_id);
          setLoading(false);

          Router.push(`/chat/${result?.data?.index_id}`);
        })
        .catch((error) => console.log("error", error));
      }
  };


  const fetchAllChats = async () => {
    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };
    
    fetch("http://localhost:5000/chat", requestOptions)
      .then(response => response.json())
      .then(result => setAllChats(result.data))
      .catch(error => console.log('error', error));
  }

  useEffect(() => {
    fetchAllChats();
  }, []);


  console.log(loading);
  return (
    <div style={{ overflow: "auto", maxHeight: "100vh" }}>
      <div className="py-4 flex flex-col items-center">
        <div className="py-4 flex flex-row items-center w-[85%] justify-between">
          <h1 className="text-4xl font-bold">All Chat Records</h1>
          <button
            onClick={openModal}
            className="px-4 py-2 flex flex-row gap-x-2 border border-gray-400 rounded-lg shadow-lg"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              className="w-6 h-6"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M12 4.5v15m7.5-7.5h-15"
              />
            </svg>
            New Chat
          </button>
        </div>

        <div className="w-[85%] mt-8">
          {allChats.map((chat) => (
            <Link href={`/chat/${chat.index_id}`}>
              <div className="bg-gray-100 border-[1px] border-blue-100 p-4 m-4 rounded-lg hover:bg-gray-200 hover:border-gray-300 ">
                <h2 className="text-xl font-semibold">{chat.title}</h2>
                <div className="text-gray-600 my-2">
                  <div className="flex flex-row gap-x-2">
                    {chat.tags.split(',').map((tag, index) => (
                      <div
                        key={index}
                        className="bg-blue-200 text-blue-700 rounded-md px-2 py-[2px] my-1"
                      >
                        {tag}
                      </div>
                    ))}
                  </div>
                  <div className="mb-2">{chat.summary}</div>
                </div>
              </div>
            </Link>
          ))}
        </div>
        {isModalOpen && (
          <div className="fixed inset-0 flex items-center justify-center z-100 drop-shadow-2xl">
            <div className="fixed top-0 left-0 w-[100%] h-[100%] bg-[#000000a3]">
              <div className="bg-white w-[500px] mx-auto my-[20vh] rounded-lg shadow-lg p-4">
                <div>
                  <div className="flex justify-between">
                    <h2 className="text-xl font-bold">Upload PDF</h2>

                    <button onClick={closeModal}>
                      <img
                        className="h-[20px]"
                        src={`/assets/icon/close.svg`}
                        alt="navicon"
                      />
                    </button>
                  </div>
                  <p>Upload PDF and ask queries.</p>
                  <label className="flex flex-col justify-center items-center mt-[20px] ">
                    <div className="cursor-pointer border-2 border-dotted w-[90%] h-[200px] border-gray-400 px-4 rounded-lg bg-white py-[30px]">
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
                      <p className="text-gray-500 mt-2 w-fit mx-auto">
                        Choose a file or drag it here
                      </p>
                      <input
                        className=" hidden"
                        type="file"
                        accept=".pdf"
                        onChange={handleFileChange}
                      />
                    </div>
                  </label>
                  <p>{fileInputValue}</p>
                  <div className="flex flex-row justify-center">
                    {loading ? (
                      <div className="mt-4">
                        <ScaleLoader color="#7C3AED" />
                        Hold on!
                      </div>
                    ) : (
                      <button
                        onClick={uploadPdfFormData}
                        className="bg-blue-500 text-white px-8 py-1 mt-4 rounded"
                      >
                        Upload
                      </button>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default AllChats;
