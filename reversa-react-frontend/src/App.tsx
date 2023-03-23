import React from 'react';
import logo from './assets/logo.svg';
import './App.css';
import { Room } from './entities/room';
import { Feature } from './entities/feature';

function App() {
  var features = {} as Feature;
  var room = {name: "TestRoom", id: 1, } as Room;
  

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
      </header>
    </div>
  );
}

export default App;
