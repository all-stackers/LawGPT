"use client"
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  
    // Log the selected file to the console
    console.log(selectedFile);
  };
  // const uploadPdfFormData = () => {
  //   console.log("suuccess");
   
  //   if (file) {
  //     console.log(loading);

  //     var formdata = new FormData();
  //     formdata.append("file", file, "[PROXY]");

  //     var requestOptions = {
  //       method: "POST",
  //       body: formdata,
  //       redirect: "follow",
  //     };

  //     fetch("http://localhost:5000/upload", requestOptions)
  //       .then((response) => response.json())
  //       .then((result) => {
  //         console.log("success")
  //         // console.log(result?.data?.index_id);
  //         console.log(result)

      
  //       })
  //       .catch((error) => console.log("error", error));
  //     }
  // };
  const handleUpload = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", file, "[PROXY]");
    console.log(formData);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log("res",response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      {/* <input type="file" name="pdf" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload PDF</button> */}
      <form encType="multipart/form-data" onSubmit={handleUpload}>
  <input type="file" name="pdf" onChange={handleFileChange} />

  <button type="submit">Submit</button>
</form>
    </div>
  );
}

export default App;
