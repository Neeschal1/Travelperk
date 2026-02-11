import { useState } from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Login from "./pages/login";
import Signup from "./pages/signup";
import Landing from "./pages/landing";

const App = () => {
  return (
    <Router>
      <div className="flex h-screen w-full">
        <Routes>
          <Route path="/" element={ <Landing /> } />
          <Route path="/login" element={ <Login /> } />
          <Route path="/signup" element={ <Signup /> } />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
