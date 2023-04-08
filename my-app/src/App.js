import './App.css'; // Importing CSS file for App component
import axios from 'axios'; // Importing Axios library for HTTP requests
import monkeys_dancing from './images/monkeys_dancing.gif'; // Importing gif file for App component

function launchGUI() {
  axios.get('http://localhost:5000/launch') // Making a GET request to '/launch' route to launch the GUI
    .then(response => console.log(response.data.message)) // Log message returned from server
    .catch(error => console.log(error)); // Log error if any
}

function App() {
  return (
    <div>
      <img src={monkeys_dancing} alt="Monkeys Dancing" className="monkeys-gif" />
      <div className="container">
        {/* Remember this is how to create a comment in the html portions */}
          {/* Text above button */}
          <div className="launch-text">
            <p>Launch website checker below:</p>
          </div>
          <button onClick={launchGUI}>Launch GUI</button>
          {/* Comment for description div */}
          <div className="description">
            <p>This app takes a web address and will check/replace every 
              character of a specific language with its relative character 
              in English. It then returns all found online and offline 
              websites that exist.</p>
          </div>
      </div>
    </div>
  );
}

export default App; // Exporting App component as default
