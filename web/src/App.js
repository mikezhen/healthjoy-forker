import { Component, Fragment } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    this.isAuthenticated = this.isAuthenticated.bind(this);
    this.forkRepo = this.forkRepo.bind(this);
    this.clearAlert = this.clearAlert.bind(this);

    this.state = {
      authenticated: false,
      alert: null
    }
  }

  componentDidMount() {
    fetch('/auth')
      .then(resp => this.setState({
        authenticated: resp.status === 200
      }))
      .catch(err => console.log(err))
  }

  isAuthenticated() {
    return this.state.authenticated
  }

  forkRepo() {
    const requestOptions = { method: 'POST' }
    fetch('/github/fork', requestOptions)
      .then(resp => {
        if (resp.ok) {
          this.setState({
            alert: {
              status: 'success',
              message: 'Successfully forked the repo as your own.'
            }
          });
        } else {
          this.setState({
            alert: {
              status: 'danger',
              message: 'Issue came up while forking the repo.'
            }
          }, this.clearAlert)
        }
      })
  }

  clearAlert() {
    setTimeout(() => this.setState({ alert: null }), 3000);
  }

  render() {
    return (
      <Fragment>
        {
          this.state.alert ?
            <div className={`alert alert-${this.state.alert?.status}`} role="alert">
              <h4>{this.state.alert?.message}</h4>
            </div>
            :
            null
        }
        <div className="App">
          <h2>Welcome to HealthJoy Forker</h2>
          {
            this.isAuthenticated() ?
            <Fragment>
              <h6>Do you want to fork this repo?</h6>
              <button onClick={this.forkRepo} className="btn btn-success">
                <i className="fas fa-code-branch" /> Fork
              </button>
            </Fragment>
            :
            <a href="/auth/login" className="btn btn-primary">
              <i className="fab fa-github" /> Sign in with Github
            </a>
          }
        </div>
      </Fragment>
    )
  }
}

export default App;
