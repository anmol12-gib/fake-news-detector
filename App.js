import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [headline, setHeadline] = useState('');
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setHeadline(e.target.value);
  };

  const handleClear = () => {
    setHeadline('');
    setResult(null);
  };

  const handleAnalyze = async () => {
    if (!headline.trim()) {
      alert('Please enter a headline to analyze.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:5000/predict', {
        headline,
      });

      setResult(response.data);
    } catch (error) {
      console.error('Error analyzing headline:', error);
      alert('Failed to analyze the headline.');
    }
  };

  return (
    <div className="container">
      <h1 className="heading">📰 Fake News Detector</h1>

      <div className="input-box">
        <input
          type="text"
          value={headline}
          onChange={handleChange}
          placeholder="Enter a news headline..."
        />
        <div className="button-group">
          <button className="analyze-btn" onClick={handleAnalyze}>
            Analyze
          </button>
          <button className="clear-btn" onClick={handleClear}>
            Clear
          </button>
        </div>
      </div>

      {result && (
        <div className="result-box">
          <div className={`result-label ${result.prediction === 'Real News' ? 'real' : 'fake'}`}>
            ✅ {result.prediction}
          </div>
          <div className="confidence">Confidence: {result.confidence}%</div>
          {result.summary && (
            <div className="summary">📝 Summary: {result.summary}</div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
