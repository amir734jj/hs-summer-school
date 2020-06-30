import React from 'react';
import logo from './logo.svg';
import './App.css';

const HowCoolIsAmir = (props) => (
	<button onClick={() => alert('Very awesome')}> How cool is Amir </button>
);

const StateLessComponent = (props) => 
	(<h2 className='cool'> StateLess! {props.name} </h2>);

class StateFull extends React.Component {
	constructor(props) {
  	super(props);
  }

  render() {
  	return (<h2 className='not-cool'> StateFull! {this.props.name} </h2>);
  }
}

const Wrapper = (props) => (<div>
  <StateLessComponent {...props} />
  <StateFull {...props} />
  <HowCoolIsAmir />
</div>);

function App() {
  return (
    <div className="App">
        <Wrapper name='Amir' age='12' />
   </div>
  );
}

export default App;
