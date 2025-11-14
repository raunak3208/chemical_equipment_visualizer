import axios from "axios"

const API_BASE = "http://localhost:8000/api"

let token = localStorage.getItem("token")

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    "Content-Type": "application/json",
  },
})

api.interceptors.request.use((config) => {
  token = localStorage.getItem("token")
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }
  return config
})

export const authAPI = {
  login: (username, password) => api.post("/auth/login/", { username, password }),
  register: (username, password, email) => api.post("/auth/register/", { username, password, email }),
  logout: () => api.post("/auth/logout/"),
}

export const equipmentAPI = {
  upload: (file) => {
    const formData = new FormData()
    formData.append("file", file)
    return api.post("/upload/", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    })
  },
  getSummary: () => api.get("/summary/"),
  getHistory: () => api.get("/history/"),
  getData: () => api.get("/data/"),
  downloadReport: () => api.post("/download-report/", {}, { responseType: "blob" }),
}