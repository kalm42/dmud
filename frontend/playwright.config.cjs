const { defineConfig } = require("@playwright/test");

module.exports = defineConfig({
  testDir: "../tests/e2e",
  use: { browserName: "chromium" },
  webServer: [
    {
      command:
        "cd ../backend && DMUD_LLM_API_KEY=canary-private-credential-123 PYTHONPATH=src uv run uvicorn dmud.main:app --host 127.0.0.1 --port 8000",
      url: "http://127.0.0.1:8000/api/status",
      reuseExistingServer: false,
    },
    {
      command: "npm run dev -- --host 127.0.0.1 --port 5173 --strictPort",
      url: "http://127.0.0.1:5173",
      reuseExistingServer: false,
    },
    {
      command:
        "DMUD_API_PROXY_TARGET=http://127.0.0.1:8999 npm run dev -- --host 127.0.0.1 --port 5174 --strictPort",
      url: "http://127.0.0.1:5174",
      reuseExistingServer: false,
    },
  ],
});
