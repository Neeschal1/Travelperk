import React from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../constants/navbar";

const Landing = () => {
  const navigate = useNavigate();
  return (
    <div className="flex items-center justify-center w-full">
      <Navbar />
    </div>
  );
};

export default Landing;
