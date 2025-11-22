// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Removed non-standard compatibilityDate property (Cloudflare-specific) to avoid unexpected plugin behavior
  devtools: { enabled: true },

  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],

  // Explicit global CSS registration to ensure Tailwind directives are processed
  css: ['~/assets/css/main.css'],

  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config',
    exposeConfig: false,
    viewer: true,
  },

  app: {
    head: {
      title: 'M3DP-UIP - AI-Powered 3D Printing Diagnostics',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: 'Minimal 3DP Unified Intelligence Platform - AI-powered diagnostic platform for 3D printing troubleshooting and calibration.'
        },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },

  // Runtime config for API endpoints
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
    }
  },

  typescript: {
    strict: true,
    typeCheck: true,
  },

  // Remove SCSS preprocessor injection (unused) to reduce CSS pipeline complexity during debugging
  vite: {
    css: {
      preprocessorOptions: {}
    }
  }
})
