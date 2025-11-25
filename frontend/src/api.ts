import axios from 'axios';

const BASE_URL = import.meta.env.VITE_BASE_URL;

// Instance
const api = axios.create({
  baseURL: `${BASE_URL}`,
});

// Save token
export const saveTokens = (access: string, refresh: string) => {
  localStorage.setItem('access', access);
  localStorage.setItem('refresh', refresh);
};
// load token
const getAccessToken = () => localStorage.getItem('access');
const getRefreshToken = () => localStorage.getItem('refresh');

// Attach access token to every request
api.interceptors.request.use(
  (config) => {
    const token = getAccessToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

const refreshAccessToken = async () => {
  const refresh = getRefreshToken();
  if (!refresh) return null;

  try {
    const response = await axios.post(`${BASE_URL}refresh/`, {
      refresh: refresh,
    });
    const newAccess = response.data.access;
    const newRefresh = response.data.refresh ?? refresh;
    saveTokens(newAccess, newRefresh);

    return newAccess;
  } catch (err) {
    return null;
  }
};

// Interceptor for auto refresh
api.interceptors.response.use(
  (response) => response,

  async (error) => {
    if (!error.response) return Promise.reject(error);

    const originalRequest = error.config;

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      const newAccess = await refreshAccessToken();

      if (newAccess) {
        originalRequest.headers['Authorization'] = `Bearer ${newAccess}`;
        return api(originalRequest);
      }

      // Refresh failed → redirect to login
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      window.location.href = '/auth/login';
    }

    return Promise.reject(error);
  }
);

export default api;
