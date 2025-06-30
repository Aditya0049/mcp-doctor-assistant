import React from "react";
import ChatBox from "../src/components/ChatBox";

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold p-6">Welcome to MCP Doc Agent</h1>
      <ChatBox />
    </div>
  );
};

export default HomePage;
