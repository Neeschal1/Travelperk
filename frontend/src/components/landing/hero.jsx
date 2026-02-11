import React from "react";
import hero from "../../assets/images/hero.jpg";
import Navbar from "../../constants/navbar";

const Hero = () => {
  return (
    <div
      style={{ backgroundImage: `url(${hero})` }}
      className="flex flex-col h-screen bg-no-repeat bg-cover bg-center relative gap-20"
    >
      <Navbar className="z-10 relative" />
      <div className="p-10 gap-5 flex-col flex">
        <div className="flex flex-col">
          <h1 className="text-white font-semibold text-7xl">
            Discover the
            <br />
            World, One <br />
            Journey at a Time
          </h1>
          <p className="text-gray-300">
            Embark on unforgettable adventures and explore new horizons. Let
            every journey <br />
            inspire you, connect you to the world, and create memories that last
            a lifetime.
          </p>
        </div>
        <button className="bg-blue-400 text-white font-regular px-8 py-4 rounded-full hover:bg-blue-600 transition self-start hover:cursor-pointer">
          Get Started
        </button>
      </div>
    </div>
  );
};

export default Hero;
