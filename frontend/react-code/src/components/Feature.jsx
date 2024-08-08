import React from "react";

const Feature = () => {
  return (
    <div>
      <section id="features" class="py-12 bg-white sm:py-16 lg:py-20">
        <div class="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div class="text-center">
            <span className="relative inline-flex">
              <span className="absolute inset-x-0 bottom-0 border-b-[30px] border-[#7cdaff]"></span>
              <span className="relative text-4xl font-bold text-black sm:text-6xl lg:text-7xl">
                Features We Provide
              </span>
            </span>
            <p class="mt-4 text-base leading-7 text-gray-600 sm:mt-8 font-pj">
              World's most advanced Healthcare Automation System
            </p>
          </div>

          <div class="grid grid-cols-1 mt-10 text-center sm:mt-16 sm:grid-cols-2 sm:gap-x-12 gap-y-12 md:grid-cols-3 md:gap-0 xl:mt-24">
            <div class="md:p-8 lg:p-14">
              <svg
                class="mx-auto"
                width="46"
                height="46"
                viewBox="0 0 46 46"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M45 29V23C45 10.85 35.15 1 23 1C10.85 1 1 10.85 1 23V29"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M13 29H1V41C1 43.209 2.791 45 5 45H13V29Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M45 29H33V45H41C43.209 45 45 43.209 45 41V29Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <h3 class="mt-12 text-xl font-bold text-gray-900 font-pj">
                Doctor Handwriting Analysis
              </h3>
              <p class="mt-5 text-base text-gray-600 font-pj">
                Automatically extract and digitize doctor notes from handwritten
                images to streamline record-keeping and analysis.
              </p>
            </div>

            <div class="md:p-8 lg:p-14 md:border-l md:border-gray-200">
              <svg
                class="mx-auto"
                width="46"
                height="46"
                viewBox="0 0 46 46"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M27 27H19V45H27V27Z"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M9 37H1V45H9V37Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M45 17H37V45H45V17Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M5 17L15 7L23 15L37 1"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M28 1H37V10"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <h3 class="mt-12 text-xl font-bold text-gray-900 font-pj">
                Disease Detection and Classification
              </h3>
              <p class="mt-5 text-base text-gray-600 font-pj">
                Utilize AI to analyze medical images for rapid and accurate
                disease identification and classification.
              </p>
            </div>

            <div class="md:p-8 lg:p-14 md:border-l md:border-gray-200">
              <svg
                class="mx-auto"
                width="42"
                height="42"
                viewBox="0 0 42 42"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M41 1H1V41H41V1Z"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M18 7H7V20H18V7Z"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M18 26H7V35H18V26Z"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M35 7H24V35H35V7Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <h3 class="mt-12 text-xl font-bold text-gray-900 font-pj">
                Symptom Analysis
              </h3>
              <p class="mt-5 text-base text-gray-600 font-pj">
                Input symptom images and text to receive quick, AI-driven
                diagnostic suggestions, improving diagnosis speed and accuracy.
              </p>
            </div>

            <div class="md:p-8 lg:p-14 md:border-t md:border-gray-200">
              <svg
                class="mx-auto"
                width="42"
                height="42"
                viewBox="0 0 42 42"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M9.66667 25H6C3.23858 25 1 27.2386 1 30V37C1 39.7614 3.23858 42 6 42H36C38.7614 42 41 39.7614 41 37V30C41 27.2386 38.7614 25 36 25H31.8333C30.2685 25 29 26.2685 29 27.8333C29 29.3981 27.7315 30.6667 26.1667 30.6667H15.3333C13.7685 30.6667 12.5 29.3981 12.5 27.8333C12.5 26.2685 11.2315 25 9.66667 25Z"
                  fill="#D4D4D8"
                />
                <path
                  d="M9 9H33"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M9 17H33"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M1 25H13V31H29V25H41"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M37 1H5C2.79086 1 1 2.79086 1 5V37C1 39.2091 2.79086 41 5 41H37C39.2091 41 41 39.2091 41 37V5C41 2.79086 39.2091 1 37 1Z"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <h3 class="mt-12 text-xl font-bold text-gray-900 font-pj">
                Data Security and Compliance
              </h3>
              <p class="mt-5 text-base text-gray-600 font-pj">
                Ensure patient data is secure and complies with all relevant
                healthcare regulations and standards.
              </p>
            </div>

            <div class="md:p-8 lg:p-14 md:border-l md:border-gray-200 md:border-t">
              <svg
                class="mx-auto"
                width="46"
                height="42"
                viewBox="0 0 46 42"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M30.562 18.4609C30.0511 17.9392 29.4292 17.5392 28.7426 17.2907C28.0559 17.0422 27.3221 16.9516 26.5956 17.0256C25.8692 17.0996 25.1687 17.3362 24.5462 17.718C23.9237 18.0998 23.3952 18.6169 23 19.2309C22.6049 18.6167 22.0764 18.0995 21.4539 17.7176C20.8315 17.3357 20.1309 17.099 19.4044 17.025C18.6779 16.951 17.944 17.0417 17.2573 17.2903C16.5706 17.5389 15.9488 17.939 15.438 18.4609C14.5163 19.4035 14.0002 20.6695 14.0002 21.9879C14.0002 23.3063 14.5163 24.5722 15.438 25.5149L23 33.1999L30.564 25.5159C31.485 24.5726 32.0004 23.3064 32 21.988C31.9997 20.6696 31.4835 19.4037 30.562 18.4609Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M41 41H5C3.93913 41 2.92172 40.5786 2.17157 39.8284C1.42143 39.0783 1 38.0609 1 37V1H17L22 9H45V37C45 38.0609 44.5786 39.0783 43.8284 39.8284C43.0783 40.5786 42.0609 41 41 41Z"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <h3 class="mt-12 text-xl font-bold text-gray-900 font-pj">
                User Friendly Interface
              </h3>
              <p class="mt-5 text-base text-gray-600 font-pj">
                Navigate our intuitive interface with ease, designed to
                integrate seamlessly into your existing workflow.
              </p>
            </div>

            <div class="md:p-8 lg:p-14 md:border-l md:border-gray-200 md:border-t">
              <svg
                class="mx-auto"
                width="44"
                height="44"
                viewBox="0 0 44 44"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M25 7C34.941 7 43 15.059 43 25C43 34.941 34.941 43 25 43C15.059 43 7 34.941 7 25"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M19 1C9.059 1 1 9.059 1 19H19V1Z"
                  fill="#D4D4D8"
                  stroke="#161616"
                  stroke-width="2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <h3 class="mt-12 text-xl font-bold text-gray-900 font-pj">
                Future Ready Technology
              </h3>
              <p class="mt-5 text-base text-gray-600 font-pj">
                Our roadmap includes powerful features like drug analysis and
                outbreak detection to help you stay ahead of healthcare
                challenges.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="py-10 bg-white sm:py-16 lg:py-24">
        <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div className="max-w-2xl mx-auto text-center">
            <span className="relative inline-flex">
              <span className="absolute inset-x-0 bottom-0 border-b-[30px] border-[#ffec84]"></span>
              <span className="relative text-4xl font-bold text-black sm:text-6xl lg:text-7xl">
                How does it work?
              </span>
            </span>
          </div>

          <div className="relative mt-12 lg:mt-20">
            <div className="absolute inset-x-0 hidden xl:px-44 top-2 md:block md:px-20 lg:px-28">
              <img
                className="w-full"
                src="https://cdn.rareblocks.xyz/collection/celebration/images/steps/2/curved-dotted-line.svg"
                alt=""
              />
            </div>

            <div className="relative grid grid-cols-1 text-center gap-y-12 md:grid-cols-3 gap-x-12">
              <div>
                <div className="flex items-center justify-center w-16 h-16 mx-auto bg-white border-2 border-gray-200 rounded-full shadow">
                  <span className="text-xl font-semibold text-gray-700">
                    {" "}
                    1{" "}
                  </span>
                </div>
                <h3 className="mt-6 text-xl font-semibold leading-tight text-black md:mt-10">
                  Upload Images and Text
                </h3>
                <p className="mt-4 text-base text-gray-600">
                  Easily upload images of handwritten notes, medical images, or
                  symptom descriptions.
                </p>
              </div>

              <div>
                <div className="flex items-center justify-center w-16 h-16 mx-auto bg-white border-2 border-gray-200 rounded-full shadow">
                  <span className="text-xl font-semibold text-gray-700">
                    {" "}
                    2{" "}
                  </span>
                </div>
                <h3 className="mt-6 text-xl font-semibold leading-tight text-black md:mt-10">
                  AI Powered Analysis
                </h3>
                <p className="mt-4 text-base text-gray-600">
                  Our advanced AI algorithms analyze the inputs to extract
                  meaningful insights and identify patterns.
                </p>
              </div>

              <div>
                <div className="flex items-center justify-center w-16 h-16 mx-auto bg-white border-2 border-gray-200 rounded-full shadow">
                  <span className="text-xl font-semibold text-gray-700">
                    {" "}
                    3{" "}
                  </span>
                </div>
                <h3 className="mt-6 text-xl font-semibold leading-tight text-black md:mt-10">
                  Instant Results
                </h3>
                <p className="mt-4 text-base text-gray-600">
                  Receive instant, accurate results on disease classification
                  and potential diagnoses to assist in decision-making.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Feature;
