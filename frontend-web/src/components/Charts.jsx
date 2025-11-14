import {
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts"
import "./Charts.css"

export default function Charts({ summary, data }) {
  if (!summary) return null

  const typeData = Object.entries(summary.equipment_types || {}).map(([type, count]) => ({
    name: type,
    value: count,
  }))

  const COLORS = ["#1a56db", "#7e3bff", "#00a8e8", "#00c9a7", "#ffa502", "#ff6b6b"]

  const avgData = [
    { name: "Flowrate", value: summary.avg_flowrate?.toFixed(2) || 0 },
    { name: "Pressure", value: summary.avg_pressure?.toFixed(2) || 0 },
    { name: "Temperature", value: summary.avg_temperature?.toFixed(2) || 0 },
  ]

  return (
    <div className="charts-container">
      <h2>Analytics & Visualizations</h2>

      <div className="charts-grid">
        <div className="chart-card">
          <h3>Equipment Type Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={typeData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, value }) => `${name}: ${value}`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {typeData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h3>Average Parameters</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={avgData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value" fill="#1a56db" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {data && data.length > 0 && (
        <div className="chart-card chart-full">
          <h3>Parameter Trends</h3>
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={data.slice(0, 20)}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="equipment_name" angle={-45} textAnchor="end" height={80} />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="flowrate" stroke="#1a56db" strokeWidth={2} />
              <Line type="monotone" dataKey="pressure" stroke="#00a8e8" strokeWidth={2} />
              <Line type="monotone" dataKey="temperature" stroke="#ffa502" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  )
}
