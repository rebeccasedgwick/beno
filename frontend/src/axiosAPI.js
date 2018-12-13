import axios from 'axios';

const axiosAPI = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL,
});

axiosAPI.CancelToken = axios.CancelToken;
axiosAPI.isCancel = axios.isCancel;

axiosAPI.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },

  error => Promise.reject(error),
);

export default axiosAPI;
