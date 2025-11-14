"use client"

import { useState, useEffect } from "react"
import { LogOut } from "lucide-react"
import { equipmentAPI, authAPI } from "./services/api"
import Login from "./components/Login"
import UploadForm from "./components/UploadForm"
import DataTable from "./components/DataTable"
import Charts from "./components/Charts"
import Summary from "./components/Summary"
import History from "./components/History"
import "./App.css"

export default function App() {
  const [user, setUser] = useState(null)
  const [summary, setSummary] = useState(null)
  const [data, setData] = useState([])
  const [history, setHistory] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const storedUser = localStorage.getItem("user")
    if (storedUser) {
      setUser(JSON.parse(storedUser))
      loadData()
    }
  }, [])

  const loadData = async () => {
    setLoading(true)
    try {
      const [summaryRes, dataRes, historyRes] = await Promise.all([
        equipmentAPI.getSummary(),
        equipmentAPI.getData(),
        equipmentAPI.getHistory(),
      ])
      setSummary(summaryRes.data)
      setData(dataRes.data)
      setHistory(historyRes.data)
    } catch (err) {
      console.error("Failed to load data")
    } finally {
      setLoading(false)
    }
  }

  const handleLogin = (userData) => {
    setUser(userData)
    loadData()
  }

  const handleLogout = async () => {
    try {
      await authAPI.logout()
    } catch (err) {
      console.error("Logout error")
    }
    localStorage.clear()
    setUser(null)
    setSummary(null)
    setData([])
    setHistory([])
  }

  if (!user) {
    return <Login onLogin={handleLogin} />
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Chemical Equipment Parameter Visualizer</h1>
        <div className="user-info">
          <span>Welcome, {user.username}</span>
          <button onClick={handleLogout} className="logout-button">
            <LogOut size={20} />
            Logout
          </button>
        </div>
      </header>

      <main className="app-main">
        <UploadForm onUploadSuccess={loadData} />
        <Summary summary={summary} />
        <Charts summary={summary} data={data} />
        <DataTable data={data} />
        <History batches={history} />
      </main>
    </div>
  )
}
