import React from "react";
import { useNavigate } from "react-router-dom";

export default function HomePage() {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-white">
      <h1 className="text-4xl font-bold mb-4">AIRA 1.0 🤖</h1>
      <p className="text-lg text-gray-600 mb-8">
        Accelerating Knowledge Retrieval from Scientific Literature
      </p>
      <button
        className="bg-green-500 text-white px-6 py-3 rounded-lg"
        onClick={() => navigate("/chat")}
      >
        Get Started
      </button>
    </div>
  );
}
