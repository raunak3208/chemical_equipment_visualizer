"use client"

import { useState } from "react"
import { authAPI } from "../services/api"
import "./Login.css"

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const [isRegister, setIsRegister] = useState(false)
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError("")
    setLoading(true)

    try {
      let response
      if (isRegister) {
        response = await authAPI.register(username, password, email)
      } else {
        response = await authAPI.login(username, password)
      }

      localStorage.setItem("token", response.data.token)
      localStorage.setItem("user", JSON.stringify(response.data.user))
      onLogin(response.data.user)
    } catch (err) {
      setError(err.response?.data?.error || "Authentication failed")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="login-container">
      <div className="login-card">
        <h1 className="login-title">Equipment Visualizer</h1>
        <form onSubmit={handleSubmit} className="login-form">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="input-field"
            required
          />
          {isRegister && (
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input-field"
              required
            />
          )}
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="input-field"
            required
          />
          {error && <div className="error-message">{error}</div>}
          <button type="submit" className="submit-button" disabled={loading}>
            {loading ? "Loading..." : isRegister ? "Register" : "Login"}
          </button>
        </form>
        <button
          onClick={() => {
            setIsRegister(!isRegister)
            setError("")
          }}
          className="toggle-button"
        >
          {isRegister ? "Already have an account? Login" : "No account? Register"}
        </button>
      </div>
    </div>
  )
}
