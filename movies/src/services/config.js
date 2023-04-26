import axios from 'axios';

const URL = "http://127.0.0.1:8000/"
  
const axiosInstance = axios.create({
  baseURL: URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    'Accept-Language': 'es-es'
  },
})

export default axiosInstance