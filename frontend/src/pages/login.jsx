import React, { useState } from "react";
import europebanner from "../assets/images/europe.jpg";
import { FaRegEyeSlash } from "react-icons/fa6";
import { TbLockPassword } from "react-icons/tb";
import { IoEyeOutline } from "react-icons/io5";
import { MdEmail } from "react-icons/md";
import loginbanner from "../assets/images/login.jpg";

const Login = () => {
  const [seepassword, setSeePassword] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSeePassword = () => {
    if (!seepassword) {
      setSeePassword(true);
    } else {
      setSeePassword(false);
    }
  };

  const handleLogin = () => {
    console.log("Data: \nEmail: ", email, "Password: ", password)
  }

  return (
    <div
      style={{ backgroundImage: `url(${europebanner})` }}
      className="flex w-full object-cover bg-cover bg-no-repeat h-screen"
    >
      <div className="bg-white/30 backdrop-blur-sm flex w-full h-full justify-center items-center">
        <div className="bg-white flex flex-row items-center rounded-3xl w-7/12">
          <div className="flex flex-col w-full items-center">
            <div className="flex py-10 px-10 w-full flex-col gap-10">
            <div className="flex flex-col">
              <h1 className="flex mt-3 font-semibold text-black text-2xl">
                travel
                <span className="font-semibold text-2xl text-blue-500">
                  perk
                </span>
              </h1>
              <h2>Enter your account's detail in order to continue</h2>
            </div>
            <div className="flex flex-col gap-5 w-full">
              <div>
                <h1>Email</h1>
                <div className="relative w-full">
                  <MdEmail
                    size={20}
                    color="gray"
                    className="absolute left-5 top-1/2 transform -translate-y-1/2"
                  />
                  <input
                    value={email}
                    onChange={(e) => {
                      setEmail(e.target.value);
                    }}
                    type="text"
                    className="pl-12 pr-3 py-4 mt-2 px-6 bg-gray-100 rounded-full w-full"
                    placeholder="Enter your email here"
                  />
                </div>
              </div>
              <div>
                <h1>Password</h1>
                <div className="relative w-full">
                  <TbLockPassword
                    size={20}
                    color="gray"
                    className="absolute left-5 top-1/2 -translate-y-1/2"
                  />

                  <input
                    value={password}
                    onChange={(e) => {
                      setPassword(e.target.value);
                    }}
                    type={seepassword ? "text" : "password"}
                    className="pl-12 pr-12 py-4 mt-2 bg-gray-100 rounded-full w-full"
                    placeholder="Enter your Password"
                  />

                  <button
                    type="button"
                    onClick={handleSeePassword}
                    className="absolute right-5 mt-9 -translate-y-1/2 text-gray-500"
                  >
                    {seepassword ? (
                      <IoEyeOutline size={20} />
                    ) : (
                      <FaRegEyeSlash size={20} />
                    )}
                  </button>
                </div>
              </div>
            </div>
            <button onClick={handleLogin} className="bg-blue-400 hover:bg-blue-600 hover:cursor-pointer text-white py-3 rounded-full font-regular duration-400">
              Login
            </button>
          </div>
          <h1 className="pt-30">New to traveperk? <a href="http://localhost:5173/signup">Signup</a></h1>
          <p className="mt-5"><strong>Travelperk.</strong> all rights reserved</p>
          </div>
          <img
            className="h-200 w-full relative rounded-br-3xl rounded-tr-3xl"
            src={loginbanner}
          />
        </div>
      </div>
    </div>
  );
};

export default Login;
