module.exports = {
    map: process.env.NODE_ENV === 'production' && {inline: false},
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
        require('postcss-combine-media-query'),
        process.env.NODE_ENV === 'production' && require('cssnano')({
            preset: 'default',
        }),
    ]
}
