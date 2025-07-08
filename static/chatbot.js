document.addEventListener("DOMContentLoaded", () => {
    const botResponse = document.querySelector(".bot-response");
    const form = document.querySelector("form");
    const textarea = form.querySelector("textarea");

    // Scroll to the bottom of the response
    if (botResponse) {
        botResponse.scrollIntoView({ behavior: "smooth" });
    }

    // Simulate typing effect (optional)
    const simulateTyping = (element, delay = 25) => {
        const text = element.innerText;
        element.innerText = "";
        let index = 0;

        const typing = setInterval(() => {
            element.innerText += text[index];
            index++;
            if (index >= text.length) {
                clearInterval(typing);
            }
        }, delay);
    };

    // Animate each disease result if exists
    if (botResponse) {
        const listItems = botResponse.querySelectorAll("li");
        listItems.forEach((item, i) => {
            item.style.opacity = 0;
            setTimeout(() => {
                item.style.opacity = 1;
                simulateTyping(item, 15);
            }, i * 300);
        });
    }

    // Clear textarea on submit
    form.addEventListener("submit", () => {
        setTimeout(() => {
            textarea.value = "";
        }, 100);
    });
});
