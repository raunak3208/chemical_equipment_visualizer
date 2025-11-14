import "./History.css"

export default function History({ batches }) {
  if (!batches || batches.length === 0) {
    return <div className="history-empty">No upload history</div>
  }

  return (
    <div className="history-container">
      <h2>Upload History (Last 5)</h2>
      <div className="history-list">
        {batches.map((batch) => (
          <div key={batch.id} className="history-item">
            <div className="history-header">
              <h3>{batch.filename}</h3>
              <span className="history-date">{new Date(batch.created_at).toLocaleString()}</span>
            </div>
            <div className="history-stats">
              <span>{batch.total_equipment} equipment</span>
              <span>Flowrate: {batch.avg_flowrate.toFixed(2)}</span>
              <span>Pressure: {batch.avg_pressure.toFixed(2)}</span>
              <span>Temperature: {batch.avg_temperature.toFixed(2)}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
