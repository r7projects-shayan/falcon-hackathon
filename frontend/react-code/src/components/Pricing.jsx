import React from "react";

const Pricing = () => {
  return (
    <section id="pricing" className="py-10 bg-white sm:py-16 lg:py-24">
      <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
        <div className="max-w-xl mx-auto text-center">
          <span className="relative inline-flex">
            <span className="absolute inset-x-0 bottom-0 border-b-[30px] border-[#a5ffc6]"></span>
            <span className="relative text-4xl font-bold text-black sm:text-6xl lg:text-7xl">
              Pricing
            </span>
          </span>
          <p className="mt-12 text-lg leading-relaxed text-gray-600">
            Get familiar with our pricing plans
          </p>
        </div>

        {/* lg+ */}
        <div className="hidden mt-16 lg:block">
          <table className="w-full">
            <thead>
              <tr>
                <th className="py-8 pr-4"></th>
                <th className="px-4 py-8 text-center">
                  <span className="text-base font-medium text-blue-600">
                    {" "}
                    Free{" "}
                  </span>
                  <p className="mt-6 text-6xl font-bold">$0</p>
                  <p className="mt-2 text-base font-normal text-gray-500">
                    Per month
                  </p>
                </th>
                <th className="px-4 py-8 text-center">
                  <span className="text-base font-medium text-blue-600">
                    {" "}
                    Individuals{" "}
                  </span>
                  <p className="mt-6 text-6xl font-bold">$150</p>
                  <p className="mt-2 text-base font-normal text-gray-500">
                    Per month
                  </p>
                </th>
                <th className="px-4 py-8 text-center bg-gray-900 rounded-t-xl">
                  <span className="px-4 py-2 text-base font-medium text-white bg-blue-600 rounded-full">
                    {" "}
                    Popular{" "}
                  </span>
                  <p className="mt-6 text-6xl font-bold text-white">$250</p>
                  <p className="mt-2 text-base font-normal text-gray-200">
                    Per month
                  </p>
                </th>
                <th className="px-4 py-8 text-center">
                  <span className="text-base font-medium text-blue-600">
                    {" "}
                    Enterprise and Hospitals{" "}
                  </span>
                  <p className="mt-6 text-6xl font-bold">$850</p>
                  <p className="mt-2 text-base font-normal text-gray-500">
                    Per month
                  </p>
                </th>
              </tr>
            </thead>

            <tbody>
              {/* Example Row */}
              <tr>
                <td className="py-4 pr-4 font-medium border-b border-gray-200">
                  Credits
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  200
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  600
                </td>
                <td className="px-4 py-4 text-center text-white bg-gray-900 border-b border-white/20">
                  1000
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  5000
                </td>
              </tr>
              {/* Repeat for other rows */}
            </tbody>
            <tbody>
              {/* Example Row */}
              <tr>
                <td className="py-4 pr-4 font-medium border-b border-gray-200">
                  Access to core features
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
                <td className="px-4 py-4 text-center text-white bg-gray-900 border-b border-white/20">
                  ✅
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
              </tr>
              {/* Repeat for other rows */}
            </tbody>
            <tbody>
              {/* Example Row */}
              <tr>
                <td className="py-4 pr-4 font-medium border-b border-gray-200">
                  Advanced Diagnostic tools
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ❌
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
                <td className="px-4 py-4 text-center text-white bg-gray-900 border-b border-white/20">
                  ✅
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
              </tr>
              {/* Repeat for other rows */}
            </tbody>
            <tbody>
              {/* Example Row */}
              <tr>
                <td className="py-4 pr-4 font-medium border-b border-gray-200">
                  Affiliate Plan
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ❌
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ❌
                </td>
                <td className="px-4 py-4 text-center text-white bg-gray-900 border-b border-white/20">
                  ✅
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
              </tr>
              {/* Repeat for other rows */}
            </tbody>
            <tbody>
              {/* Example Row */}
              <tr>
                <td className="py-4 pr-4 font-medium border-b border-gray-200">
                  Priority Customer Support 24/7
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ❌
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
                <td className="px-4 py-4 text-center text-white bg-gray-900 border-b border-white/20">
                  ✅
                </td>
                <td className="px-4 py-4 text-center border-b border-gray-200">
                  ✅
                </td>
              </tr>
              {/* Repeat for other rows */}
            </tbody>
          </table>
        </div>

        {/* xs to lg */}
        <div className="block mt-12 border-t border-b border-gray-200 divide-y divide-gray-200 lg:hidden">
          <div className="grid grid-cols-4 text-center divide-x divide-gray-200">
            <div className="px-2 py-2">
              <span className="text-sm font-medium text-blue-600"> Free </span>
              <p className="mt-2 text-xl font-bold">$0</p>
              <span className="mt-1 text-sm font-normal text-gray-500">
                {" "}
                Per month{" "}
              </span>
            </div>
            <div className="px-2 py-2">
              <span className="text-sm font-medium text-blue-600"> Team </span>
              <p className="mt-2 text-xl font-bold">$99</p>
              <span className="mt-1 text-sm font-normal text-gray-500">
                {" "}
                Per month{" "}
              </span>
            </div>
            <div className="px-2 py-2">
              <span className="text-sm font-medium text-blue-600">
                {" "}
                Popular{" "}
              </span>
              <p className="mt-2 text-xl font-bold">$150</p>
              <span className="mt-1 text-sm font-normal text-gray-500">
                {" "}
                Per month{" "}
              </span>
            </div>
            <div className="px-2 py-2">
              <span className="text-sm font-medium text-blue-600">
                {" "}
                Enterprise{" "}
              </span>
              <p className="mt-2 text-xl font-bold">$490</p>
              <span className="mt-1 text-sm font-normal text-gray-500">
                {" "}
                Per month{" "}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Pricing;
