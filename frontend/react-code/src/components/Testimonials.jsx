import React from "react";

const TestimonialCard = ({ avatar, name, title, review }) => (
  <div className="flex flex-col overflow-hidden shadow-xl">
    <div className="flex flex-col justify-between flex-1 p-6 bg-white lg:py-8 lg:px-7">
      <div className="flex-1">
        <div className="flex items-center">
          {[...Array(5)].map((_, i) => (
            <svg
              key={i}
              className="w-5 h-5 text-[#FDB241]"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
          ))}
        </div>

        <blockquote className="flex-1 mt-8">
          <p className="text-lg leading-relaxed text-gray-900 font-pj">
            {review}
          </p>
        </blockquote>
      </div>

      <div className="flex items-center mt-8">
        <img
          className="flex-shrink-0 object-cover rounded-full w-11 h-11"
          src={avatar}
          alt={name}
        />
        <div className="ml-4">
          <p className="text-base font-bold text-gray-900 font-pj">{name}</p>
          <p className="mt-0.5 text-sm font-pj text-gray-600">{title}</p>
        </div>
      </div>
    </div>
  </div>
);

const Testimonials = () => {
  const testimonials = [
    {
      avatar:
        "https://plus.unsplash.com/premium_photo-1690407617686-d449aa2aad3c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      name: "Dr. Sarah Thompson",
      title: "Cardiologist",
      review:
        "Mediscape has revolutionized the way I interact with patient data. The handwriting analysis feature alone has saved me countless hours and improved my accuracy in patient record management.",
    },
    {
      avatar:
        "https://plus.unsplash.com/premium_photo-1661745702156-cd4b0382455f?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      name: "Dr. John Lee",
      title: "General Practitioner",
      review:
        "The AI-powered disease detection system in Mediscape has become an invaluable tool in my practice. It provides me with accurate insights quickly, allowing me to focus more on patient care",
    },
    {
      avatar:
        "https://images.unsplash.com/photo-1616776005756-4dca36124bf9?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      name: "Dr. Emily Grant",
      title: "General Physician",
      review:
        "I can't imagine going back to my old methods after using Mediscape. The symptom analysis feature has enhanced my diagnostic capabilities and improved my patient outcomes",
    },
  ];

  return (
    <section className="py-12 bg-gray-50 sm:py-16 lg:py-20">
      <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
        <div className="flex flex-col items-center">
          <div className="text-center">
            <span className="relative inline-flex">
              <span className="absolute inset-x-0 bottom-0 border-b-[30px] border-[#e1baff]"></span>
              <span className="relative text-4xl font-bold text-black sm:text-6xl lg:text-7xl">
                Testimonials
              </span>
            </span>
          </div>

          <div className="mt-8 text-center md:mt-16 md:order-3">
            <a
              href="#"
              className="pb-2 text-base font-bold leading-7 text-gray-900 transition-all duration-200 border-b-2 border-gray-900 hover:border-gray-600 font-pj focus:outline-none focus:ring-1 focus:ring-gray-900 focus:ring-offset-2 hover:text-gray-600"
            >
              Check all 2,157 reviews
            </a>
          </div>

          <div className="relative mt-10 md:mt-24 md:order-2">
            <div className="absolute -inset-x-1 inset-y-16 md:-inset-x-2 md:-inset-y-6">
              <div
                className="w-full h-full max-w-5xl mx-auto rounded-3xl opacity-30 blur-lg filter"
                style={{
                  background:
                    "linear-gradient(90deg, #44ff9a -0.55%, #44b0ff 22.86%, #8b44ff 48.36%, #ff6644 73.33%, #ebff70 99.34%)",
                }}
              />
            </div>

            <div className="relative grid max-w-lg grid-cols-1 gap-6 mx-auto md:max-w-none lg:gap-10 md:grid-cols-3">
              {testimonials.map((testimonial, index) => (
                <TestimonialCard key={index} {...testimonial} />
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Testimonials;
