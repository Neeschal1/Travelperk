import React from "react";
import { FaPhoneAlt } from "react-icons/fa";
import { FaMagnifyingGlass } from "react-icons/fa6";

const Navbar = () => {
  return (
    <div className="flex flex-row justify-between align-center w-full items-start p-10">
      {/* Call Details */}
      <div className="flex gap-3 items-center justify-center">
        <div className="bg-blue-500 p-3 rounded-full">
          <FaPhoneAlt size={24} color="white" />
        </div>
        <div className="flex flex-col items-start">
          <h1 className="text-gray-300">Call Anytime</h1>
          <h1 className="font-medium text-xl text-white">+977 9867418552</h1>
        </div>
      </div>

      {/* Travelperk */}
      <h1 className="flex mt-3 font-semibold text-white text-2xl">
        travel
        <span className="font-semibold text-2xl text-blue-500">perk</span>
      </h1>

      {/* Accounts action */}
      <div className="flex flex-row gap-3 items-center">
        <div className="relative w-60">
          <FaMagnifyingGlass
            size={20}
            color="gray"
            className="absolute left-5 top-1/2 transform -translate-y-1/2"
          />
          <input
            type="text"
            className="pl-12 pr-3 py-4 px-3 bg-gray-200 rounded-full w-full"
            placeholder="Search anything..."
          />
        </div>
        <button className="flex  font-regular border border-blue-400 text-white w-30 justify-center py-4 hover:cursor-pointer hover:bg-blue-600 hover:text-white duration-400 rounded-4xl">
          Login
        </button>
        <button className="flex bg-blue-400 font-regular text-white w-30 justify-center py-4 hover:cursor-pointer hover:bg-blue-600 duration-400 rounded-4xl">
          Signup
        </button>
      </div>
    </div>
  );
};

export default Navbar;
