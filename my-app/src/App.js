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
        <div className="launch-text">
          <p>Launch website checker below:</p>
        </div>
        <button onClick={launchGUI}>Launch GUI</button>
        <div className="description">
          <p>This app takes a web address and will check/replace every 
            character of a specific language with its relative character 
            in English. It then returns all found online and offline 
            websites that exist.</p>
        </div>
    </div>
  );
}

export default App;
