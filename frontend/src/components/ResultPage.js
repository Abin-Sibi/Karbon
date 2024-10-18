import React from 'react';

function ResultsPage({ result }) {
  return (
    <div>
      <h2>Financial Analysis Result</h2>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}

export default ResultsPage;
