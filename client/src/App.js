import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Router, Link, Switch, Routes } from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Fake Reddit (The Real Reddit)</h1>
        {/* <Router>
          <Switch>
            <Routes></Routes>
          </Switch>
        </Router> */}
      </div>
    );
  }
}

export default App;
