import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";

// NOTE: this app is served through Django via django-vite. The Django
// templates reference "src/main.js" and "src/styles/*". Keep the rollup
// inputs and the `@` alias pointing at wherever the frontend source lives.
// In this (flattened) checkout the source sits at the repo root, so `@` → root.
export default defineConfig({
  plugins: [vue(), tailwindcss()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL(".", import.meta.url)),
    },
  },
  base: process.env.NODE_ENV === "production" ? "/static/" : "/",
  build: {
    manifest: "manifest.json",
    outDir: "static/dist",
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: fileURLToPath(new URL("./main.js", import.meta.url)),
        imports: fileURLToPath(new URL("./styles/imports.css", import.meta.url)),
        style: fileURLToPath(new URL("./styles/style.scss", import.meta.url)),
      },
    },
  },
  server: {
    origin: "http://localhost:5173",
  },
});
