import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import FileUpload from './components/FileUpload';
import ResultsPage from './components/ResultPage';


function App() {
  const [result, setResult] = useState(null);

  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<FileUpload setResult={setResult} />} />
          <Route path="/results" element={<ResultsPage result={result} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
