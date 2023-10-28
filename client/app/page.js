"use client";
import { useState } from "react";

const Home = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [latitude, setLatitude] = useState(null);
  const [longitude, setLongitude] = useState(null);

  const getLocation = () => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const { latitude, longitude } = position.coords;
          console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
          setLatitude(latitude);
          setLongitude(longitude);
        },
        (error) => {
          console.error("Error getting user's location:", error);
        }
      );
    } else {
      console.error("Geolocation is not available in this browser.");
    }
  };

  return (
    <section className="w-full flex-center flex-col">
      <h1 className="head_text text-center">
        Discover & Plant
        <br className="max-md:hidden" />
        <span className="orange_gradient text-center"> AI-Recommend Crops</span>
        <br className="max-md:hidden" />
      </h1>
      <p className="desc text-center">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales
        velit arcu, a fringilla ex scelerisque at. Proin vehicula, augue vel
      </p>
      <br />
      <button onClick={() => setIsModalOpen(true)} className="black_btn">
        Ask AI
      </button>

      {isModalOpen && (
        <div className="fixed inset-0 flex items-center justify-center z-100">
          <div className="absolute inset-0 " />
          <div className="bg-white flex flex-col p-8 w-[600px] rounded-lg z-10">
            <h2 className="text-3xl text-center font-bold">Enter Values</h2>
            <br />
            <p>Enter values to get AI Recommended crops for your farm</p>
            <br />
            <div className="flex flex-row justify-around items-center">
              <input
                className="border max-w-[200px] px-2 py-1 rounded-lg my-2"
                type="text"
                placeholder="Latitude"
                value={latitude}
                disabled
              ></input>
              <input
                className="border max-w-[200px] px-2 py-1 rounded-lg my-2"
                type="text"
                placeholder="Longitude"
                value={longitude}
                disabled
              ></input>
              <button
                className="bg-blue-500 w-fit h-fit px-3 rounded-lg py-1 text-white"
                onClick={getLocation}
              >
                Get Location
              </button>
            </div>
            <input
              className="border px-2 py-1 rounded-lg my-2"
              type="text"
              placeholder="Nitrogen (N)"
            ></input>
            <input
              className="border px-2 py-1 rounded-lg my-2"
              type="text"
              placeholder="Phosphorus (P)"
            ></input>
            <input
              className="border px-2 py-1 rounded-lg my-2"
              type="text"
              placeholder="Potassium (K)"
            ></input>
            <input
              className="border px-2 py-1 rounded-lg my-2"
              type="text"
              placeholder="Soil pH"
            ></input>
            <button
              onClick={() => setIsModalOpen(false)}
              className="bg-red-500 hover:bg-red-600 text-white font-semibold mt-4 py-2 px-6 rounded-full w-fit"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </section>
  );
};
export default Home;
