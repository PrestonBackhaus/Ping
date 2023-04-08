import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function launchGUI() {
  axios.get('http://localhost:5000/launch')
    .then(response => console.log(response.data.message))
    .catch(error => console.log(error));
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <button onClick={launchGUI}>Launch GUI</button>
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
