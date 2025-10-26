async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();
  if (!message) return;

  const userMsg = document.createElement("div");
  userMsg.classList.add("message", "user");
  userMsg.textContent = message;
  chatBox.appendChild(userMsg);

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const res = await fetch("http://127.0.0.1:8000/api/chatbot", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    if (!res.ok) throw new Error("Server error");
    const data = await res.json();

    const botMsg = document.createElement("div");
    botMsg.classList.add("message", "bot");
    botMsg.textContent = data.response;
    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

  } catch (err) {
    const errMsg = document.createElement("div");
    errMsg.classList.add("message", "bot");
    errMsg.textContent = "Error connecting to server.";
    chatBox.appendChild(errMsg);
  }
}
