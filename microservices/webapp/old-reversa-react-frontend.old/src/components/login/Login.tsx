import React, { useState } from 'react';
import { Form, Button, Alert } from 'react-bootstrap';

interface LoginProps {
    onLogin: (username: string, password: string) => void;
}

export function Login({ onLogin }: LoginProps) {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [errorMessage, setErrorMessage] = useState<string>('');

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if (username && password) {
            // Call the onLogin function with the username and password
            onLogin(username, password);
            setUsername('');
            setPassword('');
            setErrorMessage('');
        } else {
            setErrorMessage('Please enter a username and password.');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <Form onSubmit={handleSubmit}>
                <Form.Group controlId="formBasicUsername">
                    <Form.Label>Username:</Form.Label>
                    <Form.Control
                        type="text"
                        placeholder="Enter username"
                        value={username}
                        onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
                            setUsername(event.target.value)
                        }
                    />
                </Form.Group>
                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password:</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Enter password"
                        value={password}
                        onChange={(event: React.ChangeEvent<HTMLInputElement>) =>
                            setPassword(event.target.value)
                        }
                    />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Log in
                </Button>
                {errorMessage && <Alert variant="danger">{errorMessage}</Alert>}
            </Form>
        </div>
    );
};