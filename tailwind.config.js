module.exports = {
  purge: [
      './bookmarks_collection/templates/**/*.html',
  ],
  theme: {
    extend: {
      gridTemplateColumns: {
        'auto-xs': `repeat(auto-fill, minmax(12rem, 1fr))`,
        'auto-sm': `repeat(auto-fill, minmax(16rem, 1fr))`,
        'auto-md': `repeat(auto-fill, minmax(20rem, 1fr))`,
        'auto-lg': `repeat(auto-fill, minmax(24rem, 1fr))`,
        'auto-xl': `repeat(auto-fill, minmax(28rem, 1fr))`,
      },
      gridColumn: {
        'span-all': '1 / -1'
      }
    },
  },
  variants: {},
  plugins: [],
}
