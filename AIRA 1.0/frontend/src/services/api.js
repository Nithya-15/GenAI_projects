const API_URL = "http://localhost:8000"; // Adjust if deployed

export async function askQuestion(userQuery) {
  const response = await fetch(`${API_URL}/chat/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_query: userQuery }),
  });
  if (!response.ok) {
    throw new Error("Failed to get response from server");
  }
  return response.json();
}

export async function smartSearch(query) {
  const response = await fetch(`${API_URL}/search/smart-search`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  if (!response.ok) {
    throw new Error("Failed to search documents");
  }
  return response.json();
}

export async function extractKeywords(query) {
  const response = await fetch(`${API_URL}/search/keywords`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });
  if (!response.ok) {
    throw new Error("Failed to extract keywords");
  }
  return response.json();
}
