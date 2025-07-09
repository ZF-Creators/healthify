function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    const chatBox = document.getElementById("chat-box");

    if (!message) return;

    // Show user's message
    const userMsg = document.createElement("div");
    userMsg.className = "user-msg";
    userMsg.textContent = message;
    chatBox.appendChild(userMsg);

    // Scroll to latest
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input
    input.value = "";

    // Show bot is thinking
    const thinkingMsg = document.createElement("div");
    thinkingMsg.className = "bot-thinking";
    thinkingMsg.textContent = "Bot is thinking...";
    chatBox.appendChild(thinkingMsg);

    // Send to backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        // Remove thinking message
        thinkingMsg.remove();

        const botMsg = document.createElement("div");
        botMsg.className = "bot-msg";

        if (data.error) {
            botMsg.textContent = `❌ ${data.error}`;
        } else {
            const predictions = data.predictions
                .map(([disease, prob]) => `${disease} (${(prob * 100).toFixed(1)}%)`)
                .join(", ");
            const matched = data.matched.length ? `Matched Symptoms: ${data.matched.join(", ")}` : "";

            botMsg.innerHTML = `
                🤖 Possible diseases: <br><strong>${predictions}</strong><br>
                <small>${matched}</small>
            `;
        }

        chatBox.appendChild(botMsg);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        thinkingMsg.remove();
        const errorMsg = document.createElement("div");
        errorMsg.className = "bot-msg";
        errorMsg.textContent = "❌ Server error. Please try again later.";
        chatBox.appendChild(errorMsg);
    });
}
