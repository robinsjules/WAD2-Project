import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'https://maps.googleapis.com/maps/api/place/nearbysearch/json',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      '/api2': {
        target: 'http:127.0.0.1:5000/get_profile/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api2/, ''),
      },
    },
  },
});

