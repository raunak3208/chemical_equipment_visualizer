import "./DataTable.css"

export default function DataTable({ data }) {
  if (!data || data.length === 0) {
    return <div className="table-empty">No equipment data available</div>
  }

  return (
    <div className="table-container">
      <h2>Equipment Data</h2>
      <table className="data-table">
        <thead>
          <tr>
            <th>Equipment Name</th>
            <th>Type</th>
            <th>Flowrate</th>
            <th>Pressure</th>
            <th>Temperature</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, idx) => (
            <tr key={idx}>
              <td>{item.equipment_name}</td>
              <td>{item.equipment_type}</td>
              <td>{item.flowrate.toFixed(2)}</td>
              <td>{item.pressure.toFixed(2)}</td>
              <td>{item.temperature.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
