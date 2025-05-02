import React, { useState } from 'react';
import '../styles/theme.css';

const Widget = () => {
    const [position, setPosition] = useState({ x: 100, y: 100 });
    const [theme, setTheme] = useState('light');

    const handleDrag = (e) => {
        if (e.clientX && e.clientY) {
            setPosition({ x: e.clientX, y: e.clientY });
        }
    };

    const toggleTheme = () => {
        setTheme(theme === 'light' ? 'dark' : 'light');
    };

    console.log('Position:', position);
    console.log('Theme:', theme);

    return (
        <div
            className={`widget ${theme}`}
            style={{ left: position.x, top: position.y }}
            draggable
            onDragEnd={handleDrag}
        >
            <h3>Interactive Widget</h3>
            <button onClick={toggleTheme}>Toggle Theme</button>
        </div>
    );
};

export default Widget;
