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

      {/* main pages nav links */}
      <div className="flex flex-col gap-y-[12px] text-[14px] mt-[40px]">
        <Navlinks link="MyFiles" logo="myFiles.svg" text="My Files" />
        <Navlinks link="Recent" logo="recent.svg" text="Recent" />
        <Navlinks link="Search" logo="search.svg" text="Search media" />
        {/* <Navlinks link="Developer" logo="developer.svg" text="Developer"/> */}
      </div>

      <div className="w-full h-[1px] bg-gray my-[30px]"></div>
      <div className="flex flex-col gap-y-[12px] text-[14px]">
        <Navlinks link="settings" logo="settings.svg" text="Settings" />
        {/* <Navlinks link="Logout" logo="logout.svg" text="Logout"/> */}
      </div>
    </div>
  );
};

export default Navbar;
