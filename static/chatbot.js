async function sendMessage() {
    const input = document.getElementById("user-input");
    const msg = input.value.trim();
    if (!msg) return;

    const chatBox = document.getElementById("chat-box");

    // Add user message bubble
    const userBubble = document.createElement("div");
    userBubble.className = "user-msg";
    userBubble.innerText = msg;
    chatBox.appendChild(userBubble);

    input.value = "";

    // Add "Bot is thinking..." message
    const thinkingBubble = document.createElement("div");
    thinkingBubble.className = "bot-thinking";
    thinkingBubble.innerText = "🤖 Bot is thinking...";
    chatBox.appendChild(thinkingBubble);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // Send to backend
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });

        const data = await res.json();

        // Remove thinking message
        thinkingBubble.remove();

        // Create bot response
        const botBubble = document.createElement("div");
        botBubble.className = "bot-msg";

        if (data.error) {
            botBubble.innerText = "❌ " + data.error;
        } else {
            let html = "<strong>🤖 I think it could be:</strong><ul>";
            data.predictions.forEach(([disease, prob]) => {
                const percent = (prob * 100).toFixed(2);
                const link = `https://www.google.com/search?q=${encodeURIComponent(disease + " symptoms")}`;
                html += `<li>${disease} — ${percent}% 
                            <a href="${link}" target="_blank" class="read-more">🔍 Read more</a>
                        </li>`;
            });
            html += "</ul>";

            if (data.matched && data.matched.length > 0) {
                html += `<p><strong>🧩 Matched Symptoms:</strong> ${data.matched.join(", ")}</p>`;
            }

            botBubble.innerHTML = html;
        }

        chatBox.appendChild(botBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (err) {
        thinkingBubble.remove();

        const errorBubble = document.createElement("div");
        errorBubble.className = "bot-msg";
        errorBubble.innerText = "⚠️ Something went wrong. Please try again.";
        chatBox.appendChild(errorBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
