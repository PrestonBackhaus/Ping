import './App.css'; // Importing CSS file for App component
import axios from 'axios'; // Importing Axios library for HTTP requests
import monkeys_dancing from './images/monkeys_dancing.gif'; // Importing gif file for App component

function launchGUI() {
  axios.get('http://localhost:5001/launch') // Making a GET request to '/launch' route to launch the GUI
    .then(response => console.log(response.data.message)) // Log message returned from server
    .catch(error => console.log(error)); // Log error if any
}

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Website Checker</h1>
      </header>
      <main className="app-main">
        <img src={monkeys_dancing} alt="Monkeys Dancing" className="monkeys-gif" />
        <div className="container">
          <div className="launch-text">
            <p>Launch website checker below:</p>
          </div>
          <button onClick={launchGUI} className="launch-button">Launch GUI</button>
          <div className="description">
            <p>This app takes a web address and will check/replace every 
              character of a specific language with its relative character 
              in English. It then returns all found online and offline 
              websites that exist.</p>
          </div>
        </div>
      </main>
      <footer className="app-footer">
        <p>&copy; 2023 Website Checker. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App; // Exporting App component as default
