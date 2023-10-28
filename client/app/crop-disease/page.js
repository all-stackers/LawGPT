"use client";

import React, { useState, useEffect } from "react";
import axios from "axios";
import { ScaleLoader } from "react-spinners";
import { toast } from "react-toastify";
import { useSpeechSynthesis } from 'react-speech-kit';


const PredictDiseaseFromSymptoms = () => {

  const [value1, setValue1] = useState('Massage can be soothing for babies. Make sure the room is warm, your baby is quiet, well-rested and alert, and you’re relaxed. Try massage after your baby’s nap, when they’re being changed or in the cot, or after a bath. You can do massage for 10-30 minutes.');
  const [value2, setValue2] = useState('Smooth sorbolene cream or lotion into your warm hands and massage the soles of your baby’s feet. Use firm, gentle, slow strokes from heel to toe. Always keep one hand on your baby.');
  const [value3, setValue3] = useState('Do long smooth strokes up your baby’s leg. Massage from ankle up to thigh and over hip. Massage both legs at once or one at a time. Avoid the genital area. Hold your baby’s leg under the knee and gently press it towards the tummy to release wind.');
  const { speak, cancel, speaking } = useSpeechSynthesis();




  // const [options, setOptions] = useState([]);
  // const [to, setTo] = useState("en");
  // const [from, setFrom] = useState("en");
  // const [input, setInput] = useState("");
  // const [output, setOutput] = useState("");

  const [symptoms, setSymptoms] = useState([]);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);


  const stopSpeaking = () => {
    cancel();
  };


  //   const translate = () => {
  //     const params = new URLSearchParams();
  //     params.append("q", data.Treatment);
  //     params.append("source", from);
  //     params.append("target", to);
  //     params.append("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx");

  //     axios
  //       .post("https://libretranslate.de/translate", params, {
  //         headers: {
  //           accept: "application/json",
  //           "Content-Type": "application/x-www-form-urlencoded",
  //         },
  //       })
  //       .then((res) => {
  //         console.log(res.data);
  //         setOutput(res.data.translatedText);
  //       });
  //   };

  // useEffect(() => {
  //   axios
  //     .get("https://libretranslate.de/languages", {
  //       headers: { accept: "application/json" },
  //     })
  //     .then((res) => {
  //       console.log(res.data);
  //       setOptions(res.data);
  //     });
  // }, []);

  const onEnterPress = async (event) => {
    if (event.key === "Enter") {
      if (symptoms.length === 0) {
        toast.error("Please enter the symptoms");
        return;
      }
      setData(null);
      setLoading(true);
      try {
        const response = await axios.post(
          "http://localhost:5000/predictDisease",
          {
            symptoms: symptoms,
          }
        );
        console.log(response.data);
        const data = response.data;
        console.log(data.data);

        setData(data.data);
      } catch (error) {
        console.log(error);
      } finally {
        setLoading(false);
        setSymptoms("");
      }
    }
  };

  return (
    <div className="w-[60%] ml-auto mr-auto flex flex-col items-center ">
      {/* <div>
        From ({from}) :
        <select onChange={(e) => setFrom(e.target.value)}>
          {options.map((opt) => (
            <option key={opt.code} value={opt.code}>
              {opt.name}
            </option>
          ))}
        </select>
        To ({to}) :
        <select onChange={(e) => setTo(e.target.value)}>
          {options.map((opt) => (
            <option key={opt.code} value={opt.code}>
              {opt.name}
            </option>
          ))}
        </select>
      </div>
      <button onClick={(e) => translate()}>Translate</button> */}

      <div className="text-[26px] m-[10px] mb-[60px] font-medium border-b-[1px] border-[#ababad]">
        Crop Disease Prediction and Solution
      </div>
      <div className="flex flexcol min-h-[200px]">
        {data !== null && (
          <div className="flex flex-col w-full text-[24px]">
            <div className="text-[24px]">
              <span className="text-dark2 mr-[15px]">
                Symptoms &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:{" "}
              </span>
              {data.symptoms}
            </div>
            <div className="text-[24px] mt-[20px]">
              <span className="text-dark2 mr-[15px]">
                Disease Name &nbsp;:{" "}
              </span>
              {data.DiseaseName}
            </div>
            <div className="text-[24px] mt-[20px]">

              <span className="text-dark2 mr-[15px]">
                Treatments &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:{" "}
              </span>

            </div>
            <div className="flex flex-col gap-y-[15px] mt-[30px]">
              {data.Treatment.map((d, index) => {
                return (
                  <div className="flex flex-row gap-x-[10px]">
                    <div>{index + 1}.</div>
                    <div>
                      {d.treatmentName} : {d.treatment}
                      <div className='flex items-center'>
                        <img className='w-[20px] h-[20px] '
                          src='/assets/images/speaker.png'
                          onClick={() => speak({ text: d.treatment })}
                        />
                        <button className='w-[70px] h-[20px] p-[2px] text-[12px] rounded-[5px] ml-[10px] bg-orange-300 ' onClick={stopSpeaking} disabled={!speaking}>
                          Stop
                        </button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {loading && (
          <div className="flex flex-col gap-y-[10px] items-center justify-center m-auto text-[16px] text-[#606060]">
            <ScaleLoader color="#7C3AED" />
            Hold on!
          </div>
        )}
      </div>

      <input
        className="h-[50px] w-full ml-auto mr-auto  mb-[50px] rounded-[10px] bg-purple-light border-[1px] border-purple-dark px-[30px] box-border text-[#000000] outline-none mt-[50px]"
        placeholder="Enter The symptoms you are facing..."
        value={symptoms}
        onKeyDown={onEnterPress}
        onChange={(event) => {
          setSymptoms(event.target.value);
        }}
      />
    </div>
  );
};

export default PredictDiseaseFromSymptoms;
