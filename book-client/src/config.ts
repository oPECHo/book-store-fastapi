const isDev = process.env.NODE_ENV || process.env.NODE_ENV === 'development'

const config = {
    isDev,
    remoteRepositoryUrlPrefix: isDev ? 'http://localhost:8000/api' : '/api'
}
export default config
