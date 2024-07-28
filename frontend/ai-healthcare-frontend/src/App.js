import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { User } from 'lucide-react';

// Placeholder components
const Dashboard = () => <div className="p-4">Dashboard Content</div>;
const ChatbotDiagnosis = () => <div className="p-4">Chatbot Diagnosis Interface</div>;
const DrugIdentification = () => <div className="p-4">Drug Identification Interface</div>;
const RemoteConsultation = () => <div className="p-4">Remote Consultation Interface</div>;
const OutbreakAlert = () => <div className="p-4">Outbreak Alert System</div>;

const Sidebar = () => (
  <div className="bg-gray-800 text-white w-64 space-y-6 py-7 px-2 absolute inset-y-0 left-0 transform -translate-x-full md:relative md:translate-x-0 transition duration-200 ease-in-out">
    <nav>
      <Link to="/" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 hover:text-white">
        Dashboard
      </Link>
      <Link to="/chatbot" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 hover:text-white">
        Chatbot Diagnosis
      </Link>
      <Link to="/drug-id" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 hover:text-white">
        Drug Identification
      </Link>
      <Link to="/consultation" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 hover:text-white">
        Remote Consultation
      </Link>
      <Link to="/outbreak" className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 hover:text-white">
        Outbreak Alert
      </Link>
    </nav>
  </div>
);

const Header = () => (
  <header className="bg-white shadow-md">
    <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
      <h1 className="text-3xl font-bold text-gray-900">AI Healthcare Solution</h1>
      <div className="flex items-center">
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          New Consultation
        </button>
        <div className="ml-3 relative">
          <div>
            <button className="max-w-xs bg-gray-800 rounded-full flex items-center text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white" id="user-menu" aria-haspopup="true">
              <span className="sr-only">Open user menu</span>
              <User className="h-8 w-8 rounded-full" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </header>
);

const App = () => {
  return (
    <Router>
      <div className="flex h-screen bg-gray-100">
        <Sidebar />
        <div className="flex-1 flex flex-col overflow-hidden">
          <Header />
          <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200">
            <div className="container mx-auto px-6 py-8">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/chatbot" element={<ChatbotDiagnosis />} />
                <Route path="/drug-id" element={<DrugIdentification />} />
                <Route path="/consultation" element={<RemoteConsultation />} />
                <Route path="/outbreak" element={<OutbreakAlert />} />
              </Routes>
            </div>
          </main>
        </div>
      </div>
    </Router>
  );
};

export default App;