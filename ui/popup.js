const suggestionBox = document.getElementById("commitSuggestion");
const copyBtn = document.getElementById("copyBtn");
const regenBtn = document.getElementById("regenBtn");

// Dummy default (replace this with API call)
async function fetchCommitSuggestion() {
  suggestionBox.value = "Thinking...";
  
  const prTitle = "Fix login bug";
  const prBody = "Resolved a problem with the login redirect and added logging.";

  const response = await fetch("http://localhost:5000/suggest-commit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title: prTitle, body: prBody })
  });

  const data = await response.json();
  suggestionBox.value = data.suggestion || "Failed to fetch suggestion.";
}

copyBtn.addEventListener("click", () => {
  navigator.clipboard.writeText(suggestionBox.value);
  copyBtn.textContent = "✅ Copied!";
  setTimeout(() => copyBtn.textContent = "📋 Copy", 2000);
});

regenBtn.addEventListener("click", () => {
  fetchCommitSuggestion();
});

fetchCommitSuggestion(); // Load on open
