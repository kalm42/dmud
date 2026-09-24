const { defineConfig } = require("@playwright/test");
const { randomBytes } = require("node:crypto");

const canary = `canary-private-credential-${randomBytes(16).toString("hex")}`;
process.env.DMUD_TEST_CANARY = canary;

module.exports = defineConfig({
  testDir: "../tests/e2e",
  use: { browserName: "chromium" },
  webServer: [
    {
      command:
        "cd ../backend && uv run uvicorn dmud.main:app --host 127.0.0.1 --port 8000",
      env: { DMUD_LLM_API_KEY: canary, PYTHONPATH: "src" },
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
