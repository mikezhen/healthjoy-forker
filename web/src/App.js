import { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.forkRepo = this.forkRepo.bind(this);
  }

  forkRepo() {
    // Fork the repo
  }

  render() {
    return (
      <div className="App">
        <h2>Welcome to HealthJoy Forker</h2>
        <a href="/auth/login" className="btn btn-primary">
          <i className="fab fa-github" /> Sign in with Github
        </a>
        <a href="/fork" className="btn btn-success">
          <i className="fas fa-code-branch" /> Fork
        </a>
      </div>
    )
  }
}

export default App;
