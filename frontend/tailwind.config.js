/**
 * Tailwind configuration for M3DP-UIP.
 * Notes:
 *  - Safelist utility classes used via dynamic component rendering (glass effects).
 *  - Content globs include Nuxt config and composables to ensure class extraction.
 */
export default {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './stores/**/*.{js,ts}',
    './composables/**/*.{js,ts}',
    './app.vue',
    './nuxt.config.{js,ts}',
  ],
  safelist: [
    // Glass morphism utility classes referenced in templates and potential future dynamic injection
    'glass',
    'glass-dark'
  ],
  theme: {
    extend: {
      colors: {
        // minimal3dp.com brand colors
        brand: {
          orange: '#F97316',
        },
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
}
