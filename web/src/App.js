import { Component, Fragment } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.isAuthenticated = this.isAuthenticated.bind(this);

    this.state = {
      authenticated: false
    }
  }

  componentDidMount() {
    fetch('/auth')
      .then(resp => this.setState({
        authenticated: resp.status === 200
      }))
  }

  isAuthenticated() {
    return this.state.authenticated
  }

  render() {
    return (
      <div className="App">
        <h2>Welcome to HealthJoy Forker</h2>
        {
          this.isAuthenticated() ?
          <Fragment>
            <h6>Do you want to fork this repo?</h6>
            <a href="/fork" className="btn btn-success">
              <i className="fas fa-code-branch" /> Fork
            </a>
          </Fragment>
          :
          <a href="/auth/login" className="btn btn-primary">
            <i className="fab fa-github" /> Sign in with Github
          </a>
        }
      </div>
    )
  }
}

export default App;
