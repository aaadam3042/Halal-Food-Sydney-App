import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [data, setdata] = useState({
    api_version: "",
  });

  useEffect(() => {
    fetch("/api/").then((res) =>
        res.json().then((data) => {
            setdata({
                api_version: data.api_version,
            });
        })
    );
}, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <p> API_Version = {data.api_version} </p>
      </header>
    </div>
  );
}

export default App;
