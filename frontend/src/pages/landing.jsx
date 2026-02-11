import React from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "../constants/navbar";
import Hero from "../components/landing/hero";

const Landing = () => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col w-full">
      
      <Hero />
    </div>
  );
};

export default Landing;
