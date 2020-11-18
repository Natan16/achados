const { join } = require('path')
const _apimock = process.env.API_MOCK == '1' || (process.env.API_MOCK == undefined && process.env.npm_lifecycle_event == 'dev')
const _apijs = _apimock ? 'apimock.js' : 'api.js';

module.exports = {
  head: {
    title: 'frontend',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'google-signin-client_id', content: '649795675193-qiheujqkem1i9k0r7boqr0o0c9n5rk83.apps.googleusercontent.com'},
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Google+Sans:400,500|Material+Icons' }
    ],
    script: [
        {
          src: 'https://apis.google.com/js/platform.js',
          defer: true,
          async: true
        }
      ]


  },
  css: [
    { src: '~/assets/css/main.styl', lang: 'styl' },
    "@mdi/font/css/materialdesignicons.css"
  ],

  loading: { color: '#3B8070' },
  router: {
    middleware: ['fwdcookies', 'auth'],
  },
  build: {
    vendor: [
      'vuetify',
      'babel-polyfill'
    ],
    extend (config, { isDev, isClient }) {
      home = config.resolve.alias['~'];
      config.resolve.alias['~apijs'] = home + '/components/api/' + _apijs;
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  plugins: [
    '~plugins/vuetify.js',
    {src: '~plugins/vue2-filters', ssr: false},
  ],
  modules: [
    ['@nuxtjs/pwa', {
      manifest: {
        name: 'achados',
        short_name: 'achados',
        lang: 'pt-BR',
        theme_color: 'blue',
      },
      workbox: {
      }
    }],
  ]
}
