import React, { useState } from 'react';
import styles from './Login.module.css';

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleFormSubmit = (event) => {
        event.preventDefault();
        // Ваша логика обработки входа здесь
    };

    return (
        <div className={styles.loginForm}>
            <h2>Вход</h2>
            <form onSubmit={handleFormSubmit}>
                <div className={styles.formGroup}>
                    <label htmlFor="username">Логин:</label>
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={handleUsernameChange}
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="password">Пароль:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={handlePasswordChange}
                    />
                </div>
                <button type="submit">Войти</button>
            </form>
        </div>
    );
};

export default LoginForm;