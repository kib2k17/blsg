/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./restaurant/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          red: "#C0392B",
          dark: "#922B21",
          gold: "#D4AC0D",
        },
        surface: {
          900: "#111111",
          800: "#1C1C1E",
          700: "#2A2A2A",
          500: "#8E8E93",
          400: "#AEAEB2",
          300: "#C7C7CC",
          200: "#E5E5EA",
          100: "#F2F2F7",
        },
      },
      fontFamily: {
        display: ["Playfair Display", "Georgia", "serif"],
        body: ["Jost", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};
