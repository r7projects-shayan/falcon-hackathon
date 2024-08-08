import React, { useState } from "react";

const Faq = () => {
  const [faq, setFaq] = useState([
    {
      question: "What is Mediscape?",
      answer:
        "Mediscape is an AI-powered healthcare automation system designed to assist doctors with various tasks, such as analyzing handwritten notes, detecting diseases from medical images, and providing diagnostic insights based on symptoms. Our platform integrates advanced AI technology to streamline workflows and enhance patient care.",
      open: false,
    },
    {
      question: "How does Mediscape analyze doctor handwriting?",
      answer:
        "Mediscape uses state-of-the-art optical character recognition (OCR) and machine learning algorithms to accurately digitize and interpret handwritten notes. This feature helps doctors save time and reduces errors in patient record management by converting handwritten text into easily searchable digital documents.",
      open: false,
    },
    {
      question: "Can Mediscape detect all types of diseases from images?",
      answer:
        "While Mediscape is equipped with advanced AI models capable of identifying and classifying a wide range of diseases from medical images, its accuracy is continually being improved. Our system is trained on extensive datasets to provide reliable diagnostic suggestions, but it is always recommended to use it in conjunction with professional medical judgment.",
      open: false,
    },
    {
      question: "What future features can I expect from Mediscape?",
      answer:
        "We are continuously working on expanding Mediscapes capabilities. Upcoming features include drug analysis, which will assist in understanding drug interactions and effects, and an outbreak detection system that will help identify and respond to potential health crises quickly and effectively.",
      open: false,
    },
  ]);

  const toggleFaq = (index) => {
    setFaq(
      faq.map((item, i) => {
        if (i === index) {
          item.open = !item.open;
        } else {
          item.open = false;
        }

        return item;
      })
    );
  };

  return (
    <section className="py-10 bg-gray-50 sm:py-16 lg:py-24">
      <div className="px-4 mx-auto sm:px-6 lg:px-8 max-w-7xl">
        <div className="max-w-2xl mx-auto text-center">
          <span className="relative inline-flex">
            <span className="absolute inset-x-0 bottom-0 border-b-[30px] border-[#9de2ff]"></span>
            <span className="relative text-4xl font-bold text-black sm:text-6xl lg:text-7xl">
              Frequenty Asked Questions
            </span>
          </span>
          <p className="max-w-xl mx-auto mt-4 text-base leading-relaxed text-gray-600"></p>
        </div>

        <div className="max-w-3xl mx-auto mt-8 space-y-4 md:mt-16">
          {faq.map((item, index) => (
            <div
              key={index}
              className="transition-all duration-200 bg-white border border-gray-200 cursor-pointer hover:bg-gray-50"
            >
              <button
                type="button"
                className="flex items-center justify-between w-full px-4 py-5 sm:p-6"
                onClick={() => toggleFaq(index)}
              >
                <span className="flex text-lg font-semibold text-black">
                  {" "}
                  {item.question}{" "}
                </span>

                <svg
                  className={`w-6 h-6 text-gray-400 ${
                    item.open ? "rotate-180" : ""
                  }`}
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M19 9l-7 7-7-7"
                  />
                </svg>
              </button>

              <div
                className={`${
                  item.open ? "block" : "hidden"
                } px-4 pb-5 sm:px-6 sm:pb-6`}
              >
                <p dangerouslySetInnerHTML={{ __html: item.answer }}></p>
              </div>
            </div>
          ))}
        </div>

        <p className="text-center text-gray-600 textbase mt-9">
          Didn’t find the answer you are looking for?{" "}
          <a
            href="#"
            title=""
            className="font-medium text-blue-600 transition-all duration-200 hover:text-blue-700 focus:text-blue-700 hover:underline"
          >
            Contact our support
          </a>
        </p>
      </div>
    </section>
  );
};

export default Faq;
