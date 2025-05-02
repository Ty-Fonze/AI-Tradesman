import React from 'react';
import LiveTickerWidget from './components/LiveTickerWidget';

const App = () => {
    return (
        <div>
            <h1>Hello, React!</h1>
            <LiveTickerWidget title="Stock Market Live Updates" />
        </div>
    );
};

export default App;
