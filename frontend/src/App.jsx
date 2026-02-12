import { useState } from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import Signup from "./pages/signup";
import Landing from "./pages/landing";

const App = () => {
  return (
    <Router>
      <div className="h-screen w-full">
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
