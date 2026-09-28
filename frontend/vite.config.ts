import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

const proxyTarget =
  process.env.DMUD_API_PROXY_TARGET ?? "http://127.0.0.1:8000";
const proxyUrl = new URL(proxyTarget);
if (proxyUrl.protocol !== "http:" || proxyUrl.hostname !== "127.0.0.1") {
  throw new Error("DMUD_API_PROXY_TARGET must use HTTP on 127.0.0.1");
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      "/api": proxyTarget,
    },
  },
});
