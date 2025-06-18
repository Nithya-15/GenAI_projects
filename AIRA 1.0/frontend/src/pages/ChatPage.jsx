import React from "react";
import ChatInterface from "../components/ChatInterface";

export default function ChatPage() {
  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Ask AIRA</h2>
      <ChatInterface />
    </div>
  );
}
