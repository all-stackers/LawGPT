import Navlinks from "./navlinks";

const Navbar = () => {
  return (
    <div className="min-w-[20%] w-[20%] border-r-[1px] border-gray bg-gray-200 h-[100vh] flex flex-col px-[21px] py-[20px] box-border font-Inter">
      <div className="flex flex-col gap-y-[0px] justify-center box-border">
        <div className="flex flex-row gap-x-[5px] text-[22px] items-center font-medium font-Lexend">
          <img
            className="h-[50px]"
            src="/assets/images/law-book.png"
            alt="logo"
          />
          <p>LawYantra.AI</p>
        </div>
        <div className="flex flex-row gap-x-[5px] px-[30px] text-[#57534E] mt-[-10px] text-[10px] justify-end">
          <div>Built for Datahack 2.0</div>
        </div>
      </div>

      <div className="flex flex-col gap-y-[12px] text-[14px] mt-[40px]">
        <Navlinks link="chats" logo="chat.svg" text="Chats" />
        <Navlinks link="AskAi" logo="ai.svg" text="Ask AI" />
        <Navlinks
          link="translation"
          logo="translate.svg"
          text="Translate & Save PDF"
        />
        <Navlinks
          link="ocr"
          logo="scanner.svg"
          text="OCR Images"
        />
        <Navlinks link="query-chat" logo="query.svg" text="Query" />
      </div>

      {/* <div className="w-full h-[1px] bg-gray my-[20px]"></div> */}
      <div className="mt-auto mb-10 flex flex-row justify-between  text-[14px]">
        <Navlinks link="profile" logo="profile.svg" text="Profile" />
        {/* <Navlinks link="Logout" logo="logout.svg" text="" /> */}
      </div>
    </div>
  );
};

export default Navbar;
