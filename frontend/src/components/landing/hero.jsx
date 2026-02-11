import React from "react";
import hero from "../../assets/images/hero.jpg";
import Navbar from "../../constants/navbar";

const Hero = () => {
  return (
    <div
      style={{ backgroundImage: `url(${hero})` }}
      className="flex flex-col w-full h-screen bg-no-repeat bg-cover bg-center relative"
    >
      <Navbar className="z-10 relative" />
    </div>
  );
};

export default Hero;
