import React, { useState } from 'react';
import "./chatbot.css";

const Chatbot = () => {
    const [messages, setMessages] = useState([]);

    const handleMessageSend = (messageText) => {
        // You can handle message sending logic here
        // For demonstration, let's just add the message to state
        setMessages([...messages, { text: messageText, sender: 'user' }]);
    };

    return (
      <div className="chatbot-container">
        <div className="chat-messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              {message.text}
            </div>
          ))}
        </div>
        <input
          type="text"
        />
        response.text
        <input
          type="text"
          placeholder="Type your message..."
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              handleMessageSend(e.target.value);
              e.target.value = ''; // Clear input after sending
            }
          }}
          className="chat-input"
        />
      </div>
    );
  };
  
  export default Chatbot;
