const PDFViewer = () => {
  return (
    <div className="flex flex-wrap">
      {/* Left side (PDF Viewer) */}
      <div className="w-full md:w-7/12 p-4 h-full">
        {/* Replace the URL with the URL of your PDF */}
        <iframe
          src="/assets/AFFAIRE AVCIOgLU c. TÜRKiYE.pdf"
          width="100%"
          height="530"
          frameBorder="0"
          scrolling="no"
        />
      </div>

      {/* Right side (Text content) */}
      <div className="w-full md:w-5/12 p-4 flex flex-col">
        <h1 className="text-2xl font-bold mb-4">PDF Information</h1>
        <p>
          Here you can display text content, information, or any additional
          details related to the PDF you can display text content, information,
          or any additional details related to the .
        </p>
        <hr className="my-4" />
        <h1 className="text-xl font-medium">Simplify Legal Phrases</h1>
        <input
          type="text"
          name="price"
          id="price"
          className="h-[50px] w-full rounded-[10px] border-[1px] border-gray-200 px-[30px] box-border text-[#000000] outline-none my-[20px] focus:border-blue-300 focus:border-2"
          placeholder="Enter Text Here..."
        />
        <div
          style={{
            overflow: "auto",
            maxHeight: "230px",
          }}
          className="bg-gray-100 h-[230px] p-4 rounded-lg shadow-md"
        >
          It is a long established fact that a reader will be distracted by the
          readable content of a page when looking at its layout. The point of
          using Lorem Ipsum is that it has a more-or-less normal distribution of
          letters, as opposed to using 'Content here, content here', making it
          look like readable English. Many desktop publishing
        </div>
      </div>
    </div>
  );
};

export default PDFViewer;
