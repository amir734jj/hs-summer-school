import React, { Component } from 'react';
import './App.css';
import axios from 'axios';


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      html: '',
    };
  }

  getHtml = async event => {
    const markdown = event.target.value;
    const response = await axios.post('http://localhost:5000/md', { markdown });
    this.setState({ html: response.data });
  }

  render() {
    return (
      <div className='container-fluid' >
        <h3>python - markdown </h3>
        <div className='container' >
          <div className='row' >
            <div className='col-sm-12' >
              <textarea className={'form-control'} onChange={this.getHtml} rows='10'></textarea>
            </div>
            <div className='col-sm-12'>
              <hr />
            </div>
            <div className='col-sm-12' dangerouslySetInnerHTML={{ __html: this.state.html }}>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;