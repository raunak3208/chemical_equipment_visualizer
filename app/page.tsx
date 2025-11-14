import { ArrowRight, Code2, Database, Monitor, Zap } from "lucide-react"

export default function Page() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      {/* Header */}
      <header className="border-b border-slate-700/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center">
                <Zap className="w-6 h-6" />
              </div>
              <h1 className="text-2xl font-bold">Equipment Visualizer</h1>
            </div>
            <div className="hidden sm:flex gap-4">
              <a href="#setup" className="text-sm text-slate-300 hover:text-white transition-colors">
                Setup
              </a>
              <a href="#features" className="text-sm text-slate-300 hover:text-white transition-colors">
                Features
              </a>
            </div>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-32">
        <div className="text-center space-y-6">
          <h2 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-balance">
            Chemical Equipment Parameter Visualizer
          </h2>
          <p className="text-lg sm:text-xl text-slate-300 text-balance max-w-2xl mx-auto">
            A complete hybrid application with Django backend, React web frontend, and PyQt5 desktop application for
            monitoring and analyzing chemical equipment parameters.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-8">
            <a
              href="#getting-started"
              className="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 transition-all font-semibold"
            >
              Get Started <ArrowRight className="w-4 h-4" />
            </a>
            <a
              href="#documentation"
              className="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg border border-slate-600 hover:border-slate-400 hover:bg-slate-700/50 transition-all font-semibold"
            >
              Documentation
            </a>
          </div>
        </div>
      </section>

      {/* Architecture */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h3 className="text-3xl font-bold mb-12 text-center">Triple-Stack Architecture</h3>
        <div className="grid sm:grid-cols-3 gap-6">
          {/* Backend */}
          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-8 hover:border-blue-500/50 transition-colors">
            <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center mb-4">
              <Database className="w-6 h-6" />
            </div>
            <h4 className="text-xl font-bold mb-3">Backend API</h4>
            <p className="text-slate-300 mb-4 text-sm">Django + Django REST Framework with SQLite database</p>
            <ul className="text-sm text-slate-400 space-y-2">
              <li>✓ User authentication</li>
              <li>✓ CSV processing with Pandas</li>
              <li>✓ Equipment analytics</li>
              <li>✓ PDF report generation</li>
              <li>✓ History tracking (last 5 uploads)</li>
            </ul>
          </div>

          {/* Web Frontend */}
          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-8 hover:border-cyan-500/50 transition-colors">
            <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-cyan-500 to-cyan-600 flex items-center justify-center mb-4">
              <Code2 className="w-6 h-6" />
            </div>
            <h4 className="text-xl font-bold mb-3">Web Frontend</h4>
            <p className="text-slate-300 mb-4 text-sm">React.js with Recharts visualization</p>
            <ul className="text-sm text-slate-400 space-y-2">
              <li>✓ Responsive dashboard</li>
              <li>✓ Real-time charts</li>
              <li>✓ CSV upload interface</li>
              <li>✓ PDF download</li>
              <li>✓ Data tables</li>
            </ul>
          </div>

          {/* Desktop App */}
          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-8 hover:border-emerald-500/50 transition-colors">
            <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-emerald-500 to-emerald-600 flex items-center justify-center mb-4">
              <Monitor className="w-6 h-6" />
            </div>
            <h4 className="text-xl font-bold mb-3">Desktop App</h4>
            <p className="text-slate-300 mb-4 text-sm">PyQt5 with Matplotlib visualization</p>
            <ul className="text-sm text-slate-400 space-y-2">
              <li>✓ Native PyQt5 UI</li>
              <li>✓ Matplotlib charts</li>
              <li>✓ CSV upload</li>
              <li>✓ Data management</li>
              <li>✓ Report generation</li>
            </ul>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t border-slate-700">
        <h3 className="text-3xl font-bold mb-12 text-center">Key Features</h3>
        <div className="grid sm:grid-cols-2 gap-6">
          {[
            { title: "User Authentication", desc: "Token-based authentication for secure access" },
            { title: "CSV Processing", desc: "Upload and process equipment data with Pandas" },
            { title: "Real-time Analytics", desc: "Automatic calculation of statistics and distributions" },
            { title: "Data Visualization", desc: "Interactive charts with Recharts and Matplotlib" },
            { title: "PDF Reports", desc: "Generate professional reports with ReportLab" },
            { title: "History Tracking", desc: "Automatic history of last 5 uploads" },
            { title: "Cross-Platform", desc: "Works on web, desktop, and mobile browsers" },
            { title: "Production Ready", desc: "Clean code, error handling, and validation" },
          ].map((feature, i) => (
            <div key={i} className="flex gap-4">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-500 flex items-center justify-center">
                  <span className="text-sm font-bold">✓</span>
                </div>
              </div>
              <div>
                <h4 className="font-semibold mb-1">{feature.title}</h4>
                <p className="text-sm text-slate-400">{feature.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Getting Started */}
      <section id="getting-started" className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t border-slate-700">
        <h3 className="text-3xl font-bold mb-12 text-center">Getting Started</h3>

        <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-8 space-y-8">
          <div>
            <h4 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <span className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-sm font-bold">
                1
              </span>
              Backend Setup
            </h4>
            <pre className="bg-slate-900 rounded p-4 overflow-x-auto text-sm text-slate-300">
              {`cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver`}
            </pre>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <span className="w-8 h-8 rounded-full bg-cyan-500 flex items-center justify-center text-sm font-bold">
                2
              </span>
              Web Frontend Setup
            </h4>
            <pre className="bg-slate-900 rounded p-4 overflow-x-auto text-sm text-slate-300">
              {`cd frontend-web
npm install
npm run dev`}
            </pre>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <span className="w-8 h-8 rounded-full bg-emerald-500 flex items-center justify-center text-sm font-bold">
                3
              </span>
              Desktop App Setup
            </h4>
            <pre className="bg-slate-900 rounded p-4 overflow-x-auto text-sm text-slate-300">
              {`cd frontend-desktop
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py`}
            </pre>
          </div>

          <div>
            <h4 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <span className="w-8 h-8 rounded-full bg-amber-500 flex items-center justify-center text-sm font-bold">
                4
              </span>
              Test with Sample Data
            </h4>
            <p className="text-slate-300 mb-3">
              Use the provided sample CSV file:{" "}
              <code className="bg-slate-900 px-2 py-1 rounded text-sm">data/sample_equipment_data.csv</code>
            </p>
            <p className="text-slate-400 text-sm">
              Upload it through the web app or desktop app to populate with test data and verify everything works.
            </p>
          </div>
        </div>
      </section>

      {/* Access Points */}
      <section id="documentation" className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t border-slate-700">
        <h3 className="text-3xl font-bold mb-12 text-center">Access Points</h3>

        <div className="grid sm:grid-cols-3 gap-6">
          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-3">Backend API</h4>
            <code className="text-sm bg-slate-900 rounded px-3 py-2 block mb-2">http://localhost:8000</code>
            <p className="text-sm text-slate-400">Django REST API endpoints</p>
          </div>

          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-3">Web Application</h4>
            <code className="text-sm bg-slate-900 rounded px-3 py-2 block mb-2">http://localhost:5173</code>
            <p className="text-sm text-slate-400">React web dashboard</p>
          </div>

          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-3">Admin Panel</h4>
            <code className="text-sm bg-slate-900 rounded px-3 py-2 block mb-2">http://localhost:8000/admin</code>
            <p className="text-sm text-slate-400">Django administration</p>
          </div>
        </div>
      </section>

      {/* Project Files */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t border-slate-700">
        <h3 className="text-3xl font-bold mb-12 text-center">Project Files</h3>

        <div className="grid sm:grid-cols-2 gap-6">
          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-4 text-blue-400">Documentation</h4>
            <ul className="space-y-2 text-sm text-slate-300">
              <li>• PROJECT_DOCUMENTATION.md - Architecture & API reference</li>
              <li>• SETUP_GUIDE.md - Complete setup instructions</li>
              <li>• README.md - Quick start guide</li>
              <li>• QUICK_REFERENCE.md - Common commands</li>
            </ul>
          </div>

          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-4 text-cyan-400">Data</h4>
            <ul className="space-y-2 text-sm text-slate-300">
              <li>• sample_equipment_data.csv - 15 sample records</li>
              <li>• Columns: Equipment Name, Type, Flowrate, Pressure, Temperature</li>
              <li>• Ready for testing all features</li>
            </ul>
          </div>

          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-4 text-emerald-400">Backend Files</h4>
            <ul className="space-y-2 text-sm text-slate-300">
              <li>• config/settings.py - Django configuration</li>
              <li>• equipment_api/models.py - Database models</li>
              <li>• equipment_api/views.py - API endpoints</li>
              <li>• requirements.txt - Python dependencies</li>
            </ul>
          </div>

          <div className="rounded-lg border border-slate-700 bg-slate-800/50 p-6">
            <h4 className="font-semibold mb-4 text-amber-400">Frontend Files</h4>
            <ul className="space-y-2 text-sm text-slate-300">
              <li>• frontend-web/ - React app with Recharts</li>
              <li>• frontend-desktop/ - PyQt5 desktop app</li>
              <li>• Both connect to same backend API</li>
            </ul>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-700/50 bg-slate-900/50 mt-20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="text-center text-slate-400 text-sm">
            <p>Chemical Equipment Parameter Visualizer - Hybrid Application</p>
            <p className="mt-2">Django Backend • React Web • PyQt5 Desktop</p>
          </div>
        </div>
      </footer>
    </main>
  )
}
