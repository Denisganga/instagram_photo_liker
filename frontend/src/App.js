import React from 'react';
import LoginForm from './components/LoginForm';

const App = () => {
    const handleLogin = async (username, password) => {
        console.log('Sending credentials:', { username, password });

        try {
            const response = await fetch('http://localhost:8000/api/like-photos/', { // Corrected URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            console.log('Response:', data);
        } catch (error) {
            console.error('Fetch error:', error);
        }
    };

    return (
        <div className="App">
            <h1>Instagram Liker</h1>
            <LoginForm onSubmit={handleLogin} />
        </div>
    );
};

export default App;
