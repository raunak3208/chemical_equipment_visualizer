"use client"

import { useState, useRef } from "react"
import { equipmentAPI } from "../services/api"
import { Upload, AlertCircle } from "lucide-react"
import "./UploadForm.css"

export default function UploadForm({ onUploadSuccess }) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [success, setSuccess] = useState("")
  const fileInputRef = useRef(null)

  const handleFileChange = async (e) => {
    const file = e.target.files?.[0]
    if (!file) return

    setLoading(true)
    setError("")
    setSuccess("")

    try {
      const response = await equipmentAPI.upload(file)
      setSuccess(`Successfully uploaded ${response.data.total_equipment} equipment records`)
      setTimeout(() => {
        onUploadSuccess()
        setSuccess("")
      }, 1500)
    } catch (err) {
      setError(err.response?.data?.error || "Upload failed")
    } finally {
      setLoading(false)
      if (fileInputRef.current) fileInputRef.current.value = ""
    }
  }

  return (
    <div className="upload-form">
      <div className="upload-card">
        <h2>Upload CSV File</h2>
        <label className="upload-label">
          <div className="upload-box">
            <Upload size={40} />
            <p>Click to upload or drag and drop</p>
            <span>CSV files with equipment data</span>
          </div>
          <input ref={fileInputRef} type="file" accept=".csv" onChange={handleFileChange} disabled={loading} hidden />
        </label>

        {error && (
          <div className="alert alert-error">
            <AlertCircle size={20} />
            <span>{error}</span>
          </div>
        )}

        {success && (
          <div className="alert alert-success">
            <span>✓ {success}</span>
          </div>
        )}
      </div>
    </div>
  )
}
