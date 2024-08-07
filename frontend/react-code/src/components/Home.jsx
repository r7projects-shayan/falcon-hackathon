import React from "react";
import Hero from "./Hero";

import Feature from "./Feature";

import Testimonials from "./Testimonials";
import Faq from "./Faq";
import Team from "./Team";
import About from "./About";
import Pricing from "./Pricing";
import Contact from "./Contact";

const Home = () => {
  return (
    <div className="main-home">
      <Hero />
      <Feature />
      <About />
      <Testimonials />
      <Team />
      <Pricing />
      <Faq />
      <Contact />
    </div>
  );
};

export default Home;
