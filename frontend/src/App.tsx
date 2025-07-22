import { useEffect, useRef, useState } from "react";

type Message = {
  role: "user" | "ai";
  text: string;
};

type Role = "patient" | "doctor";

export default function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [role, setRole] = useState<Role>("patient");
  const chatEndRef = useRef<HTMLDivElement | null>(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { role: "user", text: input }]);
    setLoading(true);

    try {
      const res = await fetch("https://mcp-doctor-assistant.onrender.com", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: input }),
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "ai", text: data.response }]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "ai", text: "❌ Error reaching backend" },
      ]);
    }

    setInput("");
    setLoading(false);
  };

  const handleManualRequest = (prompt: string) => {
    setInput(prompt);
    sendMessage();
  };

  return (
    <div className="min-h-screen bg-gradient-to-tr from-blue-50 to-indigo-100 p-6 flex flex-col items-center">
      <div className="max-w-3xl w-full space-y-6">
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold text-indigo-700">🩺 Doctor Assistant</h1>
          <select
            value={role}
            onChange={(e) => setRole(e.target.value as Role)}
            className="border px-3 py-1 rounded-xl"
          >
            <option value="patient">Patient</option>
            <option value="doctor">Doctor</option>
          </select>
        </div>

        {/* Chat Window */}
        <div className="bg-white rounded-2xl shadow p-5 h-[450px] overflow-y-auto space-y-4 border">
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
              <div
                className={`px-4 py-2 rounded-2xl max-w-[75%] text-sm ${
                  msg.role === "user"
                    ? "bg-indigo-600 text-white"
                    : "bg-gray-200 text-gray-800"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}
          {loading && (
            <div className="flex justify-start">
              <div className="italic text-gray-700 text-sm">🤖 Thinking...</div>
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        {/* Input Area */}
        <div className="flex gap-3">
          <input
            className="flex-1 border border-indigo-300 rounded-xl p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
            placeholder="Ask to book, check availability, or get summary..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            disabled={loading}
          />
          <button
            className="bg-indigo-600 text-white px-5 py-2 rounded-xl hover:bg-indigo-700 disabled:opacity-50"
            onClick={sendMessage}
            disabled={loading}
          >
            {loading ? "..." : "Send"}
          </button>
        </div>

        {/* Helper Buttons */}
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-sm">
          {role === "patient" && (
            <>
              <button
                onClick={() => handleManualRequest("Book an appointment with Dr. Ahuja tomorrow morning")}
                className="bg-white border border-indigo-300 rounded-xl py-2 px-3 shadow hover:bg-indigo-50"
              >
                Book Dr. Ahuja
              </button>
              <button
                onClick={() => handleManualRequest("Check Dr. Ahuja’s availability for Friday")}
                className="bg-white border border-indigo-300 rounded-xl py-2 px-3 shadow hover:bg-indigo-50"
              >
                Check availability
              </button>
            </>
          )}
          {role === "doctor" && (
            <>
              <button
                onClick={() => handleManualRequest("Give me a summary of yesterday’s patients")}
                className="bg-white border border-indigo-300 rounded-xl py-2 px-3 shadow hover:bg-indigo-50"
              >
                🗓 Yesterday's summary
              </button>
              <button
                onClick={() => handleManualRequest("How many patients had fever yesterday?")}
                className="bg-white border border-indigo-300 rounded-xl py-2 px-3 shadow hover:bg-indigo-50"
              >
                🤒 Fever stats
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
