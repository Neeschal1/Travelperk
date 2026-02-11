import React from "react";
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const navigate = useNavigate();
  return (
    <div className="flex items-center justify-center">
      <button
        className="bg-black"
        onClick={() => {
          navigate("/login");
        }}
      >
        Login
      </button>
      <button
        className="bg-black"
        onClick={() => {
          navigate("/signup");
        }}
      >
        Signup
      </button>
    </div>
  );
};

export default Landing;
