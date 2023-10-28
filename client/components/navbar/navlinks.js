"use client";

import { useRouter } from "next/navigation";

const Navlinks = ({ link, text, logo }) => {
  const Router = useRouter();
  const { pathname } = Router;

  const onClickHandler = () => {
    if (pathname == "/" + link) {
      return;
    } else if (link == "Logout") {
    } else {
      Router.push("/" + link);
    }
  };
  console.log(pathname);

  return (
    <div
      className={`flex flex-row gap-x-[20px] font-medium px-[16px] py-[8px] box-border items-center ${
        pathname == "/" + link && "bg-purple-light fade-bg"
      }  rounded-[10px] cursor-pointer`}
      onClick={onClickHandler}
    >
      <img className="h-[20px]" src={`/assets/icon/${logo}`} alt="navicon" />
      <div>{text}</div>
    </div>
  );
};

export default Navlinks;
