import { useState } from "react";

import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="">
      <Navbar />
      <Home />
      <Footer />
    </div>
  );
}

export default App;
