import React, { useState } from "react";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input) {
      const newMessages = [...messages, { user: "User", text: input }];
      setMessages(newMessages);
      setInput("");
      
      // Simulate an AI response
      const aiResponse = "Here's your AI-generated YouTube script!";
      setTimeout(() => {
        setMessages([...newMessages, { user: "AI", text: aiResponse }]);
      }, 1000);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index}>
            <strong>{msg.user}: </strong>{msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        placeholder="Type your prompt here..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={(e) => e.key === "Enter" && handleSend()}
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default Chat;
