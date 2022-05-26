
import standings_data from './backend_data/standings.json'
import Standings from './Components/Standings'
import './App.css';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <Standings
        standingsJSON = {standings_data}
        />
      </header>
    </div>
  );
}

export default App;
