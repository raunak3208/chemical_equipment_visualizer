"use client"
import { Download } from "lucide-react"
import { equipmentAPI } from "../services/api"
import "./Summary.css"

export default function Summary({ summary, onDownload }) {
  const handleDownloadReport = async () => {
    try {
      const response = await equipmentAPI.downloadReport()
      const url = window.URL.createObjectURL(response.data)
      const link = document.createElement("a")
      link.href = url
      link.setAttribute("download", "equipment_report.pdf")
      document.body.appendChild(link)
      link.click()
      link.parentNode.removeChild(link)
      window.URL.revokeObjectURL(url)
    } catch (err) {
      console.error("PDF download error:", err)
      alert("Failed to download report: " + (err.response?.data?.error || err.message))
    }
  }

  if (!summary) return null

  return (
    <div className="summary-container">
      <h2>Summary Statistics</h2>
      <div className="summary-grid">
        <div className="stat-card">
          <h3>Total Equipment</h3>
          <p className="stat-value">{summary.total_equipment}</p>
        </div>
        <div className="stat-card">
          <h3>Avg Flowrate</h3>
          <p className="stat-value">{summary.avg_flowrate?.toFixed(2)}</p>
        </div>
        <div className="stat-card">
          <h3>Avg Pressure</h3>
          <p className="stat-value">{summary.avg_pressure?.toFixed(2)}</p>
        </div>
        <div className="stat-card">
          <h3>Avg Temperature</h3>
          <p className="stat-value">{summary.avg_temperature?.toFixed(2)}</p>
        </div>
      </div>

      <button onClick={handleDownloadReport} className="download-button">
        <Download size={20} />
        Download PDF Report
      </button>
    </div>
  )
}
