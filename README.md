# NewsAgent: AI Trend Research Crew

NewsAgent is an automated AI research and writing tool powered by [CrewAI](https://github.com/joaomoura/crewai). This project deploys a team of specialized AI agents to autonomously search the web, uncover groundbreaking technology trends, and draft comprehensive, highly-structured blog posts or reports.

## 🚀 Features

* **Autonomous Research:** Utilizes the `SerperDevTool` to search the web for the latest, up-to-date information on any given tech topic.
* **Multi-Agent Collaboration:** Employs a dual-agent system consisting of a "Senior Researcher" to gather data and a "Writer" to synthesize the findings into an engaging format.
* **Powered by Gemini:** Uses Google's `gemini-2.5-flash` language model for high-quality, efficient text generation and reasoning.
* **Markdown Output:** Automatically generates clean, ready-to-publish Markdown files (e.g., `new_blog_post.md`) containing the final report.

## 📋 Prerequisites

Before running the project, you will need to set up API keys for both the LLM and the search tool:

1. **Google API Key:** Required to access the `gemini-2.5-flash` model. [Get an API key from Google AI Studio](https://aistudio.google.com/).
2. **Serper API Key:** Required for the internet search tool. [Get an API key from Serper.dev](https://serper.dev/).

## 🛠️ Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/Nitishamadeshiya/newsagent.git
   cd newsagent
