import React from "react";
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const navigate = useNavigate();
  return (
    <div className="flex items-center justify-center">
      <button
        className="bg-black text-white"
        onClick={() => {
          navigate("/login");
        }}
      >
        Login
      </button>
      <button
        className="bg-black text-white"
        onClick={() => {
          navigate("/signup");
        }}
      >
        Signup
      </button>
      <br />
      <h1 className="text-2xl text-black">Hello Pulu 🔥</h1>
    </div>
  );
};

export default Landing;
