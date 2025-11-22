// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],

  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config',
    exposeConfig: false,
    viewer: true,
  },

  // Inline PostCSS plugins (Tailwind + Autoprefixer) replacing external postcss.config.cjs
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    }
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
      ],
      script: [
        // GA4 script (uses env var or fallback project ID)
        {
          src: `https://www.googletagmanager.com/gtag/js?id=${process.env.NUXT_PUBLIC_GA_ID || 'G-VQ8RPWC2MK'}`,
          async: true
        },
        {
          // Inline gtag init using 'innerHTML' key supported by Nuxt app.head
          innerHTML: `window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', '${process.env.NUXT_PUBLIC_GA_ID || 'G-VQ8RPWC2MK'}', { debug_mode: ${process.env.NUXT_PUBLIC_GA_DEBUG === 'true' ? 'true' : 'false'} });`,
          type: 'text/javascript'
        }
      ]
    }
  },

  // Runtime config for API endpoints
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
      gaMeasurementId: process.env.NUXT_PUBLIC_GA_ID || 'G-VQ8RPWC2MK'
    }
  },

  typescript: {
    strict: true,
    typeCheck: true,
  },

  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "@/assets/scss/vars.scss" as *;'
        }
      }
    }
  }
})
