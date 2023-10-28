import React from "react";

const AllChats = () => {
  const allChats = [
    {
      id: "0f75f3af-9f26-4f9d-9fe8-cabbdee853a8",
      title: "Marriage",
      tags: ["Marriage", "Relationships", "Family"],
      description:
        "A case involving a couple planning to get married and seeking legal advice on marriage contracts, prenuptial agreements, and related family matters.",
    },
    {
      id: "1a23b4c5-6d78-9e01-2f3g-4h56i7j8k90l",
      title: "Child Custody Battle",
      tags: ["Custody", "Divorce", "Children"],
      description: "A case involving a custody dispute after a divorce.",
    },
    {
      id: "2mnopq3r-4stu-5vw6x7-yz89a0b1c2",
      title: "Employment Discrimination",
      tags: ["Employment", "Discrimination", "Workplace"],
      description: "An employment discrimination case at a workplace.",
    },
    {
      id: "3d4e56f7g-89hi01-j2klm3no-4pqrs5tu6",
      title: "Personal Injury Lawsuit",
      tags: ["Personal Injury", "Accident", "Legal"],
      description: "A legal case involving personal injury from an accident.",
    },
    {
      id: "4v5w67x8y-9z01a2b3c4-d5e6f7g8h90",
      title: "Real Estate Dispute",
      tags: ["Real Estate", "Property", "Legal"],
      description: "A legal dispute related to real estate and property.",
    },
    {
      id: "5ij6kl7mn-89op01q2r-3s4tu5v6wx7",
      title: "Criminal Defense",
      tags: ["Criminal Defense", "Legal", "Crime"],
      description:
        "A legal case involving criminal defense and criminal charges.",
    },
    {
      id: "6yz7ab8cd-9ef01g2hi-3jk4lm5no6p7",
      title: "Business Contract Dispute",
      tags: ["Business", "Contract", "Legal"],
      description: "A legal dispute related to a business contract.",
    },
  ];

  return (
    <div style={{ overflow: "auto", maxHeight: "100vh" }}>
      <div className="px-5 py-2 flex flex-row justify-between">
        <p className="text-[#1772ff]">Chats /</p>
      </div>
      <div className="py-4 flex flex-col items-center">
        <h1 className="text-4xl font-bold">All Chat Records</h1>
        <div className="w-[85%] mt-8">
          {allChats.map((chat) => (
            <div className="bg-gray-100 p-4 m-4 rounded-lg">
              <h2 className="text-xl font-semibold">{chat.title}</h2>
              <div className="text-gray-600 my-2">
                <div className="flex flex-row gap-x-2">
                  {chat.tags.map((tag, index) => (
                    <div
                      key={index}
                      className="bg-blue-200 text-blue-700 rounded-full px-2 py-1 my-1"
                    >
                      {tag}
                    </div>
                  ))}
                </div>
                <div className="mb-2">{chat.description}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AllChats;
